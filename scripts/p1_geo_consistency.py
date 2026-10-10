from pathlib import Path

p = Path('geo-ai-search-optimization.html')
text = p.read_text(encoding='utf-8')
changes = [
    ('"name": "GEO and AI Search Optimization for Limo Companies",', '"name": "GEO, AEO and AI Search Optimization for Limo Companies",'),
    ('<div class="eyebrow"><span class="dot"></span>GEO / AI SEARCH OPTIMIZATION</div>', '<div class="eyebrow"><span class="dot"></span>GEO / AEO / AI SEARCH OPTIMIZATION</div>'),
]
for old, new in changes:
    if old not in text:
        raise SystemExit(f'MISSING:{old[:70]}')
    text = text.replace(old, new, 1)
p.write_text(text, encoding='utf-8')
print('GEO_CONSISTENCY_PASS')
