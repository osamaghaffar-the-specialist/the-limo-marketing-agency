from pathlib import Path
import re

ROOT = 'https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/'


def must_replace(text, old, new, label):
    if old not in text:
        raise SystemExit(f'MISSING:{label}')
    return text.replace(old, new, 1)


def insert_after_hero(text, block, marker):
    if marker in text:
        return text
    m = re.search(r'<section[^>]*class="[^"]*hero[^"]*"[^>]*>', text, re.I)
    if not m:
        raise SystemExit(f'MISSING_HERO:{marker}')
    end = text.find('</section>', m.end())
    if end == -1:
        raise SystemExit(f'MISSING_HERO_END:{marker}')
    end += len('</section>')
    return text[:end] + '\n' + block + text[end:]


# ---------------- SEO PAGE ----------------
p = Path('seo-for-limo-companies.html')
text = p.read_text(encoding='utf-8')
text = must_replace(text,
    '<title>SEO for Limo Companies | The Limo Marketing Agency</title>',
    '<title>Limo SEO Services | SEO for Limo Companies</title>',
    'seo-title')
text = must_replace(text,
    '<meta name="description" content="SEO for limo, chauffeur and black car companies, including technical SEO, local search, content, internal linking and organic growth strategy."/>',
    '<meta name="description" content="Limo SEO services for limo, chauffeur and black car companies, including technical SEO, local search, service pages, content, internal linking and organic growth strategy."/>',
    'seo-meta')
text = must_replace(text,
    '<meta property="og:title" content="SEO for Limo Companies | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="Limo SEO Services | SEO for Limo Companies"/>',
    'seo-og-title')
text = must_replace(text,
    '<meta property="og:description" content="SEO for limo, chauffeur and black car companies, including technical SEO, local search, content, internal linking and organic growth strategy."/>',
    '<meta property="og:description" content="Limo SEO services for limo, chauffeur and black car companies, including technical SEO, local search, service pages, content, internal linking and organic growth strategy."/>',
    'seo-og-description')
text = must_replace(text,
    '"name": "SEO for Limo Companies",\n      "serviceType": "Search engine optimization for limo, chauffeur, black car and airport transportation companies"',
    '"name": "Limo SEO Services for Limo Companies",\n      "serviceType": "Limo SEO and search engine optimization services for limo, chauffeur, black car and airport transportation companies"',
    'seo-service-schema')
text = must_replace(text,
    '<div class="eyebrow"><span class="dot"></span>SEO FOR LIMO COMPANIES</div>',
    '<div class="eyebrow"><span class="dot"></span>LIMO SEO SERVICES</div>',
    'seo-eyebrow')
text = must_replace(text,
    '<h1>Get Found When Limo Customers Are <span>Already Searching.</span></h1>',
    '<h1>Limo SEO Services That Get You Found When Customers Are <span>Already Searching.</span></h1>',
    'seo-h1')
text = must_replace(text,
    '<p>We build organic search visibility for limo, chauffeur, black car and airport transportation companies around the searches that can become calls, booking requests and paid rides, not traffic for traffic\'s sake.</p>',
    '<p>Our limo SEO services build organic search visibility for limo, chauffeur, black car and airport transportation companies around the searches that can become calls, booking requests and paid rides, not traffic for traffic\'s sake.</p>',
    'seo-hero-copy')

seo_answer = '''<section class="section soft" aria-labelledby="what-is-limo-seo">
<div class="container">
<div class="center-head">
<div class="kicker">QUICK ANSWER</div>
<h2 id="what-is-limo-seo">What Is Limo SEO?</h2>
<p><strong>Limo SEO is search engine optimization for limousine, chauffeur, black car and airport transportation companies.</strong> It combines technical SEO, local search, service and location pages, internal linking, structured data and content built around searches that can lead to calls, quote requests and bookings.</p>
</div>
</div>
</section>'''
text = insert_after_hero(text, seo_answer, 'id="what-is-limo-seo"')
p.write_text(text, encoding='utf-8')


# ---------------- GOOGLE ADS PAGE ----------------
p = Path('google-ads-for-limo-companies.html')
text = p.read_text(encoding='utf-8')
text = must_replace(text,
    '<title>Google Ads for Limo Companies | The Limo Marketing Agency</title>',
    '<title>Limo Google Ads &amp; PPC | Google Ads for Limo Companies</title>',
    'ads-title')
text = must_replace(text,
    '<meta name="description" content="Google Ads management for limo, chauffeur and black car companies focused on high-intent searches, qualified leads, conversion tracking and booked rides."/>',
    '<meta name="description" content="Limo Google Ads and PPC management for limo, chauffeur and black car companies focused on high-intent searches, conversion tracking, qualified leads and booked rides."/>',
    'ads-meta')
text = must_replace(text,
    '<meta property="og:title" content="Google Ads for Limo Companies | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="Limo Google Ads &amp; PPC | Google Ads for Limo Companies"/>',
    'ads-og-title')
text = must_replace(text,
    '<meta property="og:description" content="Google Ads management for limo, chauffeur and black car companies focused on high-intent searches, qualified leads, conversion tracking and booked rides."/>',
    '<meta property="og:description" content="Limo Google Ads and PPC management for limo, chauffeur and black car companies focused on high-intent searches, conversion tracking, qualified leads and booked rides."/>',
    'ads-og-description')
text = must_replace(text,
    '"name": "Google Ads Management for Limo Companies",\n      "serviceType": "Google Ads and PPC management for limo, chauffeur and black car companies"',
    '"name": "Limo Google Ads and PPC Management",\n      "serviceType": "Google Ads and PPC management for limo, chauffeur, black car and airport transportation companies"',
    'ads-service-schema')
text = must_replace(text,
    '<div class="eyebrow"><span class="dot"></span>Google Ads for Limo Companies</div>',
    '<div class="eyebrow"><span class="dot"></span>Limo Google Ads &amp; PPC</div>',
    'ads-eyebrow')
text = must_replace(text,
    '<h1 id="page-title">Turn High-Intent Searches into <span>Booked Rides.</span></h1>',
    '<h1 id="page-title">Limo Google Ads That Turn High-Intent Searches into <span>Booked Rides.</span></h1>',
    'ads-h1')
text = must_replace(text,
    '<p>Google Ads management built specifically for limo companies, chauffeur companies, black car services and airport transportation businesses. We connect search intent, campaign structure, landing pages and conversion tracking so you can focus spend on the searches most likely to become real business.</p>',
    '<p>Our limo Google Ads and PPC management is built specifically for limo companies, chauffeur companies, black car services and airport transportation businesses. We connect search intent, campaign structure, landing pages and conversion tracking so you can focus spend on the searches most likely to become real business.</p>',
    'ads-hero-copy')

ads_answer = '''<section class="section soft" aria-labelledby="what-are-limo-google-ads">
<div class="container">
<div class="center-head">
<div class="kicker">QUICK ANSWER</div>
<h2 id="what-are-limo-google-ads">What Are Limo Google Ads?</h2>
<p><strong>Limo Google Ads are paid search campaigns designed for limousine, chauffeur, black car and airport transportation services.</strong> For a limo service, Google Ads and PPC work best when high-intent keywords, location targeting, negative keywords, landing pages and conversion tracking are aligned around calls, quote requests and bookings.</p>
</div>
</div>
</section>'''
text = insert_after_hero(text, ads_answer, 'id="what-are-limo-google-ads"')
p.write_text(text, encoding='utf-8')

# Validation
for filename in ['seo-for-limo-companies.html', 'google-ads-for-limo-companies.html']:
    t = Path(filename).read_text(encoding='utf-8')
    if len(re.findall(r'<h1\b', t, flags=re.I)) != 1:
        raise SystemExit(f'H1_COUNT_FAIL:{filename}')
    if '<link rel="canonical"' not in t:
        raise SystemExit(f'CANONICAL_FAIL:{filename}')
    if '#website' not in t or '#service' not in t or '#webpage' not in t:
        raise SystemExit(f'SCHEMA_GRAPH_FAIL:{filename}')

print('P1_SEO_GOOGLE_ADS_PASS')
