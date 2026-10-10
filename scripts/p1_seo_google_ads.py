from pathlib import Path
import re


def must_replace(text, old, new, label):
    if old not in text:
        raise SystemExit(f'MISSING:{label}')
    return text.replace(old, new, 1)

# This second pass removes duplicate answer blocks discovered during review and
# strengthens the site's pre-existing answer boxes instead of adding new ones.

# ---------------- SEO PAGE ----------------
p = Path('seo-for-limo-companies.html')
text = p.read_text(encoding='utf-8')
seo_duplicate = '''<section class="section soft" aria-labelledby="what-is-limo-seo">
<div class="container">
<div class="center-head">
<div class="kicker">QUICK ANSWER</div>
<h2 id="what-is-limo-seo">What Is Limo SEO?</h2>
<p><strong>Limo SEO is search engine optimization for limousine, chauffeur, black car and airport transportation companies.</strong> It combines technical SEO, local search, service and location pages, internal linking, structured data and content built around searches that can lead to calls, quote requests and bookings.</p>
</div>
</div>
</section>
'''
if seo_duplicate in text:
    text = text.replace(seo_duplicate, '', 1)

text = must_replace(
    text,
    '<div><h2>What is SEO for limo companies?</h2><p>SEO for limo companies is the process of making a limo, chauffeur, black car or airport transportation business easier to find in organic and local search for commercially relevant queries, while connecting those search visits to calls, consultation requests and booking flows. The goal is not simply more rankings, it is more qualified visibility and measurable customer action.</p></div>',
    '<div><h2>What is limo SEO and how does it help limo companies?</h2><p><strong>Limo SEO is search engine optimization for limousine, chauffeur, black car and airport transportation companies.</strong> It combines technical SEO, local search, service and location pages, internal linking, structured data and useful content so the business is easier to find for commercially relevant searches and those visits can move toward calls, quote requests and bookings.</p></div>',
    'seo-existing-answer'
)
p.write_text(text, encoding='utf-8')

# ---------------- GOOGLE ADS PAGE ----------------
p = Path('google-ads-for-limo-companies.html')
text = p.read_text(encoding='utf-8')
ads_duplicate = '''<section class="section soft" aria-labelledby="what-are-limo-google-ads">
<div class="container">
<div class="center-head">
<div class="kicker">QUICK ANSWER</div>
<h2 id="what-are-limo-google-ads">What Are Limo Google Ads?</h2>
<p><strong>Limo Google Ads are paid search campaigns designed for limousine, chauffeur, black car and airport transportation services.</strong> For a limo service, Google Ads and PPC work best when high-intent keywords, location targeting, negative keywords, landing pages and conversion tracking are aligned around calls, quote requests and bookings.</p>
</div>
</div>
</section>
'''
if ads_duplicate in text:
    text = text.replace(ads_duplicate, '', 1)

text = must_replace(
    text,
    '<h2 id="quick-answer-title">Do Google Ads work for limo companies?</h2>\n<p>They can work well when campaigns target real booking intent, send each search to a relevant landing page and measure valuable actions such as calls, consultation requests or completed bookings. The goal is not to buy more traffic. The goal is to buy the right demand and connect it to a conversion path.</p>',
    '<h2 id="quick-answer-title">What are limo Google Ads, and do they work for limo companies?</h2>\n<p><strong>Limo Google Ads are paid search campaigns designed for limousine, chauffeur, black car and airport transportation services.</strong> They can work well when campaigns target real booking intent, use relevant location and negative-keyword controls, send each search to the right landing page and measure valuable actions such as calls, consultation requests or completed bookings.</p>',
    'ads-existing-answer'
)
p.write_text(text, encoding='utf-8')

# Validation
seo = Path('seo-for-limo-companies.html').read_text(encoding='utf-8')
ads = Path('google-ads-for-limo-companies.html').read_text(encoding='utf-8')
for filename, t in [('seo-for-limo-companies.html', seo), ('google-ads-for-limo-companies.html', ads)]:
    if len(re.findall(r'<h1\b', t, flags=re.I)) != 1:
        raise SystemExit(f'H1_COUNT_FAIL:{filename}')
    if '<link rel="canonical"' not in t:
        raise SystemExit(f'CANONICAL_FAIL:{filename}')
    if '#website' not in t or '#service' not in t or '#webpage' not in t:
        raise SystemExit(f'SCHEMA_GRAPH_FAIL:{filename}')

if 'id="what-is-limo-seo"' in seo:
    raise SystemExit('SEO_DUPLICATE_ANSWER_REMAINS')
if 'id="what-are-limo-google-ads"' in ads:
    raise SystemExit('ADS_DUPLICATE_ANSWER_REMAINS')
if 'What is limo SEO and how does it help limo companies?' not in seo:
    raise SystemExit('SEO_ANSWER_MISSING')
if 'What are limo Google Ads, and do they work for limo companies?' not in ads:
    raise SystemExit('ADS_ANSWER_MISSING')

print('P1_SEO_GOOGLE_ADS_REVIEW_PASS')
