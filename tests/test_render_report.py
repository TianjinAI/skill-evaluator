import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('render_report',ROOT/'scripts/render_report.py')
renderer=importlib.util.module_from_spec(spec);spec.loader.exec_module(renderer)

class Report(unittest.TestCase):
    def setUp(self):
        self.data=json.loads((ROOT/'examples/report-input.json').read_text())
    def test_generic_omits_private_round(self):
        self.data['round2']['summary']='SECRET-INVENTORY'
        self.assertNotIn('SECRET-INVENTORY',renderer.render(self.data))
        self.assertIn('SECRET-INVENTORY',renderer.render(self.data,True))
        self.assertIn('PRIVATE',renderer.render(self.data,True))
    def test_candidate_text_is_not_active_html(self):
        self.data['round1']['summary']='<script>alert(1)</script>'
        out=renderer.render(self.data)
        self.assertNotIn('<script>',out)
        self.assertIn('&lt;script&gt;',out)
    def test_unsafe_source_urls_rejected(self):
        for url in ['javascript:alert(1)','data:text/html,hi','https://user:pass@example.com','https://exa\nmple.com']:
            self.data['round1']['sources'][0]['url']=url
            with self.subTest(url=url),self.assertRaises(ValueError): renderer.render(self.data)
    def test_bad_scores_and_missing_provenance_rejected(self):
        row=self.data['round1']['scorecard'][0]
        for score in [0,6,3.5,True,'3','unknown']:
            row['score']=score
            with self.subTest(score=score),self.assertRaises(ValueError):renderer.render(self.data)
        row['score']=3;row['evidence']=''
        with self.assertRaises(ValueError):renderer.render(self.data)
    def test_unicode_and_complete_tables(self):
        self.data['metadata']['title']='评估报告'
        out=renderer.render(self.data,True)
        self.assertIn('评估报告',out)
        for row in self.data['round2']['scorecard']:self.assertIn(row['category'],out)
        self.data['round1']['checks']['rows'][0].append('extra')
        with self.assertRaises(ValueError):renderer.render(self.data)
    def test_cli_refuses_overwrite_and_symlink(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/'in.json';src.write_text(json.dumps(self.data))
            dest=Path(d)/'out.html'
            self.assertEqual(renderer.main([str(src),str(dest)]),0)
            original=dest.read_bytes()
            self.assertEqual(renderer.main([str(src),str(dest)]),1)
            self.assertEqual(dest.read_bytes(),original)
            link=Path(d)/'link.html';link.symlink_to(dest)
            self.assertEqual(renderer.main([str(src),str(link)]),1)
            self.assertEqual(dest.read_bytes(),original)
    def test_invalid_input_does_not_create_output(self):
        with tempfile.TemporaryDirectory() as d:
            src=Path(d)/'in.json';src.write_text('{}')
            out=Path(d)/'out.html'
            self.assertEqual(renderer.main([str(src),str(out)]),1)
            self.assertFalse(out.exists())
if __name__=='__main__':unittest.main()
