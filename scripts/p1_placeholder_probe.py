from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
terms=re.compile(r'before launch|demo form|future email-capture|illustrative performance|replace with verified|connect this form|production crm',re.I)
for path in sorted(ROOT.glob('*.html')):
    text=path.read_text(encoding='utf-8',errors='replace')
    for m in terms.finditer(text):
        a=max(0,m.start()-260); b=min(len(text),m.end()+360)
        snippet=' '.join(text[a:b].split())
        print(f'PROBE|{path.name}|{m.group(0)}|{snippet}')
