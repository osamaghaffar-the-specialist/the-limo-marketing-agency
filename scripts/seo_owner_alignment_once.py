from pathlib import Path


def replace_exact(path, old, new, expected=None):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if expected is not None and count != expected:
        raise SystemExit(f"{path}: expected {expected} occurrences, found {count}: {old[:90]}")
    if expected is None and count == 0:
        raise SystemExit(f"{path}: source text not found: {old[:90]}")
    p.write_text(text.replace(old, new), encoding="utf-8")
    print(f"{path}: replaced {count} occurrence(s)")


# Homepage: own broad commercial intent and strengthen internal anchors.
replace_exact(
    "index.html",
    "Grow your limo, chauffeur or black car company with Google Ads, SEO, GEO, conversion-focused websites and automated booking systems. Serving clients worldwide.",
    "The Limo Marketing Agency helps limo, chauffeur and black car companies grow with Google Ads, SEO, GEO, conversion-focused websites and booking systems.",
)
replace_exact(
    "index.html",
    "<h1>TURN YOUR LIMO BUSINESS INTO A DIGITAL GROWTH SYSTEM</h1>",
    "<h1>THE LIMO MARKETING AGENCY FOR GROWTH, BOOKINGS &amp; AUTOMATION</h1>",
    1,
)
replace_exact("index.html", "<h3>Limo SEO</h3>", "<h3>SEO for Limo Companies</h3>", 1)
replace_exact("index.html", "Explore Limo SEO Services", "Explore SEO for Limo Companies", 1)
replace_exact(
    "index.html",
    "<h3>Google Ads &amp; PPC Management</h3>",
    "<h3>Google Ads for Limo Companies</h3>",
    1,
)
replace_exact(
    "index.html",
    'href="google-ads-for-limo-companies.html">\n                Learn More',
    'href="google-ads-for-limo-companies.html">\n                Explore Google Ads for Limo Companies',
    1,
)
replace_exact(
    "index.html",
    "<h3>High-Conversion Web Design</h3>",
    "<h3>Limo Website Design</h3>",
    1,
)
replace_exact(
    "index.html",
    'href="limo-website-design.html">\n                Learn More',
    'href="limo-website-design.html">\n                Explore Limo Website Design',
    1,
)

# SEO owner page.
replace_exact(
    "seo-for-limo-companies.html",
    "Limo SEO services for limo, chauffeur and black car companies covering technical SEO, local search, content, internal linking and organic visibility.",
    "SEO for limo companies, chauffeur businesses and black car services covering technical SEO, local SEO, content architecture, internal linking and organic visibility.",
)
replace_exact(
    "seo-for-limo-companies.html",
    '"name": "Limo SEO Services for Limo Companies",',
    '"name": "SEO for Limo Companies",',
    1,
)
replace_exact(
    "seo-for-limo-companies.html",
    "<h1>Limo SEO Services That Get You Found When Customers Are <span>Already Searching.</span></h1>",
    "<h1>SEO for Limo Companies That Helps You Get Found When Customers Are <span>Already Searching.</span></h1>",
    1,
)
replace_exact(
    "seo-for-limo-companies.html",
    "Our limo SEO services build organic search visibility for limo, chauffeur, black car and airport transportation companies around the searches that can become calls, booking requests and paid rides, not traffic for traffic's sake.",
    "Our SEO for limo companies builds organic search visibility for limo, chauffeur, black car and airport transportation businesses around searches that can become calls, booking requests and paid rides, not traffic for traffic's sake.",
    1,
)

# Google Ads owner page.
replace_exact(
    "google-ads-for-limo-companies.html",
    "Limo Google Ads and PPC management focused on high-intent searches, qualified leads, conversion tracking and booked rides for limo and black car companies.",
    "Google Ads for limo companies and black car services focused on high-intent searches, qualified leads, conversion tracking, landing pages and booked rides.",
)
replace_exact(
    "google-ads-for-limo-companies.html",
    '"name": "Limo Google Ads and PPC Management",',
    '"name": "Google Ads for Limo Companies",',
    1,
)
replace_exact(
    "google-ads-for-limo-companies.html",
    '<h1 id="page-title">Limo Google Ads That Turn High-Intent Searches into <span>Booked Rides.</span></h1>',
    '<h1 id="page-title">Google Ads for Limo Companies That Turn High-Intent Searches into <span>Booked Rides.</span></h1>',
    1,
)
replace_exact(
    "google-ads-for-limo-companies.html",
    "Our limo Google Ads and PPC management is built specifically for limo companies, chauffeur companies, black car services and airport transportation businesses. We connect search intent, campaign structure, landing pages and conversion tracking so you can focus spend on the searches most likely to become real business.",
    "Our Google Ads management for limo companies is built specifically for limo, chauffeur, black car and airport transportation businesses. We connect search intent, campaign structure, landing pages and conversion tracking so you can focus spend on searches most likely to become real business.",
    1,
)

# Budget article: own informational budget intent, not the service query.
replace_exact(
    "how-much-should-limo-company-spend-google-ads-2026.html",
    "Limo Google Ads Budget Guide 2026 | TLMA",
    "How Much Should a Limo Company Spend on Google Ads? (2026)",
)
replace_exact(
    "how-much-should-limo-company-spend-google-ads-2026.html",
    '"dateModified": "2026-10-02",',
    '"dateModified": "2026-10-12",',
    1,
)
replace_exact(
    "how-much-should-limo-company-spend-google-ads-2026.html",
    ">Explore Google Ads Service</a>",
    ">Explore Google Ads for Limo Companies</a>",
    1,
)

Path("docs/seo-gsc-owner-alignment-2026-10-12.md").write_text(
    """# GSC Keyword-Owner Alignment Sprint — 2026-10-12

## Evidence window

Google Search Console data: 2026-09-12 through 2026-10-09 (latest settled date at analysis time).

## Indexed-page baseline

| Page | Impressions | Avg. position |
|---|---:|---:|
| Homepage `/` | 15 | 36.73 |
| `/booking-systems.html` | 1 | 8.00 |
| `/geo-ai-search-optimization.html` | 10 | 56.50 |
| `/google-ads-for-limo-companies.html` | 30 | 59.73 |
| `/how-much-should-limo-company-spend-google-ads-2026.html` | 9 | 37.67 |
| `/limo-website-design.html` | 11 | 64.09 |
| `/seo-for-limo-companies.html` | 35 | 71.69 |

All seven audited URLs were HTTP 200, indexable, self-canonical and had one H1. The sprint therefore targets search-intent ownership rather than broad technical rewrites.

## Cannibalization signals

- `limo seo`: homepage 7 impressions at avg. position 27.29 vs dedicated SEO page 5 impressions at 77.80.
- `seo limousine company`: homepage 1 impression at 19.00 vs dedicated SEO page 8 impressions at 70.25.
- `limo service google ads`: Google Ads service page 25 impressions at 68.72 vs budget article 5 impressions at 61.40.

## Changes

- Homepage H1 and description aligned to the broad `limo marketing agency` commercial intent.
- Homepage service cards strengthened with explicit internal anchor language for SEO, Google Ads and website-design owner URLs.
- SEO service page H1, intro, description and Service schema name aligned to `SEO for limo companies`.
- Google Ads service page H1, intro, description and Service schema name aligned to `Google Ads for limo companies`.
- Budget article title kept strictly informational and the related-service anchor strengthened; `dateModified` updated truthfully to 2026-10-12.
- Booking Systems, GEO/AI Search and Limo Website Design were not rewritten because current GSC evidence did not justify broader changes; the website-design page was already strongly aligned on-page.

## Guardrails

- No new production URLs.
- No sitemap, robots or canonical changes.
- No fake proof, rankings, testimonials or metrics.
- No paid links or memberships.
- Measure impact through GSC query-to-page ownership, impressions, average position, clicks and cannibalization after Google recrawls the changed URLs.
""",
    encoding="utf-8",
)

# Remove one-time automation artifacts before the resulting commit.
Path(".github/workflows/seo-gsc-owner-alignment.yml").unlink(missing_ok=True)
Path("scripts/seo_owner_alignment_once.py").unlink(missing_ok=True)
