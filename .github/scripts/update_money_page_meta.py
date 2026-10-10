from pathlib import Path
import html
import re

UPDATES = {
    "seo-for-limo-companies.html": (
        "Limo SEO services for limo, chauffeur and black car companies, including technical SEO, local search, service pages, content, internal linking and organic growth strategy.",
        "Limo SEO services for limo, chauffeur and black car companies covering technical SEO, local search, content, internal linking and organic visibility.",
    ),
    "google-ads-for-limo-companies.html": (
        "Limo Google Ads and PPC management for limo, chauffeur and black car companies focused on high-intent searches, conversion tracking, qualified leads and booked rides.",
        "Limo Google Ads and PPC management focused on high-intent searches, qualified leads, conversion tracking and booked rides for limo and black car companies.",
    ),
    "geo-ai-search-optimization.html": (
        "GEO, AEO and AI search optimization for limo, chauffeur and black car companies using entity clarity, answer-ready content, structured data, evidence and technical SEO.",
        "GEO, AEO and AI search optimization for limo, chauffeur and black car companies using entity clarity, answer-ready content, structured data and technical SEO.",
    ),
    "limo-website-design.html": (
        "Limo and limousine website design services built for SEO, GEO, mobile performance, trust, lead generation, booking-system integration and measurable conversions.",
        "Limo and limousine website design built for SEO, GEO, mobile performance, trust, lead generation, booking integrations and measurable conversions.",
    ),
    "booking-systems.html": (
        "Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies.",
        "Custom limo booking software with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies.",
    ),
}

meta_re = re.compile(r'<meta(?=[^>]*\bname=["\']description["\'])[^>]*\bcontent=["\']([^"\']*)["\'][^>]*>', re.I)
og_re = re.compile(r'<meta(?=[^>]*\bproperty=["\']og:description["\'])[^>]*\bcontent=["\']([^"\']*)["\'][^>]*>', re.I)

for filename, (old, new) in UPDATES.items():
    path = Path(filename)
    text = path.read_text(encoding="utf-8")

    if not 135 <= len(new) <= 160:
        raise SystemExit(f"{filename}: new description length {len(new)} outside 135-160")

    meta_matches = list(meta_re.finditer(text))
    og_matches = list(og_re.finditer(text))
    if len(meta_matches) != 1 or len(og_matches) != 1:
        raise SystemExit(f"{filename}: expected one meta description and one OG description")
    if html.unescape(meta_matches[0].group(1)) != old:
        raise SystemExit(f"{filename}: current meta description does not match audited source")
    if html.unescape(og_matches[0].group(1)) != old:
        raise SystemExit(f"{filename}: current OG description does not match audited source")

    new_text, meta_count = meta_re.subn(
        lambda m: m.group(0).replace(m.group(1), new, 1), text, count=1
    )
    new_text, og_count = og_re.subn(
        lambda m: m.group(0).replace(m.group(1), new, 1), new_text, count=1
    )
    if meta_count != 1 or og_count != 1:
        raise SystemExit(f"{filename}: replacement count validation failed")

    path.write_text(new_text, encoding="utf-8")

    meta = meta_re.search(new_text)
    og = og_re.search(new_text)
    if not meta or not og:
        raise SystemExit(f"{filename}: post-edit description tag validation failed")
    if html.unescape(meta.group(1)) != new or html.unescape(og.group(1)) != new:
        raise SystemExit(f"{filename}: meta/OG descriptions do not match intended text")

    print(f"{filename} PASS length={len(new)}")

print("UPDATED", len(UPDATES), "FILES")
