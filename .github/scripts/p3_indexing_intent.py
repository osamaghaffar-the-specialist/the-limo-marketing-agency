from pathlib import Path
import datetime as dt
import re
import subprocess
import xml.etree.ElementTree as ET

ROOT = "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/"
INDEX = Path("index.html")
SITEMAP = Path("sitemap.xml")

# --- 1) Tighten homepage SEO intent without changing URL/title/canonical/H1 ---
text = INDEX.read_text(encoding="utf-8")
pattern = re.compile(
    r'(<article class="core-service-card reveal">\s*'
    r'<div class="core-service-icon core-service-logo-wrap"><img alt="SEO and GEO logo".*?</div>\s*)'
    r'<h3>SEO \+ GEO</h3>\s*'
    r'<p>\s*Improve organic, local Maps and AI-search visibility so your fleet is discovered across\s*'
    r'the full modern search journey\.\s*</p>\s*'
    r'(<a class="core-service-link" href="seo-for-limo-companies\.html">\s*)'
    r'Learn More',
    re.S,
)
replacement = (
    r'\1<h3>Limo SEO</h3>\n'
    r'<p>\n'
    r'                Improve organic and local search visibility around high-intent limo, chauffeur and black car searches\n'
    r'                that can become calls, quote requests and bookings.\n'
    r'              </p>\n'
    r'\2Explore Limo SEO Services'
)
new_text, count = pattern.subn(replacement, text, count=1)
if count != 1:
    raise SystemExit(f"Expected exactly one linked homepage SEO card match, found {count}")

# Guardrails: do not alter primary page signals in this step.
def one(pattern_text, source, flags=0):
    m = re.findall(pattern_text, source, flags)
    if len(m) != 1:
        raise SystemExit(f"Expected one match for {pattern_text!r}, found {len(m)}")
    return m[0]

for pat in [r'<title>.*?</title>', r'<link rel="canonical"[^>]*>', r'<h1\b[^>]*>.*?</h1>']:
    if one(pat, text, re.S) != one(pat, new_text, re.S):
        raise SystemExit(f"Protected homepage signal changed unexpectedly: {pat}")

if new_text.count('href="seo-for-limo-companies.html"') != text.count('href="seo-for-limo-companies.html"'):
    raise SystemExit("SEO target link count changed unexpectedly")
if "Explore Limo SEO Services" not in new_text:
    raise SystemExit("Descriptive SEO anchor was not written")
INDEX.write_text(new_text, encoding="utf-8")

# --- 2) Add accurate <lastmod> to every sitemap URL ---
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", NS)
tree = ET.parse(SITEMAP)
root = tree.getroot()
urls = root.findall(f"{{{NS}}}url")
if len(urls) != 21:
    raise SystemExit(f"Expected 21 sitemap URLs, found {len(urls)}")

locs_before = []
today = dt.datetime.now(dt.timezone.utc).date()

def loc_to_file(loc):
    if loc == ROOT:
        return "index.html"
    if not loc.startswith(ROOT):
        raise SystemExit(f"Off-property sitemap URL: {loc}")
    rel = loc[len(ROOT):]
    if not rel or "/" in rel.strip("/"):
        # Current sitemap is root-level only; fail instead of guessing nested mappings.
        raise SystemExit(f"Unexpected sitemap path shape: {loc}")
    return rel

def git_last_date(filename):
    out = subprocess.check_output(
        ["git", "log", "-1", "--format=%cs", "--", filename],
        text=True,
    ).strip()
    if not out:
        raise SystemExit(f"No git history found for {filename}")
    return dt.date.fromisoformat(out)

for url_node in urls:
    loc_node = url_node.find(f"{{{NS}}}loc")
    if loc_node is None or not (loc_node.text or "").strip():
        raise SystemExit("Sitemap URL missing loc")
    loc = loc_node.text.strip()
    locs_before.append(loc)
    filename = loc_to_file(loc)
    if not Path(filename).is_file():
        raise SystemExit(f"Sitemap target file missing: {filename}")

    # index.html is modified in this run, so its truthful lastmod is today.
    last_date = today if filename == "index.html" else git_last_date(filename)
    if last_date > today:
        raise SystemExit(f"Future lastmod for {filename}: {last_date}")

    lastmod_node = url_node.find(f"{{{NS}}}lastmod")
    if lastmod_node is None:
        lastmod_node = ET.SubElement(url_node, f"{{{NS}}}lastmod")
    lastmod_node.text = last_date.isoformat()

ET.indent(tree, space="  ")
tree.write(SITEMAP, encoding="utf-8", xml_declaration=True)
with SITEMAP.open("a", encoding="utf-8") as fh:
    fh.write("\n")

# Re-parse and verify URL set/order unchanged and every lastmod is present/valid.
check = ET.parse(SITEMAP).getroot()
urls_after = check.findall(f"{{{NS}}}url")
locs_after = []
for url_node in urls_after:
    loc = url_node.find(f"{{{NS}}}loc").text.strip()
    lm = url_node.find(f"{{{NS}}}lastmod")
    if lm is None or not (lm.text or "").strip():
        raise SystemExit(f"Missing lastmod after write: {loc}")
    dt.date.fromisoformat(lm.text.strip())
    locs_after.append(loc)
if locs_after != locs_before:
    raise SystemExit("Sitemap URL order/set changed unexpectedly")

print("P3_INDEXING_INTENT_PASS")
print("SITEMAP_URLS", len(locs_after))
print("HOMEPAGE_SEO_ANCHOR", "Explore Limo SEO Services")
print("HOMEPAGE_TARGET", ROOT + "seo-for-limo-companies.html")
