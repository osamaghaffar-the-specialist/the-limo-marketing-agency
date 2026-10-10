from pathlib import Path
import json
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')
old = '''      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/",
      "description": "Marketing and booking technology for limo, chauffeur, black car and airport transportation companies.",'''
new = '''      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#logo",
        "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/assets/brand-logo.png",
        "contentUrl": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/assets/brand-logo.png",
        "caption": "The Limo Marketing Agency"
      },
      "description": "Marketing and booking technology for limo, chauffeur, black car and airport transportation companies.",'''

count = text.count(old)
print('ORGANIZATION_TARGET_COUNT', count)
if count != 1:
    raise SystemExit(f'Expected exactly one Organization insertion target, found {count}')
text = text.replace(old, new, 1)
path.write_text(text, encoding='utf-8')

blocks = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, flags=re.I | re.S)
parsed = [json.loads(block.strip()) for block in blocks]
print('JSONLD_BLOCKS_PARSED', len(parsed))

org_id = 'https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#organization'
logo_url = 'https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/assets/brand-logo.png'
orgs = []
for doc in parsed:
    if not isinstance(doc, dict):
        continue
    for node in doc.get('@graph', []):
        if isinstance(node, dict) and node.get('@id') == org_id and node.get('@type') == 'Organization':
            orgs.append(node)
if len(orgs) != 1:
    raise SystemExit(f'Expected one Organization node, found {len(orgs)}')
logo = orgs[0].get('logo')
if not isinstance(logo, dict) or logo.get('url') != logo_url or logo.get('contentUrl') != logo_url:
    raise SystemExit('Organization logo schema validation failed')
if not Path('assets/brand-logo.png').is_file():
    raise SystemExit('Logo asset missing')
print('ORGANIZATION_LOGO_SCHEMA PASS')

empty_alt_tags = re.findall(r'<img\b[^>]*\balt=""[^>]*>', text, flags=re.I)
bad = [tag for tag in empty_alt_tags if not re.search(r'\baria-hidden="true"', tag, flags=re.I)]
print('EMPTY_ALT_IMG_COUNT', len(empty_alt_tags))
print('EMPTY_ALT_WITHOUT_ARIA_HIDDEN', len(bad))
if bad:
    raise SystemExit('Found an empty-alt image that is not aria-hidden')
