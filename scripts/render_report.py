#!/usr/bin/env python3
"""Render an authored review JSON as offline HTML; no evaluation or network calls."""
import argparse
from html import escape
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

BAND_RE = re.compile(r'([1-5])[-\u2013]([1-5])')

CSS = '''
:root{color-scheme:light;--ink:#162b35;--muted:#52646c;--line:#d6e0e3;--accent:#087f80}
*{box-sizing:border-box}body{margin:0;background:#f1f5f5;color:var(--ink);font:16px/1.65 system-ui,sans-serif}
main{max-width:1120px;margin:auto;padding:40px 28px 80px}header{border-top:6px solid var(--accent);padding:24px;background:#fff}
h1{font-size:clamp(26px,4vw,42px);line-height:1.2;margin:8px 0 18px}h2{font-size:28px;margin-top:40px}h3{font-size:20px}
p{overflow-wrap:anywhere;margin:0 0 14px}.meta{color:var(--muted);font-size:14px}.verdict{border-left:4px solid var(--accent);padding:14px 20px;background:#e4f2f0}
.private{padding:12px 20px;background:#fff0d1;border:1px solid #bc8b28}section{background:white;padding:20px 24px;margin:20px 0;border:1px solid var(--line)}
a{color:#066365;overflow-wrap:anywhere}nav{display:flex;gap:24px;flex-wrap:wrap;padding-top:14px}.table-wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;vertical-align:top;padding:10px;border-bottom:1px solid var(--line);min-width:100px;overflow-wrap:anywhere}th{background:#edf4f4}
footer{margin-top:28px;border-top:1px solid var(--line);padding-top:16px}
.private,.table-wrap{overflow-wrap:anywhere}
/*
 Prose blocks are authored as emphasised, structured notes. This block is the entire rendering
 contract; text not listed here is escaped literal text and must stay readable as a paragraph.
*/
.prose{font-size:15px}
.prose strong{font-weight:650;color:#0d2b33}
.prose code{font:13px/1.5 ui-monospace,SFMono-Regular,Menlo,monospace;background:#eef4f4;border:1px solid #dbe6e6;border-radius:3px;padding:1px 5px}
.prose .ln{display:block;padding-left:18px;position:relative;margin:0 0 4px}
.prose .ln::before{content:"";position:absolute;left:4px;top:.62em;width:4px;height:4px;border-radius:50%;background:var(--accent)}
.prose .ln .lb{display:block;font-weight:650;color:#0d2b33}
.prose .ln.note{padding-left:34px}.prose .ln.note::before{left:20px;background:#8aa8ac}
ul{padding-left:24px}
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


INLINE_RE = re.compile(r'(\*\*.+?\*\*|`[^`]+`)')


def inline(text):
    """Render the two inline markers that carry meaning in review prose.

    Everything else is escaped literal text. Deliberately narrow: no HTML pass-through,
    no headings, no images, no links. `**bold**` becomes <strong>, `` `code` `` becomes <code>.
    """
    parts = []
    for piece in INLINE_RE.split(text):
        if not piece:
            continue
        if piece.startswith('**') and piece.endswith('**') and len(piece) > 4:
            parts.append('<strong>'+txt(piece[2:-2])+'</strong>')
        elif piece.startswith('`') and piece.endswith('`') and len(piece) > 2:
            parts.append('<code>'+txt(piece[1:-1])+'</code>')
        else:
            parts.append(txt(piece))
    return ''.join(parts)


def prose(text):
    """Render an authored prose block as indented lines instead of one text wall.

    The author's own structure is respected: a newline starts a line, one leading bullet
    (`·`, `-`, `*`, `•`) marks a list line, and two leading full-width spaces mark a
    subordinate line. Emphasised lead-ins become block labels. No text is reworded here.
    """
    blocks = []
    if not isinstance(text, str):
        raise ValueError('Report prose must be a string')
    for raw in text.split('\n'):
        if not raw.strip():
            continue
        line = raw.rstrip()
        note = line.startswith('\u3000\u3000')
        line = line.lstrip('\u3000').lstrip()
        classes = 'ln'
        if note:
            classes += ' note'
        # Remove one explicit list marker, never a numeric sign or punctuation.
        line = re.sub(r'^[·•*-]\s+', '', line, count=1)
        match = re.match(r'^\*\*(.+?)\*\*[:\uff1a]?\s*(.*)$', line)
        if match:
            head, rest = match.group(1), match.group(2)
            inner = '<span class="lb">'+txt(head)+'</span>'+(' '+inline(rest) if rest else '')
        else:
            inner = inline(line)
        blocks.append('<span class="'+classes+'">'+inner+'</span>')
    return '<div class="prose">'+''.join(blocks)+'</div>'


def round_html(data, number):
    # Titles are authored labels, not prose: keep them as single-line escaped text.
    # The heading already carries the round number; a title repeating it renders as "Round 1 · Round 1 · …".
    title=data['title'].strip()
    if re.match(rf'^round\s*{number}\b', title, re.I):
        raise ValueError(f'Round {number} title must not repeat the "Round {number}" prefix')
    out = [f'<article id="round-{number}"><h2>Round {number} · '+txt(title)+'</h2>', '<p class="verdict">'+inline(data['verdict'])+'</p>']
    out.append(prose(data['summary']))
    for section in data.get('sections', []):
        out.append('<section><h3>'+txt(section['title'])+'</h3>')
        out.extend(prose(p) for p in section.get('paragraphs', []))
        if section.get('bullets'):
            out.append('<ul>'+''.join('<li>'+inline(p)+'</li>' for p in section['bullets'])+'</ul>')
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
            # Optional reasoned interval, printed beside the point score so an
            # uncertain number is legible without relying on font styling.
            cell=str(score)
            band=row.get('band')
            if band is not None:
                if type(score) is not int:
                    raise ValueError('A score band is only valid for numeric scores')
                match=BAND_RE.fullmatch(band) if isinstance(band,str) else None
                if not match or int(match.group(1)) > int(match.group(2)):
                    raise ValueError('Score band must be ascending whole numbers 1–5, e.g. "2–4"')
                if not int(match.group(1)) <= score <= int(match.group(2)):
                    raise ValueError('Score band must contain the point score')
                cell=cell+' ('+band.replace('-','\u2013')+')'
            rows.append([row['category'],cell,row['confidence'],row['evidence'],row['scope'],row['rationale']])
        out.append('<section><h3>'+txt(data.get('scorecard_title','Category scorecard'))+'</h3>')
        if data.get('scorecard_note'):
            out.append(prose(data['scorecard_note']))
        out.append(table(['Category','Score','Confidence','Evidence','Scope','Rationale'],rows)+'</section>')
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
