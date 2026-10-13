from pathlib import Path
import re

page = Path('index.html')
text = page.read_text(encoding='utf-8')
original = text

replacements = [
    (
        '                  Organic Traffic\n                </div>',
        '                  Organic Traffic · Illustrative\n                </div>',
    ),
    (
        '<div class="conversion-title">Conversions</div>',
        '<div class="conversion-title">Conversions · Illustrative</div>',
    ),
    (
        'Results vary by market, offer, competition, tracking and execution. Verified client outcomes are published only when supporting data is available.',
        'Illustrative dashboard metrics shown in this section are examples, not client KPIs. Results vary by market, offer, competition, tracking and execution. Verified client outcomes are published only when supporting data and permission are available.',
    ),
]

for old, new in replacements:
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'Expected exactly 1 occurrence for trust marker, found {count}: {old[:80]!r}')
    text = text.replace(old, new, 1)

# Diagnostic only: report image tags missing an alt attribute. Do not auto-fill them,
# because meaningful images need descriptive alt text rather than a fake empty pass.
missing = []
for match in re.finditer(r'<img\b[^>]*>', text, flags=re.I | re.S):
    tag = match.group(0)
    if not re.search(r'\balt\s*=', tag, flags=re.I):
        missing.append(' '.join(tag.split()))

print(f'MISSING_ALT_COUNT={len(missing)}')
for tag in missing:
    print('MISSING_ALT_TAG=' + tag)

if text == original:
    raise SystemExit('No homepage changes were made.')

page.write_text(text, encoding='utf-8')
print('Homepage trust disclosure updated successfully.')
