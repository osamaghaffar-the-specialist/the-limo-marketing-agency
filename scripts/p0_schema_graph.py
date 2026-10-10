from pathlib import Path
import json
import re

ROOT = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/"
ORG_ID = ROOT + "#organization"
WEBSITE_ID = ROOT + "#website"
LD_RE = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)

WEBSITE_NODE = {
    "@type": "WebSite",
    "@id": WEBSITE_ID,
    "url": ROOT,
    "name": "The Limo Marketing Agency",
    "publisher": {"@id": ORG_ID},
    "inLanguage": "en"
}


def page_url_for(path: Path) -> str:
    return ROOT if path.name == "index.html" else ROOT + path.name


def normalize_item_url(value):
    if not isinstance(value, str):
        return value
    value = value.strip()
    if value.startswith("https://") or value.startswith("http://"):
        return value
    if value in ("", ".", "./", "index.html", "/"):
        return ROOT
    return ROOT + value.lstrip("./")


def normalize_graph(data, page_url):
    if not isinstance(data, dict) or not isinstance(data.get("@graph"), list):
        return data, False

    graph = data["@graph"]
    changed = False
    has_tlma_org = False

    for node in graph:
        if not isinstance(node, dict):
            continue
        node_type = node.get("@type")
        if node_type == "Organization" and node.get("name") == "The Limo Marketing Agency":
            has_tlma_org = True
            if node.get("@id") != ORG_ID:
                node["@id"] = ORG_ID; changed = True
            if node.get("url") != ROOT:
                node["url"] = ROOT; changed = True

    if has_tlma_org and not any(isinstance(n, dict) and n.get("@id") == WEBSITE_ID for n in graph):
        org_index = next((i for i, n in enumerate(graph) if isinstance(n, dict) and n.get("@id") == ORG_ID), 0)
        graph.insert(org_index + 1, dict(WEBSITE_NODE))
        changed = True

    for node in graph:
        if not isinstance(node, dict):
            continue
        node_type = node.get("@type")

        if node_type == "WebSite" and node.get("@id") == WEBSITE_ID:
            expected = dict(WEBSITE_NODE)
            for key, value in expected.items():
                if node.get(key) != value:
                    node[key] = value; changed = True

        if node_type == "Service":
            expected_provider = {"@id": ORG_ID}
            if node.get("provider") != expected_provider:
                node["provider"] = expected_provider; changed = True

        if node_type == "WebPage":
            expected_part = {"@id": WEBSITE_ID}
            if node.get("isPartOf") != expected_part:
                node["isPartOf"] = expected_part; changed = True
            if not node.get("url"):
                node["url"] = page_url; changed = True
            if not node.get("inLanguage"):
                node["inLanguage"] = "en"; changed = True

        if node_type == "BreadcrumbList":
            for item in node.get("itemListElement", []):
                if not isinstance(item, dict) or "item" not in item:
                    continue
                old = item["item"]
                new = normalize_item_url(old)
                if new != old:
                    item["item"] = new; changed = True
                if item.get("position") == 1 and item.get("name", "").lower() == "home" and item.get("item") != ROOT:
                    item["item"] = ROOT; changed = True

    return data, changed


def booking_schema():
    page_url = ROOT + "booking-systems.html"
    return {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": ORG_ID,
                "name": "The Limo Marketing Agency",
                "url": ROOT,
                "description": "A specialized growth and technology agency serving limo companies, chauffeur companies, black car services and airport transportation companies with Google Ads, SEO, GEO, website development, booking automation and social media marketing.",
                "areaServed": ["United States", "Canada", "United Kingdom", "Worldwide"]
            },
            dict(WEBSITE_NODE),
            {
                "@type": "Service",
                "@id": page_url + "#service",
                "name": "Limo Booking System and Automation",
                "serviceType": "Booking system and booking automation for limo, chauffeur and black car companies",
                "provider": {"@id": ORG_ID},
                "audience": {
                    "@type": "BusinessAudience",
                    "audienceType": "Limo companies, chauffeur companies, black car services and airport transportation companies"
                },
                "description": "Automated limo booking systems with live pricing, card payments, booking confirmation and connected admin operations for limo and black-car companies.",
                "areaServed": ["United States", "Canada", "United Kingdom", "Worldwide"]
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Home", "item": ROOT},
                    {"@type": "ListItem", "position": 2, "name": "Services", "item": ROOT + "services.html"},
                    {"@type": "ListItem", "position": 3, "name": "Limo Booking System & Automation", "item": page_url}
                ]
            },
            {
                "@type": "WebPage",
                "@id": page_url + "#webpage",
                "url": page_url,
                "name": "Limo Booking System & Automation",
                "isPartOf": {"@id": WEBSITE_ID},
                "about": {"@id": page_url + "#service"},
                "description": "Automated limo booking systems with live pricing, card payments, booking confirmation and connected admin operations for limo and black-car companies.",
                "inLanguage": "en"
            }
        ]
    }


changed_files = []
parsed_scripts = 0

for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    original = text
    page_url = page_url_for(path)

    if path.name == "booking-systems.html":
        text = text.replace('&amp;amp;', '&amp;')
        if '<meta property="og:url"' not in text:
            anchor = '<meta property="og:description" content="Automated limo booking systems with live pricing, card payments, booking confirmation and connected admin operations for limo and black-car companies."/>'
            text = text.replace(anchor, anchor + f'\n<meta property="og:url" content="{page_url}"/>', 1)
        if not LD_RE.search(text):
            block = '<script type="application/ld+json">\n' + json.dumps(booking_schema(), indent=2, ensure_ascii=False) + '\n</script>\n'
            text = text.replace('<style>', block + '<style>', 1)

    def repl(match):
        nonlocal_placeholder = None
        raw = match.group(1)
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SystemExit(f'ERROR: invalid JSON-LD in {path.name}: {exc}')
        normalized, _ = normalize_graph(data, page_url)
        return '<script type="application/ld+json">\n' + json.dumps(normalized, indent=2, ensure_ascii=False) + '\n</script>'

    matches = list(LD_RE.finditer(text))
    parsed_scripts += len(matches)
    if matches:
        text = LD_RE.sub(repl, text)

    if text != original:
        path.write_text(text, encoding='utf-8')
        changed_files.append(path.name)

# Validation pass
errors = []
for path in sorted(Path('.').glob('*.html')):
    text = path.read_text(encoding='utf-8')
    page_url = page_url_for(path)
    for match in LD_RE.finditer(text):
        data = json.loads(match.group(1))
        graph = data.get('@graph', []) if isinstance(data, dict) else []
        for node in graph:
            if not isinstance(node, dict):
                continue
            if node.get('@type') == 'WebPage':
                if node.get('isPartOf') != {'@id': WEBSITE_ID}:
                    errors.append(f'{path.name}: WebPage isPartOf is not WebSite')
            if node.get('@type') == 'Service':
                if node.get('provider') != {'@id': ORG_ID}:
                    errors.append(f'{path.name}: Service provider is not Organization')
            if node.get('@type') == 'BreadcrumbList':
                for item in node.get('itemListElement', []):
                    value = item.get('item') if isinstance(item, dict) else None
                    if isinstance(value, str) and not value.startswith(('https://', 'http://')):
                        errors.append(f'{path.name}: non-absolute breadcrumb item {value}')

booking = Path('booking-systems.html').read_text(encoding='utf-8')
if '<meta property="og:url" content="' + ROOT + 'booking-systems.html"/>' not in booking:
    errors.append('booking-systems.html: missing og:url')
if not LD_RE.search(booking):
    errors.append('booking-systems.html: missing JSON-LD')
if '&amp;amp;' in booking:
    errors.append('booking-systems.html: double-encoded ampersand remains')

if errors:
    raise SystemExit('ERROR:\n' + '\n'.join(errors))

print('P0 schema graph normalization PASS')
print(f'JSON-LD scripts parsed: {parsed_scripts}')
print(f'Files changed: {len(changed_files)}')
for name in changed_files:
    print(f' - {name}')
