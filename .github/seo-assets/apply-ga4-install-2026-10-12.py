from pathlib import Path

MEASUREMENT_ID = "G-DXCDK9ZELZ"
MARKER = "<!-- TLMA Google Analytics 4 -->"
TAG = f'''{MARKER}\n<script async src="https://www.googletagmanager.com/gtag/js?id={MEASUREMENT_ID}"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){{dataLayer.push(arguments);}}\n  gtag('js', new Date());\n  gtag('config', '{MEASUREMENT_ID}');\n</script>'''

# Only real top-level HTML documents. Google verification tokens can also end in
# .html but are plain-text files and must never be modified.
html_files = []
non_document_html = []
for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    if '<html' in text.lower() and '<head>' in text:
        html_files.append(path)
    else:
        non_document_html.append(path)

assert html_files, 'No real top-level HTML documents found'

changed = []
for path in html_files:
    text = path.read_text(encoding='utf-8')
    if MEASUREMENT_ID in text:
        continue
    text = text.replace('<head>', '<head>\n' + TAG, 1)
    path.write_text(text, encoding='utf-8')
    changed.append(str(path))

# Connect the success-only lead signal to gtag.js. Keep a dataLayer fallback
# for environments where the Google tag is blocked or unavailable.
thank_you = Path('thank-you.html')
text = thank_you.read_text(encoding='utf-8')
old = """  window.dataLayer.push({\n    event:'generate_lead',\n    lead_source:leadSource,\n    form_type:'consultation',\n    conversion_page:'thank-you'\n  });"""
new = """  const leadEventParams={\n    lead_source:leadSource,\n    form_type:'consultation',\n    conversion_page:'thank-you'\n  };\n\n  if(typeof window.gtag==='function'){\n    window.gtag('event','generate_lead',leadEventParams);\n  }else{\n    window.dataLayer.push(Object.assign({event:'generate_lead'},leadEventParams));\n  }"""
assert old in text, 'Expected generate_lead dataLayer block not found in thank-you.html'
text = text.replace(old, new, 1)
thank_you.write_text(text, encoding='utf-8')

# Validation
for path in html_files:
    text = path.read_text(encoding='utf-8')
    assert text.count(MEASUREMENT_ID) == 2, f'Expected exactly 2 Measurement ID references in {path}, got {text.count(MEASUREMENT_ID)}'
    assert text.count(MARKER) == 1, f'Expected one GA4 marker in {path}'

# Any .html file that is not an actual document (e.g. Search Console verification)
# must remain untouched by the analytics patch.
for path in non_document_html:
    text = path.read_text(encoding='utf-8')
    assert MEASUREMENT_ID not in text, f'GA4 unexpectedly added to non-document HTML file {path}'
    assert MARKER not in text, f'GA4 marker unexpectedly added to non-document HTML file {path}'

text = thank_you.read_text(encoding='utf-8')
assert "window.gtag('event','generate_lead',leadEventParams);" in text
assert '<meta content="noindex,follow" name="robots"/>' in text
params = text[text.find('const leadEventParams='):text.find("if(typeof window.gtag", text.find('const leadEventParams='))]
for pii in ['email:', 'phone:', 'name:', 'company:']:
    assert pii not in params, f'PII-like field found in lead event params: {pii}'

print(f'GA4 installed on {len(html_files)} real top-level HTML documents; newly changed tag files: {len(changed)}')
print(f'Excluded {len(non_document_html)} non-document .html verification/token file(s)')
print('Success-only generate_lead event wired to gtag.js on thank-you.html')
