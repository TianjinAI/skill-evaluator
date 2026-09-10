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
    def test_round_title_must_not_repeat_round_prefix(self):
        self.data['round1']['title']='Round 1 · Generic review'
        with self.assertRaises(ValueError):renderer.render(self.data)
        self.data['round1']['title']='Generic review'
        self.assertIn('Round 1 · Generic review',renderer.render(self.data))
    def test_scorecard_note_renders_as_prose_before_the_table(self):
        self.data['round1']['scorecard_note']='**How to read**: score and confidence are independent.'
        out=renderer.render(self.data)
        self.assertLess(out.index('How to read'),out.index('Category</th>'))
        self.assertIn('<span class="lb">How to read</span>',out)
    def test_prose_lines_and_inline_markers(self):
        self.data['round1']['summary']='Lead line.\n**Key point**: body text.\n\u3000\u3000- subordinate note.'
        out=renderer.render(self.data)
        self.assertIn('<span class="lb">Key point</span> body text.',out)
        self.assertIn('<span class="ln note">subordinate note.</span>',out)
        self.assertIn('<span class="ln">Lead line.</span>',out)
        self.assertNotIn('**',out)
    def test_prose_does_not_pass_through_html(self):
        self.data['round1']['summary']='<strong>x</strong>\n**<script>alert(1)</script>**\n`<img src=x>`'
        out=renderer.render(self.data)
        self.assertNotIn('<script>',out)
        self.assertNotIn('<img',out)
        self.assertIn('&lt;strong&gt;x&lt;/strong&gt;',out)
        self.assertIn('<span class="lb">&lt;script&gt;alert(1)&lt;/script&gt;</span>',out)
    def test_score_band_is_printed_beside_point_score(self):
        row=self.data['round1']['scorecard'][0]
        row.pop('band',None)
        row['score']=3
        self.assertIn('<td>3</td>',renderer.render(self.data))
        row['band']='2\u20134'
        out=renderer.render(self.data)
        self.assertIn('<td>3 (2\u20134)</td>',out)
        self.assertNotIn('italic',out)
    def test_bad_score_bands_rejected(self):
        row=self.data['round1']['scorecard'][0]
        row['score']=3
        for band in ['4\u20132','1\u20135x','0\u20133','3\u20133.5','2 to 4','','\u20133',3]:
            row['band']=band
            with self.subTest(band=band),self.assertRaises(ValueError):renderer.render(self.data)
        row['band']='2\u20134';row['score']='NE'
        with self.assertRaises(ValueError):renderer.render(self.data)
    def test_prose_preserves_negative_values_and_literal_markers(self):
        out=renderer.prose('-74 penalty\n- -128 starting value\n--flag\n*literal\n**Label**: -28')
        for value in ('-74 penalty','-128 starting value','--flag','*literal','-28'):
            self.assertIn(value,out)
        self.assertNotIn('>74 penalty',out)
    def test_band_contains_point_score(self):
        row=self.data['round1']['scorecard'][0]
        row['score']=3
        for band in ['1–2','4–5']:
            row['band']=band
            with self.subTest(band=band),self.assertRaises(ValueError):renderer.render(self.data)
    def test_nontext_prose_rejected(self):
        self.data['round1']['summary']=None
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
