from pathlib import Path
import json
import re

ROOT = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/"
WEBSITE_ID = ROOT + "#website"
LD_RE = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)


def page_url_for(path: Path) -> str:
    return ROOT if path.name == "index.html" else ROOT + path.name


def is_webpage_type(node_type):
    if isinstance(node_type, str):
        return node_type == "WebPage" or node_type.endswith("Page")
    if isinstance(node_type, list):
        return any(isinstance(t, str) and (t == "WebPage" or t.endswith("Page")) for t in node_type)
    return False

changed_files = []
page_nodes_checked = 0

for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    original = text
    page_url = page_url_for(path)

    def repl(match):
        nonlocal_data = None
        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"ERROR: invalid JSON-LD in {path.name}: {exc}")

        graph = data.get('@graph', []) if isinstance(data, dict) else []
        if not isinstance(graph, list):
            return match.group(0)

        for node in graph:
            if not isinstance(node, dict) or not is_webpage_type(node.get('@type')):
                continue
            node['isPartOf'] = {'@id': WEBSITE_ID}
            node.setdefault('url', page_url)
            node.setdefault('inLanguage', 'en')

        return '<script type="application/ld+json">\n' + json.dumps(data, indent=2, ensure_ascii=False) + '\n</script>'

    text = LD_RE.sub(repl, text)
    if text != original:
        path.write_text(text, encoding='utf-8')
        changed_files.append(path.name)

# Strict validation across every JSON-LD page-like node.
errors = []
for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    expected_url = page_url_for(path)
    for match in LD_RE.finditer(text):
        data = json.loads(match.group(1))
        graph = data.get('@graph', []) if isinstance(data, dict) else []
        if not isinstance(graph, list):
            continue
        for node in graph:
            if not isinstance(node, dict) or not is_webpage_type(node.get('@type')):
                continue
            page_nodes_checked += 1
            if node.get('isPartOf') != {'@id': WEBSITE_ID}:
                errors.append(f"{path.name}: {node.get('@type')} isPartOf != WebSite")
            if not node.get('url'):
                errors.append(f"{path.name}: {node.get('@type')} missing url")
            if node.get('inLanguage') != 'en':
                errors.append(f"{path.name}: {node.get('@type')} missing/invalid inLanguage")

if errors:
    raise SystemExit('ERROR:\n' + '\n'.join(errors))

print('P0 webpage subclass normalization PASS')
print(f'Page-like schema nodes checked: {page_nodes_checked}')
print(f'Files changed: {len(changed_files)}')
for name in changed_files:
    print(f' - {name}')
