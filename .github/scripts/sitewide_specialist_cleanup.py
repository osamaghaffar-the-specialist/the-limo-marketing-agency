from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
import html
import json
import re
import xml.etree.ElementTree as ET
from collections import defaultdict, deque

ROOT = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/"
ORG_ID = ROOT + "#organization"
LOGO_URL = ROOT + "assets/brand-logo.png"
EXPECTED_MISSING_LOGO = {
    "about.html",
    "airport-transportation-companies.html",
    "black-car-services.html",
    "case-studies-results.html",
    "chauffeur-companies.html",
    "how-much-should-limo-company-spend-google-ads-2026.html",
    "limousine-companies.html",
    "privacy-policy.html",
    "resources.html",
    "terms.html",
    "why-limo-google-ads-get-expensive.html",
}

META_UPDATES = {
    "chauffeur-companies.html": {
        "old_title": "Marketing for Chauffeur Companies | Executive Growth Strategy",
        "new_title": "Marketing for Chauffeur Companies | Growth Strategy",
        "old_desc": "Marketing for chauffeur companies focused on corporate, airport, executive and repeat-client demand using Google Ads, SEO, GEO, premium websites and booking systems.",
        "new_desc": "Marketing for chauffeur companies focused on corporate, airport and executive demand using Google Ads, SEO, GEO, premium websites and booking systems.",
    },
    "limousine-companies.html": {
        "old_title": "Marketing for Limousine Companies | Growth & Booking Strategy",
        "new_title": "Marketing for Limousine Companies | Growth Strategy",
        "old_desc": "Growth strategy for limousine companies across Google Ads, SEO, GEO, website design and booking systems, built around airport, corporate, hourly and event demand.",
        "new_desc": "Growth strategy for limousine companies using Google Ads, SEO, GEO, website design and booking systems across airport, corporate, hourly and event demand.",
    },
    "black-car-services.html": {
        "old_title": "Marketing for Black Car Services | Growth & Booking Strategy",
        "new_title": "Marketing for Black Car Services | Growth & Booking Strategy",
        "old_desc": "Marketing for black car services focused on airport, corporate, local and point-to-point demand using Google Ads, SEO, GEO, mobile-first websites and booking systems.",
        "new_desc": "Marketing for black car services focused on airport, corporate and point-to-point demand using Google Ads, SEO, GEO, mobile-first websites and booking systems.",
    },
}

jsonld_re = re.compile(r'(<script[^>]+type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)', re.I | re.S)
title_re = re.compile(r'(<title>)(.*?)(</title>)', re.I | re.S)
meta_desc_re = re.compile(r'(<meta(?=[^>]*\bname=["\']description["\'])[^>]*\bcontent=["\'])([^"\']*)(["\'][^>]*>)', re.I)
og_title_re = re.compile(r'(<meta(?=[^>]*\bproperty=["\']og:title["\'])[^>]*\bcontent=["\'])([^"\']*)(["\'][^>]*>)', re.I)
og_desc_re = re.compile(r'(<meta(?=[^>]*\bproperty=["\']og:description["\'])[^>]*\bcontent=["\'])([^"\']*)(["\'][^>]*>)', re.I)
canonical_re = re.compile(r'<link(?=[^>]*\brel=["\']canonical["\'])[^>]*\bhref=["\']([^"\']+)["\'][^>]*>', re.I)
h1_re = re.compile(r'<h1\b', re.I)

if not Path("assets/brand-logo.png").is_file():
    raise SystemExit("Verified brand logo asset is missing")

# Load exact sitemap file set.
root_xml = ET.parse("sitemap.xml").getroot()
ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [n.text.strip() for n in root_xml.findall("sm:url/sm:loc", ns)]
if len(urls) != 21:
    raise SystemExit(f"Expected 21 sitemap URLs, found {len(urls)}")

def url_to_file(url):
    if url == ROOT:
        return "index.html"
    if not url.startswith(ROOT):
        raise SystemExit(f"Off-property sitemap URL: {url}")
    return url[len(ROOT):]

files = [url_to_file(u) for u in urls]
for f in files:
    if not Path(f).is_file():
        raise SystemExit(f"Missing sitemap HTML file: {f}")

# 1) Add verified shared Organization logo only where genuinely missing.
missing_before = set()
changed_files = set()
for filename in files:
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    matches = list(jsonld_re.finditer(text))
    org_count = 0
    changed = False
    parts = []
    cursor = 0

    for m in matches:
        parts.append(text[cursor:m.start()])
        opening, raw, closing = m.group(1), m.group(2), m.group(3)
        doc = json.loads(raw.strip())
        if isinstance(doc, dict):
            nodes = doc.get("@graph", [])
            if not isinstance(nodes, list):
                nodes = []
            for node in nodes:
                if isinstance(node, dict) and node.get("@type") == "Organization" and node.get("@id") == ORG_ID:
                    org_count += 1
                    logo = node.get("logo")
                    logo_ok = (
                        isinstance(logo, dict)
                        and logo.get("@type") == "ImageObject"
                        and logo.get("@id") == ROOT + "#logo"
                        and logo.get("url") == LOGO_URL
                        and logo.get("contentUrl") == LOGO_URL
                    )
                    if not logo_ok:
                        missing_before.add(filename)
                        node["logo"] = {
                            "@type": "ImageObject",
                            "@id": ROOT + "#logo",
                            "url": LOGO_URL,
                            "contentUrl": LOGO_URL,
                            "caption": "The Limo Marketing Agency",
                        }
                        changed = True

            # 2) On resources hub, reference article entities instead of redeclaring incomplete Article nodes.
            if filename == "resources.html":
                for node in nodes:
                    if isinstance(node, dict) and node.get("@type") == "ItemList" and node.get("@id") == ROOT + "resources.html#guide-list":
                        elements = node.get("itemListElement", [])
                        if len(elements) != 2:
                            raise SystemExit("resources.html: expected exactly 2 guide ListItems")
                        for element in elements:
                            item = element.get("item") if isinstance(element, dict) else None
                            if not isinstance(item, dict) or item.get("@type") != "Article" or not item.get("@id") or not item.get("url") or not item.get("headline"):
                                raise SystemExit("resources.html: unexpected guide Article node shape")
                            element["item"] = {
                                "@id": item["@id"],
                                "url": item["url"],
                                "name": item["headline"],
                            }
                        changed = True

        rendered = "\n" + json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
        parts.append(opening + rendered + closing)
        cursor = m.end()
    parts.append(text[cursor:])

    if org_count != 1:
        raise SystemExit(f"{filename}: expected exactly one shared Organization node, found {org_count}")

    new_text = "".join(parts)
    if changed:
        path.write_text(new_text, encoding="utf-8")
        changed_files.add(filename)

if missing_before != EXPECTED_MISSING_LOGO:
    raise SystemExit(f"Unexpected missing-logo set. Found={sorted(missing_before)}")

# 3) Tighten the only remaining over-length industry metadata, preserving intent.
def replace_one(pattern, text, old, new, label, filename):
    matches = list(pattern.finditer(text))
    if len(matches) != 1:
        raise SystemExit(f"{filename}: expected one {label}, found {len(matches)}")
    current = html.unescape(matches[0].group(2))
    if current != old:
        raise SystemExit(f"{filename}: {label} source mismatch: {current!r}")
    return pattern.sub(lambda m: m.group(1) + new.replace('&', '&amp;') + m.group(3), text, count=1)

for filename, cfg in META_UPDATES.items():
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    text = replace_one(title_re, text, cfg["old_title"], cfg["new_title"], "title", filename)
    text = replace_one(og_title_re, text, cfg["old_title"], cfg["new_title"], "og:title", filename)
    text = replace_one(meta_desc_re, text, cfg["old_desc"], cfg["new_desc"], "meta description", filename)
    text = replace_one(og_desc_re, text, cfg["old_desc"], cfg["new_desc"], "og:description", filename)
    if len(cfg["new_title"]) > 60 or len(cfg["new_desc"]) > 160:
        raise SystemExit(f"{filename}: optimized metadata still over target")
    path.write_text(text, encoding="utf-8")
    changed_files.add(filename)
    print(f"META_PASS {filename} title={len(cfg['new_title'])} desc={len(cfg['new_desc'])}")

# 4) Re-parse every JSON-LD block and verify shared Organization logo on all 21 sitemap pages.
for filename in files:
    text = Path(filename).read_text(encoding="utf-8")
    orgs = []
    for m in jsonld_re.finditer(text):
        doc = json.loads(m.group(2).strip())
        if isinstance(doc, dict):
            for node in doc.get("@graph", []):
                if isinstance(node, dict) and node.get("@type") == "Organization" and node.get("@id") == ORG_ID:
                    orgs.append(node)
    if len(orgs) != 1:
        raise SystemExit(f"{filename}: final shared Organization count={len(orgs)}")
    logo = orgs[0].get("logo")
    if not isinstance(logo, dict) or logo.get("url") != LOGO_URL or logo.get("contentUrl") != LOGO_URL:
        raise SystemExit(f"{filename}: final Organization logo invalid")

# 5) Specialist crawl graph: broken local files, fragments, inbound links, and click depth.
class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if "id" in d:
            self.ids.add(d["id"])
        if tag == "a" and d.get("href"):
            self.hrefs.append(d["href"])

parsed = {}
for filename in files:
    p = LinkParser()
    p.feed(Path(filename).read_text(encoding="utf-8"))
    parsed[filename] = p

sitemap_set = set(files)
inbound = defaultdict(set)
adjacency = defaultdict(set)
broken_files = []
broken_fragments = []

def target_file(source_file, href):
    low = href.lower().strip()
    if low.startswith(("mailto:", "tel:", "javascript:", "data:")):
        return None, None
    absolute = urljoin(ROOT + ("" if source_file == "index.html" else source_file), href)
    u = urlparse(absolute)
    root_u = urlparse(ROOT)
    if u.netloc != root_u.netloc or not u.path.startswith(root_u.path):
        return None, None
    rel = u.path[len(root_u.path):]
    if rel in ("", "/"):
        rel = "index.html"
    rel = rel.lstrip("/")
    return rel, u.fragment or None

for source in files:
    for href in parsed[source].hrefs:
        target, frag = target_file(source, href)
        if not target:
            continue
        if not Path(target).is_file():
            broken_files.append((source, href, target))
            continue
        if frag and target.endswith(".html") and frag not in parsed.get(target, LinkParser()).ids:
            broken_fragments.append((source, href, target, frag))
        if target in sitemap_set and target != source:
            inbound[target].add(source)
            adjacency[source].add(target)

orphans = sorted(f for f in files if f != "index.html" and not inbound[f])
depth = {"index.html": 0}
q = deque(["index.html"])
while q:
    src = q.popleft()
    for tgt in adjacency[src]:
        if tgt not in depth:
            depth[tgt] = depth[src] + 1
            q.append(tgt)
unreachable = sorted(f for f in files if f not in depth)
max_depth = max(depth.values()) if depth else 0

# Canonical/H1 smoke test across every sitemap URL.
for url, filename in zip(urls, files):
    text = Path(filename).read_text(encoding="utf-8")
    canon = canonical_re.findall(text)
    if len(canon) != 1 or canon[0] != url:
        raise SystemExit(f"{filename}: canonical mismatch {canon}")
    if len(h1_re.findall(text)) != 1:
        raise SystemExit(f"{filename}: H1 count is not exactly 1")

print("ORG_LOGO_FIXED", len(missing_before), sorted(missing_before))
print("CHANGED_FILES", len(changed_files), sorted(changed_files))
print("BROKEN_LOCAL_FILES", len(broken_files), broken_files[:20])
print("BROKEN_FRAGMENTS", len(broken_fragments), broken_fragments[:20])
print("ORPHANS", len(orphans), orphans)
print("UNREACHABLE_FROM_HOME", len(unreachable), unreachable)
print("MAX_CLICK_DEPTH", max_depth)
for f in sorted(files, key=lambda x: (len(inbound[x]), x)):
    print("INBOUND", f, len(inbound[f]), "DEPTH", depth.get(f, "NA"))

if broken_files or broken_fragments or orphans or unreachable:
    raise SystemExit("Specialist link-integrity gate failed")
if max_depth > 3:
    raise SystemExit(f"Click depth too high: {max_depth}")

print("SITEWIDE_SPECIALIST_GATE PASS")
