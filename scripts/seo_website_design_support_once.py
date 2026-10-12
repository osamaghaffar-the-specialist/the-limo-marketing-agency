from pathlib import Path


def replace_exact(path, old, new, expected=1):
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    count = text.count(old)
    if count != expected:
        raise SystemExit(f"{path}: expected {expected} occurrence(s), found {count}: {old[:100]}")
    p.write_text(text.replace(old, new), encoding="utf-8")
    print(f"{path}: replaced {count} occurrence(s)")

replace_exact(
    "limo-website-design.html",
    "<title>Limo Website Design | Limousine Website Design</title>",
    "<title>Limo Website Design Services | Limousine Web Design</title>",
)
replace_exact(
    "limo-website-design.html",
    '<meta property="og:title" content="Limo Website Design | Limousine Website Design"/>',
    '<meta property="og:title" content="Limo Website Design Services | Limousine Web Design"/>',
)
replace_exact(
    "limo-website-design.html",
    '"name": "Limo and Limousine Website Design Services",',
    '"name": "Limo Website Design Services",',
)

replace_exact(
    "booking-systems.html",
    "<div class=\"section-head reveal\"><div><div class=\"kicker\"><span class=\"dot\"></span>The 2026 Booking Standard</div><h2>The Technology Changed. <span>Customer Expectations Changed with It.</span></h2></div><p>Premium chauffeur customers are already familiar with digital-first booking journeys. The opportunity for independent limo companies is to offer the same kind of speed and clarity while keeping their own fleet, pricing rules and brand experience.</p></div>",
    "<div class=\"section-head reveal\"><div><div class=\"kicker\"><span class=\"dot\"></span>The 2026 Booking Standard</div><h2>The Technology Changed. <span>Customer Expectations Changed with It.</span></h2></div><p>Premium chauffeur customers are already familiar with digital-first booking journeys. The opportunity for independent limo companies is to offer the same kind of speed and clarity while keeping their own fleet, pricing rules and brand experience. If the customer-facing site also needs rebuilding, our <a href=\"limo-website-design.html\" style=\"color:var(--blue);font-weight:850\">Limo Website Design</a> service connects the front end to the booking flow.</p></div>",
)

replace_exact(
    "geo-ai-search-optimization.html",
    "<div class=\"section-head\"><div><div class=\"kicker\"><span class=\"dot\"></span>CONNECTED GROWTH</div><h2>GEO Works Better When SEO, Paid Search and Booking Technology <span>Support the Same Journey.</span></h2></div><p>AI visibility is one discovery channel. The website still needs organic strength, paid demand capture and a strong way for visitors to book or contact the business.</p></div>",
    "<div class=\"section-head\"><div><div class=\"kicker\"><span class=\"dot\"></span>CONNECTED GROWTH</div><h2>GEO Works Better When SEO, Paid Search and Booking Technology <span>Support the Same Journey.</span></h2></div><p>AI visibility is one discovery channel. Strong <a href=\"limo-website-design.html\" style=\"color:var(--blue);font-weight:850\">limo website design</a> still matters because the site needs organic strength, paid demand capture and a clear way for visitors to book or contact the business.</p></div>",
)

Path("docs/seo-website-design-owner-support-2026-10-12.md").write_text(
    """# Limo Website Design Owner Support Sprint — 2026-10-12

## Evidence

Google Search Console settled through 2026-10-09.

- `/limo-website-design.html`: 11 impressions, average position 64.09, 0 clicks.
- Query `limo company website design services`: 2 impressions, average position 80.
- Query `limo website design`: 3 impressions, average position 83.33.
- Additional template-related impressions exist, but the production page is a custom service page and is not being repositioned toward template intent.
- Live technical audit: HTTP 200, indexable, self-canonical, one H1, structured data present, no on-page audit issues.

## SERP intent check

Current results emphasize industry-specific website services, booking conversion, mobile usability, SEO architecture and integration with booking workflows. The production page already covers those areas, so this sprint avoids a broad rewrite.

## Changes

- Tighten the title and Service schema name around `Limo Website Design Services` while preserving the existing H1 and page body.
- Add one contextual internal link from the indexed Booking Systems page to the website-design owner page.
- Add one contextual internal link from the indexed GEO / AI Search page to the website-design owner page.

## Guardrails

- No new URLs.
- No city/location pages.
- No fake proof or performance claims.
- No sitemap, robots or canonical changes.
- No broad content expansion because the page already satisfies the observed service intent.
""",
    encoding="utf-8",
)

Path("scripts/seo_website_design_support_once.py").unlink(missing_ok=True)
Path(".github/workflows/seo-website-design-owner-support.yml").unlink(missing_ok=True)
