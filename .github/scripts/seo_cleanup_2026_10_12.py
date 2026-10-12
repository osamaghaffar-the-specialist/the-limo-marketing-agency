from pathlib import Path
import json
import re

PRODUCTION_FILES = [
    "index.html",
    "booking-systems.html",
    "geo-ai-search-optimization.html",
    "google-ads-for-limo-companies.html",
    "limo-website-design.html",
    "seo-for-limo-companies.html",
    "how-much-should-limo-company-spend-google-ads-2026.html",
    "about.html",
    "industries.html",
    "limousine-companies.html",
    "resources.html",
    "why-limo-google-ads-get-expensive.html",
    "social-media-marketing-for-limo-companies.html",
    "black-car-services.html",
    "chauffeur-companies.html",
    "case-studies-results.html",
    "contact.html",
    "privacy-policy.html",
    "terms.html",
    "airport-transportation-companies.html",
    "services.html",
]

FAVICON = '<link rel="icon" type="image/png" href="assets/brand-logo.png"/>'
VIEWPORT_RE = re.compile(r'(<meta\b[^>]*\bname=["\']viewport["\'][^>]*?/?>\s*)', re.I)

for filename in PRODUCTION_FILES:
    path = Path(filename)
    if not path.exists():
        raise SystemExit(f"Missing production file: {filename}")
    text = path.read_text(encoding="utf-8")
    if 'rel="icon"' not in text and "rel='icon'" not in text:
        text, count = VIEWPORT_RE.subn(lambda m: m.group(1) + FAVICON + "\n", text, count=1)
        if count != 1:
            raise SystemExit(f"Could not insert favicon exactly once in {filename}: {count}")
        path.write_text(text, encoding="utf-8")

seo_path = Path("seo-for-limo-companies.html")
seo_text = seo_path.read_text(encoding="utf-8")
old_desc = "SEO for limo companies, chauffeur businesses and black car services covering technical SEO, local SEO, content architecture, internal linking and organic visibility."
new_desc = "SEO for limo companies, chauffeur and black car businesses covering technical SEO, local SEO, content architecture, internal linking and organic visibility."
if seo_text.count(old_desc) != 2:
    raise SystemExit(f"Expected SEO description twice (meta + OG), found {seo_text.count(old_desc)}")
seo_text = seo_text.replace(old_desc, new_desc)
seo_path.write_text(seo_text, encoding="utf-8")

logo_id = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#logo"

budget_path = Path("how-much-should-limo-company-spend-google-ads-2026.html")
budget_text = budget_path.read_text(encoding="utf-8")
budget_old = '      "description": "A practical Google Ads budgeting guide for limo, chauffeur and black car companies.",\n      "datePublished": "2026-10-02",'
budget_new = f'      "description": "A practical Google Ads budgeting guide for limo, chauffeur and black car companies.",\n      "image": {{\n        "@id": "{logo_id}"\n      }},\n      "datePublished": "2026-10-02",'
if budget_text.count(budget_old) != 1:
    raise SystemExit(f"Budget Article schema anchor mismatch: {budget_text.count(budget_old)}")
budget_text = budget_text.replace(budget_old, budget_new, 1)
budget_path.write_text(budget_text, encoding="utf-8")

expensive_path = Path("why-limo-google-ads-get-expensive.html")
expensive_text = expensive_path.read_text(encoding="utf-8")
expensive_old = '      "description": "A practical diagnostic guide for limousine and black car companies dealing with expensive Google Ads leads.",\n      "author": {'
expensive_new = f'      "description": "A practical diagnostic guide for limousine and black car companies dealing with expensive Google Ads leads.",\n      "image": {{\n        "@id": "{logo_id}"\n      }},\n      "datePublished": "2026-09-25",\n      "dateModified": "2026-10-12",\n      "author": {{'
if expensive_text.count(expensive_old) != 1:
    raise SystemExit(f"Expensive Article schema anchor mismatch: {expensive_text.count(expensive_old)}")
expensive_text = expensive_text.replace(expensive_old, expensive_new, 1)
expensive_path.write_text(expensive_text, encoding="utf-8")

# Validation: one favicon per production page.
for filename in PRODUCTION_FILES:
    text = Path(filename).read_text(encoding="utf-8")
    if text.count(FAVICON) != 1:
        raise SystemExit(f"Favicon validation failed for {filename}: {text.count(FAVICON)}")

# Validation: SEO description remains below 160 characters.
if len(new_desc) >= 160:
    raise SystemExit(f"SEO description too long: {len(new_desc)}")

# Validation: every JSON-LD block touched remains valid JSON.
for filename in ["seo-for-limo-companies.html", "how-much-should-limo-company-spend-google-ads-2026.html", "why-limo-google-ads-get-expensive.html"]:
    text = Path(filename).read_text(encoding="utf-8")
    blocks = re.findall(r'<script\s+type="application/ld\+json">\s*(.*?)\s*</script>', text, flags=re.S | re.I)
    if not blocks:
        raise SystemExit(f"No JSON-LD found in {filename}")
    for block in blocks:
        json.loads(block)

# Validation: Article fields are present.
for filename in ["how-much-should-limo-company-spend-google-ads-2026.html", "why-limo-google-ads-get-expensive.html"]:
    text = Path(filename).read_text(encoding="utf-8")
    blocks = re.findall(r'<script\s+type="application/ld\+json">\s*(.*?)\s*</script>', text, flags=re.S | re.I)
    graph = json.loads(blocks[0]).get("@graph", [])
    articles = [node for node in graph if node.get("@type") == "Article"]
    if len(articles) != 1:
        raise SystemExit(f"Expected one Article node in {filename}, got {len(articles)}")
    article = articles[0]
    for field in ["image", "datePublished"]:
        if not article.get(field):
            raise SystemExit(f"Missing {field} in {filename}")

print("SEO cleanup validation PASS")
print(f"Production pages with favicon: {len(PRODUCTION_FILES)}")
print(f"SEO meta description length: {len(new_desc)}")
