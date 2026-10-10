from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
BASE='https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/'
changed=[]

def load(name): return (ROOT/name).read_text(encoding='utf-8')
def save(name,text,old):
    if text==old: raise SystemExit(f'{name}: no changes applied')
    (ROOT/name).write_text(text,encoding='utf-8'); changed.append(name)
def once(text,old,new,label):
    c=text.count(old)
    if c!=1: raise SystemExit(f'{label}: expected 1 match, found {c}')
    return text.replace(old,new,1)

def jsonld_ok(name,text):
    blocks=re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>\s*(.*?)\s*</script>',text,flags=re.S|re.I)
    for i,b in enumerate(blocks,1):
        try: json.loads(b)
        except Exception as e: raise SystemExit(f'{name}: invalid JSON-LD block {i}: {e}')

# 1) Remove visible pre-launch/demo copy from live lead forms.
replacements={
'about.html': [('Connect this form to the production CRM or email endpoint before launch.','Your details are sent to our team so we can review the business and respond to your consultation request.')],
'case-studies-results.html': [('Connect this form to the production CRM / email endpoint before launch.','Your details are sent to our team so we can review the business and respond to your consultation request.')],
'contact.html': [('Your information should only be used to review and respond to your consultation request. Add the production privacy-policy link before launch.','Your information is used only to review and respond to your consultation request. See our <a href="privacy-policy.html">Privacy Policy</a>.')],
'geo-ai-search-optimization.html': [("Form UI is ready. Connect your production CRM or form endpoint before launch.","Thanks — your consultation request is being processed.")],
'google-ads-for-limo-companies.html': [('Form is prepared for a secure CRM or form endpoint. Connect the production endpoint before launch. Do not send sensitive information through an unconfigured demo form.','Your details are sent to our team for consultation follow-up. Please do not include passwords, payment details or other sensitive information.')],
'industries.html': [('Connect this form to the production CRM or email endpoint before launch.','Your details are sent to our team so we can review the business and respond to your consultation request.')],
'seo-for-limo-companies.html': [("Form UI is ready. Connect your production CRM or form endpoint before launch.","Thanks — your consultation request is being processed.")],
'social-media-marketing-for-limo-companies.html': [('This demo form is prepared for lead tracking. Connect it to your production CRM, email or form endpoint before launch.','Your details are sent to our team for consultation follow-up. Please do not include passwords, payment details or other sensitive information.')],
}
for name,pairs in replacements.items():
    old=load(name); text=old
    for a,b in pairs: text=once(text,a,b,f'{name} launch copy')
    save(name,text,old)

# 2) Social-media page: make exact service intent explicit in title/H1 while preserving scope.
name='social-media-marketing-for-limo-companies.html'; old=load(name); text=old
old_title='Social Media for Limo Companies | The Limo Marketing Agency'
if text.count(old_title)!=2: raise SystemExit(f'{name}: expected title twice, found {text.count(old_title)}')
text=text.replace(old_title,'Social Media Marketing for Limo Companies | TLMA')
text=once(text,'<h1>Turn Social Attention into <span>Trust, Traffic &amp; Bookings.</span></h1>','<h1>Social Media Marketing for Limo Companies That Turns <span>Attention into Trust, Traffic &amp; Bookings.</span></h1>',f'{name} H1')
save(name,text,old)

# 3) Resources hub: remove pre-launch subscription copy, strengthen H1, and define the current guide collection in schema.
name='resources.html'; old=load(name); text=old
text=once(text,'<h1>Practical Growth Insights for <span>Premium Transportation Companies.</span></h1>','<h1>Limo Marketing Resources &amp; Growth Guides for <span>Premium Transportation Companies.</span></h1>',f'{name} H1')
text=once(text,'<p>Use this as the future email-capture section for new guides, platform changes and practical growth insights relevant to premium transportation businesses.</p>','<p>Get new guides, platform updates and practical growth insights created for limo, chauffeur, black car and airport transportation operators.</p>',f'{name} subscribe copy')
text=once(text,'<div class="subscribe-note">Connect this form to the production email platform before launch.</div>','<div class="subscribe-note">Practical updates only. You can unsubscribe from future emails at any time.</div>',f'{name} subscribe note')
old_collection='''    {
      "@type": "CollectionPage",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html#webpage",
      "name": "Limo Marketing Resources & Insights",
      "isPartOf": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#website"
      },
      "description": "Educational resources covering limo marketing, SEO, GEO, Google Ads, websites, booking systems and digital operations.",
      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html",
      "inLanguage": "en"
    },
'''
new_collection='''    {
      "@type": "CollectionPage",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html#webpage",
      "name": "Limo Marketing Resources & Insights",
      "isPartOf": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#website"
      },
      "publisher": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#organization"
      },
      "mainEntity": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html#guide-list"
      },
      "description": "Educational resources covering limo marketing, SEO, GEO, Google Ads, websites, booking systems and digital operations.",
      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html",
      "inLanguage": "en"
    },
    {
      "@type": "ItemList",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/resources.html#guide-list",
      "name": "Featured Limo Marketing Guides",
      "numberOfItems": 2,
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "Article",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/how-much-should-limo-company-spend-google-ads-2026.html#article",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/how-much-should-limo-company-spend-google-ads-2026.html",
            "headline": "How Much Should a Limo Company Spend on Google Ads in 2026?"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "Article",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/why-limo-google-ads-get-expensive.html#article",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/why-limo-google-ads-get-expensive.html",
            "headline": "Why Limo Google Ads Get Expensive and What to Check Before Increasing Budget"
          }
        }
      ]
    },
'''
text=once(text,old_collection,new_collection,f'{name} collection schema')
save(name,text,old)

# 4) Homepage: remove illustrative/fake percentage results; keep strategy section useful without invented proof.
name='index.html'; old=load(name); text=old
metric_map={
'198':('<strong>SEO</strong>','<span>Search Visibility &amp; Organic Demand</span>'),
'305':('<strong>PPC</strong>','<span>High-Intent Search Acquisition</span>'),
'206':('<strong>BOOK</strong>','<span>Conversion &amp; Booking Infrastructure</span>'),
}
for target,(strong,span) in metric_map.items():
    pat=re.compile(r'<div class="strategy-stat">\s*<strong class="metric-counter"[^>]*data-target="'+target+r'"[^>]*>.*?</strong>\s*<span>.*?</span>\s*</div>',re.S)
    text,c=pat.subn('<div class="strategy-stat">\n'+strong+'\n'+span+'\n</div>',text,count=1)
    if c!=1: raise SystemExit(f'{name}: metric {target} expected 1 match, found {c}')
text=once(text,'*Illustrative performance figures for website presentation. Replace with verified client results before final launch.','Results vary by market, offer, competition, tracking and execution. Verified client outcomes are published only when supporting data is available.',f'{name} disclaimer')
save(name,text,old)

# 5) Strengthen the Google Ads topic cluster and fix the two low-inbound article relationships.
name='google-ads-for-limo-companies.html'; old=load(name); text=old
text=once(text,'<p>Google Ads gives you reach, but reach without control can become expensive. We manage the settings and search data that determine where budget is being used.</p>','<p>Google Ads gives you reach, but reach without control can become expensive. We manage the settings and search data that determine where budget is being used. If costs are already rising, use our <a href="why-limo-google-ads-get-expensive.html">limo Google Ads cost diagnostic guide</a> before increasing spend.</p>',f'{name} diagnostic link')
save(name,text,old)

name='why-limo-google-ads-get-expensive.html'; old=load(name); text=old
old_card='<article class="related-card reveal"><span class="brand-badge"></span><h3>Airport Pages vs Location Pages</h3><p>How to structure organic search pages around real transportation demand rather than thin location content.</p><a href="seo-for-limo-companies.html">Explore Limo SEO</a></article>'
new_card='<article class="related-card reveal"><span class="brand-badge"></span><h3>Limo Google Ads Budget Guide 2026</h3><p>Use booking goals, acquisition economics and conversion data to decide how much budget the account can support.</p><a href="how-much-should-limo-company-spend-google-ads-2026.html">Read Budget Guide</a></article>'
text=once(text,old_card,new_card,f'{name} budget cluster link')
save(name,text,old)

# 6) QA: all targeted pre-launch signals gone, schemas parse, single H1 on indexable pages, and key links exist.
for path in sorted(ROOT.glob('*.html')):
    text=path.read_text(encoding='utf-8',errors='replace')
    low=text.lower()
    banned=['before launch','demo form','future email-capture','illustrative performance','replace with verified','connect this form','production crm']
    hits=[b for b in banned if b in low]
    if hits: raise SystemExit(f'{path.name}: launch-copy signals remain: {hits}')
    jsonld_ok(path.name,text)
    robots=' '.join(re.findall(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\']([^"\']+)',text,flags=re.I))
    if 'noindex' not in robots.lower() and path.name!='google83fa3a3dc6e43838.html':
        h1s=re.findall(r'<h1\b',text,flags=re.I)
        if len(h1s)!=1: raise SystemExit(f'{path.name}: expected exactly one H1, found {len(h1s)}')

resources=load('resources.html')
if resources.count('resources.html#guide-list')<2 or resources.count('"numberOfItems": 2')!=1: raise SystemExit('resources guide ItemList failed')
social=load('social-media-marketing-for-limo-companies.html')
if 'Social Media Marketing for Limo Companies That Turns' not in social: raise SystemExit('social H1 failed')
if 'why-limo-google-ads-get-expensive.html' not in load('google-ads-for-limo-companies.html'): raise SystemExit('Google Ads diagnostic link missing')
if 'how-much-should-limo-company-spend-google-ads-2026.html' not in load('why-limo-google-ads-get-expensive.html'): raise SystemExit('budget reciprocal link missing')
if any(x in load('index.html') for x in ['data-target="198"','data-target="305"','data-target="206"']): raise SystemExit('illustrative homepage counters still present')

print('P1 FIX COMPLETE')
print('CHANGED_FILES='+' '.join(changed))
