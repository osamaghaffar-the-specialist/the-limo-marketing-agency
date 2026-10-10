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

if not Path("assets/brand-logo.png").is_file():
    raise SystemExit("Verified brand logo asset is missing")

pattern = re.compile(r'(<script[^>]+type=["\']application/ld\+json["\'][^>]*>)(.*?)(</script>)', re.I | re.S)
changed = []

for filename in FILES:
    path = Path(filename)
    text = path.read_text(encoding="utf-8")
    matches = list(pattern.finditer(text))
    if not matches:
        raise SystemExit(f"{filename}: no JSON-LD blocks found")

    found_org = 0
    changed_this_file = False
    rebuilt_parts = []
    cursor = 0

    for match in matches:
        rebuilt_parts.append(text[cursor:match.start()])
        opening, raw_json, closing = match.group(1), match.group(2), match.group(3)
        doc = json.loads(raw_json.strip())

        if isinstance(doc, dict):
            for node in doc.get("@graph", []):
                if isinstance(node, dict) and node.get("@type") == "Organization" and node.get("@id") == ORG_ID:
                    found_org += 1
                    logo = node.get("logo")
                    already_ok = (
                        node.get("url") == ROOT
                        and isinstance(logo, dict)
                        and logo.get("url") == LOGO_URL
                        and logo.get("contentUrl") == LOGO_URL
                    )
                    if not already_ok:
                        if node.get("url") not in (None, ROOT):
                            raise SystemExit(f"{filename}: unexpected Organization url {node.get('url')!r}")
                        node["url"] = ROOT
                        node["logo"] = {
                            "@type": "ImageObject",
                            "@id": ROOT + "#logo",
                            "url": LOGO_URL,
                            "contentUrl": LOGO_URL,
                            "caption": "The Limo Marketing Agency",
                        }
                        changed_this_file = True

        rendered = "\n" + json.dumps(doc, ensure_ascii=False, indent=2) + "\n"
        rebuilt_parts.append(opening + rendered + closing)
        cursor = match.end()

    rebuilt_parts.append(text[cursor:])

    if found_org != 1:
        raise SystemExit(f"{filename}: expected exactly one Organization node, found {found_org}")

    new_text = "".join(rebuilt_parts)
    if changed_this_file:
        path.write_text(new_text, encoding="utf-8")
        changed.append(filename)
        print(filename, "ORGANIZATION_LOGO_SCHEMA UPDATED")
    else:
        print(filename, "ALREADY_OK")

    # Validate the final JSON-LD and exact Organization relationship.
    final_blocks = pattern.findall(new_text)
    final_orgs = []
    for _open, raw, _close in final_blocks:
        doc = json.loads(raw.strip())
        if not isinstance(doc, dict):
            continue
        for node in doc.get("@graph", []):
            if isinstance(node, dict) and node.get("@type") == "Organization" and node.get("@id") == ORG_ID:
                final_orgs.append(node)
    if len(final_orgs) != 1:
        raise SystemExit(f"{filename}: final Organization validation failed")
    org = final_orgs[0]
    logo = org.get("logo")
    if org.get("url") != ROOT:
        raise SystemExit(f"{filename}: final Organization url validation failed")
    if not isinstance(logo, dict) or logo.get("url") != LOGO_URL or logo.get("contentUrl") != LOGO_URL:
        raise SystemExit(f"{filename}: final Organization logo validation failed")
    print(filename, "FINAL_VALIDATION PASS")

print("CHANGED_COUNT", len(changed))
print("CHANGED_FILES", ",".join(changed))
