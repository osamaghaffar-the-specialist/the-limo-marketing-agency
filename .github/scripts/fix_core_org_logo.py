from pathlib import Path
import json
import re

ROOT = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/"
ORG_ID = ROOT + "#organization"
LOGO_URL = ROOT + "assets/brand-logo.png"
FILES = [
    "services.html",
    "industries.html",
    "seo-for-limo-companies.html",
    "google-ads-for-limo-companies.html",
    "geo-ai-search-optimization.html",
    "limo-website-design.html",
    "booking-systems.html",
    "social-media-marketing-for-limo-companies.html",
    "contact.html",
]

marker = (
    '      "@type": "Organization",\n'
    f'      "@id": "{ORG_ID}",\n'
    '      "name": "The Limo Marketing Agency",\n'
    f'      "url": "{ROOT}",'
)
logo_block = (
    f'{marker}\n'
    '      "logo": {\n'
    '        "@type": "ImageObject",\n'
    f'        "@id": "{ROOT}#logo",\n'
    f'        "url": "{LOGO_URL}",\n'
    f'        "contentUrl": "{LOGO_URL}",\n'
    '        "caption": "The Limo Marketing Agency"\n'
    '      },'
)

if not Path("assets/brand-logo.png").is_file():
    raise SystemExit("Verified brand logo asset is missing")

changed = []
for filename in FILES:
    path = Path(filename)
    text = path.read_text(encoding="utf-8")

    # Skip safely if this page already has the exact Organization logo relation.
    blocks = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, flags=re.I | re.S)
    parsed = [json.loads(block.strip()) for block in blocks]
    orgs = []
    for doc in parsed:
        if not isinstance(doc, dict):
            continue
        for node in doc.get("@graph", []):
            if isinstance(node, dict) and node.get("@type") == "Organization" and node.get("@id") == ORG_ID:
                orgs.append(node)
    if len(orgs) != 1:
        raise SystemExit(f"{filename}: expected exactly one Organization node, found {len(orgs)}")

    existing_logo = orgs[0].get("logo")
    if isinstance(existing_logo, dict) and existing_logo.get("url") == LOGO_URL and existing_logo.get("contentUrl") == LOGO_URL:
        print(filename, "ALREADY_OK")
        continue

    count = text.count(marker)
    print(filename, "INSERTION_TARGET_COUNT", count)
    if count != 1:
        raise SystemExit(f"{filename}: expected one insertion target, found {count}")

    text = text.replace(marker, logo_block, 1)
    path.write_text(text, encoding="utf-8")

    # Re-parse after edit and verify the exact node.
    blocks2 = re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, flags=re.I | re.S)
    parsed2 = [json.loads(block.strip()) for block in blocks2]
    orgs2 = []
    for doc in parsed2:
        if not isinstance(doc, dict):
            continue
        for node in doc.get("@graph", []):
            if isinstance(node, dict) and node.get("@type") == "Organization" and node.get("@id") == ORG_ID:
                orgs2.append(node)
    if len(orgs2) != 1:
        raise SystemExit(f"{filename}: post-edit Organization validation failed")
    logo = orgs2[0].get("logo")
    if not isinstance(logo, dict) or logo.get("url") != LOGO_URL or logo.get("contentUrl") != LOGO_URL:
        raise SystemExit(f"{filename}: post-edit logo validation failed")
    changed.append(filename)
    print(filename, "ORGANIZATION_LOGO_SCHEMA PASS")

print("CHANGED_COUNT", len(changed))
print("CHANGED_FILES", ",".join(changed))
