from pathlib import Path

ROOT = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/"
OLD_HOME = ROOT + "index.html"

changed_files = []
old_url_hits_before = 0
old_href_hits_before = 0

for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    old_url_hits_before += text.count(OLD_HOME)
    old_href_hits_before += text.count('href="index.html"') + text.count("href='index.html'")

    updated = text.replace(OLD_HOME, ROOT)
    updated = updated.replace('href="index.html"', 'href="./"')
    updated = updated.replace("href='index.html'", "href='./'")

    if updated != text:
        path.write_text(updated, encoding='utf-8')
        changed_files.append(path.name)

# Hard checks: preferred homepage must be root everywhere in technical signals.
remaining_old_urls = []
remaining_old_hrefs = []
for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if OLD_HOME in text:
        remaining_old_urls.append(path.name)
    if 'href="index.html"' in text or "href='index.html'" in text:
        remaining_old_hrefs.append(path.name)

index_text = Path('index.html').read_text(encoding='utf-8')
required_index_signals = [
    f'<link rel="canonical" href="{ROOT}"',
    f'<meta property="og:url" content="{ROOT}"',
    f'"@id": "{ROOT}#organization"',
    f'"@id": "{ROOT}#website"',
    f'"@id": "{ROOT}#webpage"',
    f'"url": "{ROOT}"',
]
missing = [signal for signal in required_index_signals if signal not in index_text]

sitemap = Path('sitemap.xml').read_text(encoding='utf-8')
if f'<loc>{ROOT}</loc>' not in sitemap:
    raise SystemExit('ERROR: clean root homepage missing from sitemap.xml')
if f'<loc>{OLD_HOME}</loc>' in sitemap:
    raise SystemExit('ERROR: /index.html still listed as sitemap homepage')
if remaining_old_urls:
    raise SystemExit(f'ERROR: old absolute homepage URL remains in: {remaining_old_urls}')
if remaining_old_hrefs:
    raise SystemExit(f'ERROR: relative index.html Home links remain in: {remaining_old_hrefs}')
if missing:
    raise SystemExit(f'ERROR: homepage is missing normalized technical signals: {missing}')

print('P0 homepage normalization PASS')
print(f'Absolute /index.html URL occurrences replaced: {old_url_hits_before}')
print(f'Relative Home href occurrences replaced: {old_href_hits_before}')
print(f'Files changed: {len(changed_files)}')
for name in changed_files:
    print(f' - {name}')
