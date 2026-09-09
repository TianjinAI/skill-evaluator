import importlib.util
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('init_review', ROOT/'scripts/init_review.py')
init = importlib.util.module_from_spec(spec)
spec.loader.exec_module(init)

class Initializer(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.parent = Path(self.tmp.name)
        self.dest = self.parent/'review'

    def test_generic_has_no_private_profile(self):
        init.create_review(self.dest, '示例', 'v1')
        self.assertEqual({p.name for p in self.dest.iterdir()}, {'round-1.md', 'evidence.csv'})
        self.assertIn('示例', (self.dest/'round-1.md').read_text())
        self.assertIn('DRAFT', (self.dest/'round-1.md').read_text())

    def test_both_rounds_remain_distinct(self):
        init.create_review(self.dest, 'Example', 'v1', 'both')
        self.assertEqual(len(list(self.dest.iterdir())), 4)
        self.assertIn('private context', (self.dest/'round-2.md').read_text())
        self.assertIn('no runs performed', (self.dest/'pilot.md').read_text())

    def test_existing_directory_untouched(self):
        self.dest.mkdir()
        (self.dest/'keep').write_text('user work')
        with self.assertRaises(FileExistsError):
            init.create_review(self.dest, 'Example')
        self.assertEqual((self.dest/'keep').read_text(), 'user work')
        self.assertEqual(len(list(self.dest.iterdir())), 1)

    def test_symlink_not_followed(self):
        target = self.parent/'target'; target.mkdir()
        try:
            self.dest.symlink_to(target, target_is_directory=True)
        except OSError:
            self.skipTest('symlinks unavailable on this host')
        with self.assertRaises(FileExistsError):
            init.create_review(self.dest, 'Example')
        self.assertEqual(list(target.iterdir()), [])

    def test_invalid_input_leaves_no_directory(self):
        for package in ('', '  ', 'a\nb'):
            with self.subTest(package=package), self.assertRaises(ValueError):
                init.create_review(self.dest, package)
        self.assertFalse(self.dest.exists())

    def test_missing_templates_leave_no_directory(self):
        with patch.object(init, 'TEMPLATES', self.parent/'missing'), self.assertRaises(FileNotFoundError):
            init.create_review(self.dest, 'Example')
        self.assertFalse(self.dest.exists())

    def test_write_failure_removes_new_directory(self):
        with patch.object(Path, 'write_text', side_effect=OSError('disk full')), self.assertRaises(OSError):
            init.create_review(self.dest, 'Example')
        self.assertFalse(self.dest.exists())

    def test_cli_status_for_existing_destination(self):
        self.dest.mkdir()
        self.assertEqual(init.main([str(self.dest), '--package', 'Example']), 1)

class Package(unittest.TestCase):
    def test_relative_document_links_resolve(self):
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                with self.subTest(file=path.relative_to(ROOT), target=target):
                    self.assertTrue((path.parent/target.split('#')[0]).exists())

    def test_version_is_semantic(self):
        self.assertRegex((ROOT/'VERSION').read_text().strip(), r'^\d+\.\d+\.\d+$')

if __name__ == '__main__':
    unittest.main()
