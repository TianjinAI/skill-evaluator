#!/usr/bin/env python3
"""Create draft review files in a new directory. No network or candidate execution."""
import argparse
from pathlib import Path
import shutil
import sys

TEMPLATES = Path(__file__).resolve().parents[1] / 'templates'

def create_review(destination, package, revision='unresolved', rounds='generic'):
    if rounds not in ('generic', 'both'):
        raise ValueError('rounds must be generic or both')
    if not package.strip() or any(c in package + revision for c in '\r\n\x00'):
        raise ValueError('package and revision must be single-line text; package must not be blank')
    files = ['round-1.md', 'evidence.csv']
    if rounds == 'both':
        files += ['round-2.md', 'pilot.md']
    # Read before creating anything, so a damaged installation cannot leave a partial review.
    payloads = {name: (TEMPLATES / name).read_text(encoding='utf-8') for name in files}
    destination = Path(destination)
    # Do not resolve an existing symlink into somebody else's directory.
    destination.mkdir()  # deliberately exclusive, parent must already exist
    try:
        for name, content in payloads.items():
            content = content.replace('{{PACKAGE}}', package).replace('{{REVISION}}', revision)
            (destination / name).write_text(content, encoding='utf-8')
    except Exception:
        shutil.rmtree(destination)
        raise
    return destination

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', help='new directory; its parent must already exist')
    parser.add_argument('--package', required=True)
    parser.add_argument('--revision', default='unresolved')
    parser.add_argument('--rounds', choices=['generic', 'both'], default='generic')
    args = parser.parse_args(argv)
    try:
        path = create_review(args.destination, args.package, args.revision, args.rounds)
    except (OSError, ValueError) as exc:
        print(f'Cannot create review: {exc}', file=sys.stderr)
        return 1
    print(f'Created draft review: {path.resolve()}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
