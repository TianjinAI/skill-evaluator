#!/usr/bin/env python3
"""Render an authored review JSON as offline HTML; no evaluation or network calls."""
import argparse
from html import escape
import json
from pathlib import Path
import sys
from urllib.parse import urlsplit

CSS = '''
:root{color-scheme:light;--ink:#162b35;--muted:#52646c;--line:#d6e0e3;--accent:#087f80}
*{box-sizing:border-box}body{margin:0;background:#f1f5f5;color:var(--ink);font:16px/1.65 system-ui,sans-serif}
main{max-width:1120px;margin:auto;padding:40px 28px 80px}header{border-top:6px solid var(--accent);padding:24px;background:#fff}
h1{font-size:clamp(26px,4vw,42px);line-height:1.2;margin:8px 0 18px}h2{font-size:28px;margin-top:40px}h3{font-size:20px}
p{overflow-wrap:anywhere}.meta{color:var(--muted);font-size:14px}.verdict{border-left:4px solid var(--accent);padding:14px 20px;background:#e4f2f0}
.private{padding:12px 20px;background:#fff0d1;border:1px solid #bc8b28}section{background:white;padding:20px 24px;margin:20px 0;border:1px solid var(--line)}
a{color:#066365;overflow-wrap:anywhere}nav{display:flex;gap:24px;flex-wrap:wrap;padding-top:14px}.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid var(--line);min-width:100px;overflow-wrap:anywhere}th{background:#edf4f4}ul{padding-left:24px}
@media(max-width:640px){main{padding:16px 12px 40px}section,header{padding:16px}}
@media print{body{background:white;font-size:11pt}main{max-width:none;padding:0}nav{display:none}section{padding:8px 0;border:0}h2,h3{break-after:avoid}tr{break-inside:avoid}.table-wrap{overflow:visible}th,td{min-width:0;padding:5px;font-size:9pt}a{color:inherit}}
'''


def txt(value):
    if not isinstance(value, str):
        raise ValueError('Report text must be a string')
    return escape(value, quote=True)


def table(headers, rows):
    if not headers or not isinstance(rows, list):
        raise ValueError('Tables need headers and rows')
    if any(len(row) != len(headers) for row in rows):
        raise ValueError('Table row width differs from headers')
    return '<div class="table-wrap"><table><thead><tr>' + ''.join('<th scope="col">'+txt(h)+'</th>' for h in headers) + '</tr></thead><tbody>' + ''.join('<tr>'+''.join('<td>'+txt(c)+'</td>' for c in row)+'</tr>' for row in rows) + '</tbody></table></div>'


def round_html(data, number):
    out = [f'<article id="round-{number}"><h2>Round {number} · '+txt(data['title'])+'</h2>', '<p class="verdict">'+txt(data['verdict'])+'</p>']
    out.append('<p>'+txt(data['summary'])+'</p>')
    for section in data.get('sections', []):
        out.append('<section><h3>'+txt(section['title'])+'</h3>')
        out.extend('<p>'+txt(p)+'</p>' for p in section.get('paragraphs', []))
        if section.get('bullets'):
            out.append('<ul>'+''.join('<li>'+txt(p)+'</li>' for p in section['bullets'])+'</ul>')
        if 'table' in section:
            out.append(table(section['table']['headers'], section['table']['rows']))
        out.append('</section>')
    scores = data.get('scorecard', [])
    if scores:
        rows=[]
        for row in scores:
            score=row['score']
            if not ((type(score) is int and 1 <= score <= 5) or (isinstance(score,str) and score in ('NE','NA'))):
                raise ValueError('Scores must be whole numbers 1–5, NE or NA')
            for key in ('category','confidence','evidence','scope','rationale'):
                if not isinstance(row.get(key),str) or not row[key].strip():
                    raise ValueError('Every score requires '+key)
            rows.append([row['category'],str(score),row['confidence'],row['evidence'],row['scope'],row['rationale']])
        out.append('<section><h3>'+txt(data.get('scorecard_title','Category scorecard'))+'</h3>'+table(['Category','Score','Confidence','Evidence','Scope','Rationale'],rows)+'</section>')
    for key in ('gates','checks'):
        if data.get(key):
            out.append('<section><h3>'+txt(data.get(key+'_title',key.title()))+'</h3>'+table(data[key]['headers'],data[key]['rows'])+'</section>')
    if data.get('sources'):
        out.append('<section><h3>'+txt(data.get('sources_title','Evidence sources'))+'</h3><ul>')
        for source in data['sources']:
            url=source.get('url','')
            label=txt(source['id']+' — '+source['label'])
            if url:
                parsed=urlsplit(url)
                if parsed.scheme not in ('https','http') or not parsed.netloc or parsed.username or parsed.password or any(c.isspace() for c in url):
                    raise ValueError('Source links must be credential-free HTTP(S) URLs')
                label='<a href="'+txt(url)+'" rel="noreferrer">'+label+'</a>'
            out.append('<li>'+label+'</li>')
        out.append('</ul></section>')
    out.append('</article>')
    return ''.join(out)


def render(data, include_round_2=False):
    # Generic metadata must itself be sanitized; omitting Round 2 is not a privacy audit.
    meta=data['metadata']
    lang=txt(meta.get('language','en'))
    out=['<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="referrer" content="no-referrer"><title>'+txt(meta['title'])+'</title><style>'+CSS+'</style></head><body><main>']
    if include_round_2:
        if not data.get('round2'):
            raise ValueError('Round 2 requested but absent')
        out.append('<p class="private">PRIVATE · Includes user-specific context. Local file; not published.</p>')
    out.append('<header><p class="meta">SKILL EVALUATOR · '+txt(meta['date'])+'</p><h1>'+txt(meta['title'])+'</h1><p class="meta">'+txt(meta['candidate'])+' · '+txt(meta['revision'])+' · '+txt(meta['scope'])+'</p><nav><a href="#round-1">Round 1</a>')
    if include_round_2:
        out.append('<a href="#round-2">Round 2</a>')
    out.append('</nav></header>'+round_html(data['round1'],1))
    if include_round_2:
        out.append(round_html(data['round2'],2))
    out.append('<footer class="meta">Evidence-scoped assessment. Scores are ordinal judgments; unknowns are not passes. No aggregate score.</footer></main></body></html>')
    return ''.join(out)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input',type=Path)
    parser.add_argument('output',type=Path)
    parser.add_argument('--include-round-2',action='store_true',help='Explicitly include private suitability notes')
    args=parser.parse_args(argv)
    try:
        html=render(json.loads(args.input.read_text(encoding='utf-8')),args.include_round_2)
        with args.output.open('x',encoding='utf-8') as f:
            f.write(html)
        print(args.output.resolve())
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print('Report not written: '+str(exc),file=sys.stderr)
        return 1
    return 0

if __name__=='__main__':
    sys.exit(main())
