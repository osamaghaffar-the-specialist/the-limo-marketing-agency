from pathlib import Path
import json
import re

PAGE = Path('uk/taxi-dispatch-system-prices/index.html')
RESOURCES = Path('resources.html')
SITEMAP = Path('sitemap.xml')
URL = 'https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/uk/taxi-dispatch-system-prices/'


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected exactly 1 match, found {count}')
    return text.replace(old, new, 1)

# --- Release page ---
text = PAGE.read_text(encoding='utf-8')
text = replace_once(
    text,
    '<meta name="robots" content="noindex,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"/>',
    '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"/>',
    'robots release',
)

if 'G-DXCDK9ZELZ' not in text:
    ga4 = '''<!-- TLMA Google Analytics 4 -->\n<script async src="https://www.googletagmanager.com/gtag/js?id=G-DXCDK9ZELZ"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag('js', new Date());\n  gtag('config', 'G-DXCDK9ZELZ');\n</script>\n'''
    text = replace_once(text, '<head>\n', '<head>\n' + ga4, 'GA4 insertion')

if 'rel="icon"' not in text:
    text = replace_once(
        text,
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n',
        '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n<link rel="icon" type="image/png" href="../../assets/brand-logo.png"/>\n',
        'favicon insertion',
    )

text, n = re.subn(r'\.pre-release\{[^}]*\}', '', text, count=1)
if n != 1:
    raise SystemExit(f'pre-release style: expected 1 match, found {n}')
text = replace_once(
    text,
    '<div class="pre-release">Pre-release build: this page is intentionally noindex until TLMA\'s indexing expansion gate is passed.</div>\n',
    '',
    'pre-release banner',
)
text = text.replace('checked on 12 October 2026', 'checked on 14 October 2026')
text = text.replace('<strong>Last research check:</strong> 12 October 2026.', '<strong>Last research check:</strong> 14 October 2026.')
text = text.replace(
    '<li>Before this page is released from pre-production, every price source must be re-opened and checked again.</li>',
    '<li>Published price sources are re-opened and re-checked before material pricing updates are made to this guide.</li>',
)

if 'noindex' in re.sub(r'<!--.*?-->', '', text, flags=re.S).lower():
    raise SystemExit('Release page still contains noindex after patch')
if 'Pre-release build:' in text:
    raise SystemExit('Release banner still present after patch')
PAGE.write_text(text, encoding='utf-8')

# --- Resources hub: add one discoverable editorial link and keep ItemList schema aligned ---
rtext = RESOURCES.read_text(encoding='utf-8')
if URL not in rtext:
    card = '''\n<article class="article-card reveal"><span class="article-type">UK TAXI TECHNOLOGY</span><h3>Taxi Dispatch System Prices UK (2026): Real Costs Compared</h3><p>Compare published UK taxi dispatch pricing models, entry prices and common extras using vendor and authorised-reseller sources.</p><div class="article-meta"><span>Pricing Guide</span><span>Updated Oct 2026</span></div><a href="uk/taxi-dispatch-system-prices/">Compare UK Dispatch Prices →</a></article>'''
    exact_grid_start = '<div class="article-grid">\n<article class="article-card reveal"><span class="article-type">GOOGLE ADS</span>'
    replacement = '<div class="article-grid">' + card + '\n<article class="article-card reveal"><span class="article-type">GOOGLE ADS</span>'
    rtext = replace_once(rtext, exact_grid_start, replacement, 'resources strategic-articles grid')

    match = re.search(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', rtext, flags=re.S)
    if not match:
        raise SystemExit('Resources JSON-LD block not found')
    data = json.loads(match.group(2))
    item_list = None
    for node in data.get('@graph', []):
        if node.get('@type') == 'ItemList' and str(node.get('@id', '')).endswith('#guide-list'):
            item_list = node
            break
    if item_list is None:
        raise SystemExit('Resources ItemList schema not found')
    items = item_list.setdefault('itemListElement', [])
    if not any(URL in json.dumps(item) for item in items):
        items.append({
            '@type': 'ListItem',
            'position': len(items) + 1,
            'item': {
                '@id': URL + '#webpage',
                'url': URL,
                'name': 'Taxi Dispatch System Prices UK (2026): Real Costs Compared',
            },
        })
    for idx, item in enumerate(items, start=1):
        item['position'] = idx
    item_list['numberOfItems'] = len(items)
    new_json = json.dumps(data, indent=2, ensure_ascii=False)
    rtext = rtext[:match.start(2)] + new_json + rtext[match.end(2):]
    RESOURCES.write_text(rtext, encoding='utf-8')

# --- Sitemap: add release URL and update Resources lastmod because it changed ---
sxml = SITEMAP.read_text(encoding='utf-8')
resources_entry_old = '''  <url>\n    <loc>https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html</loc>\n    <lastmod>2026-10-10</lastmod>\n  </url>'''
resources_entry_new = '''  <url>\n    <loc>https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html</loc>\n    <lastmod>2026-10-14</lastmod>\n  </url>'''
if resources_entry_old in sxml:
    sxml = sxml.replace(resources_entry_old, resources_entry_new, 1)
elif resources_entry_new not in sxml:
    raise SystemExit('Resources sitemap entry not in expected state')

if URL not in sxml:
    new_url = f'''  <url>\n    <loc>{URL}</loc>\n    <lastmod>2026-10-14</lastmod>\n  </url>\n'''
    sxml = replace_once(sxml, '</urlset>', new_url + '</urlset>', 'sitemap insertion')
SITEMAP.write_text(sxml, encoding='utf-8')

print('UK taxi pricing release patch complete')
print('PAGE_ROBOTS_INDEX=' + str('content="index,follow' in PAGE.read_text(encoding='utf-8')))
print('PAGE_GA4=' + str('G-DXCDK9ZELZ' in PAGE.read_text(encoding='utf-8')))
print('PAGE_FAVICON=' + str('rel="icon"' in PAGE.read_text(encoding='utf-8')))
print('RESOURCE_LINK=' + str(URL in RESOURCES.read_text(encoding='utf-8')))
print('SITEMAP_LINK=' + str(URL in SITEMAP.read_text(encoding='utf-8')))
