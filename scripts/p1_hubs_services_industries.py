from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f"{label}: expected exactly 1 match, found {count}")
    return text.replace(old, new, 1)


def validate_jsonld(text, path):
    blocks = re.findall(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', text, flags=re.S)
    if not blocks:
        raise SystemExit(f"{path}: no JSON-LD blocks found")
    for i, block in enumerate(blocks, 1):
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"{path}: JSON-LD block {i} invalid: {exc}")


# ---------------- industries.html ----------------
path = ROOT / "industries.html"
text = path.read_text(encoding="utf-8")

old_collection = '''    {
      "@type": "CollectionPage",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/industries.html#webpage",
      "name": "Industries We Serve",
      "isPartOf": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#website"
      },
      "description": "Industry-specific marketing, website, SEO, GEO, booking automation and growth systems for premium transportation businesses.",
      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/industries.html",
      "inLanguage": "en"
    },
'''

new_collection = '''    {
      "@type": "CollectionPage",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/industries.html#webpage",
      "name": "Transportation Industries We Serve",
      "isPartOf": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#website"
      },
      "publisher": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#organization"
      },
      "about": [
        {"@type": "Thing", "name": "Limousine Companies"},
        {"@type": "Thing", "name": "Chauffeur Companies"},
        {"@type": "Thing", "name": "Black Car Services"},
        {"@type": "Thing", "name": "Airport Transportation Companies"}
      ],
      "mainEntity": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/industries.html#industry-list"
      },
      "description": "Industry-specific marketing, website, SEO, GEO, booking automation and growth systems for premium transportation businesses.",
      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/industries.html",
      "inLanguage": "en"
    },
    {
      "@type": "ItemList",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/industries.html#industry-list",
      "name": "Premium Transportation Industries",
      "numberOfItems": 4,
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/limousine-companies.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/limousine-companies.html",
            "name": "Marketing for Limousine Companies"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/chauffeur-companies.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/chauffeur-companies.html",
            "name": "Marketing for Chauffeur Companies"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/black-car-services.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/black-car-services.html",
            "name": "Marketing for Black Car Services"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/airport-transportation-companies.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/airport-transportation-companies.html",
            "name": "Airport Transportation Marketing"
          }
        }
      ]
    },
'''
text = replace_once(text, old_collection, new_collection, "industries schema hub")

text = replace_once(
    text,
    '<h1>Built Specifically for <span>Premium Transportation Businesses.</span></h1>',
    '<h1>Marketing for <span>Limo, Chauffeur, Black Car &amp; Airport Transportation Companies.</span></h1>',
    "industries H1",
)

text = replace_once(
    text,
    '<h2>Who does The Limo Marketing Agency work with?</h2><p>We specialize in premium ground transportation businesses, especially limousine companies, chauffeur companies, black car services and airport transportation companies. Our work can include Google Ads, SEO, GEO and AI search optimization, website design, automated booking systems, social media marketing, analytics and conversion-focused digital infrastructure.</p>',
    '<h2>Which transportation businesses does The Limo Marketing Agency serve?</h2><p><strong>The Limo Marketing Agency specializes in limousine companies, executive chauffeur companies, black car services and airport transportation operators.</strong> We connect customer acquisition, SEO/GEO visibility, premium websites and booking infrastructure, while adapting the strategy to each operator\'s service mix, fleet, market, corporate-account needs and customer booking journey.</p>',
    "industries answer block",
)

if text.count('<h1>') != 1:
    raise SystemExit("industries.html must contain exactly one H1")
if 'industries.html#industry-list' not in text or text.count('"numberOfItems": 4') != 1:
    raise SystemExit("industries ItemList validation failed")
validate_jsonld(text, path.name)
path.write_text(text, encoding="utf-8")


# ---------------- services.html ----------------
path = ROOT / "services.html"
text = path.read_text(encoding="utf-8")

old_desc = 'Explore Google Ads, SEO, GEO, website design, booking automation, analytics and growth services built for limo, chauffeur and black car companies worldwide.'
new_desc = 'Explore Google Ads, SEO, GEO, website design, booking systems, automation and analytics for limo, chauffeur, black car and airport transportation companies.'
if text.count(old_desc) != 3:
    raise SystemExit(f"services description: expected 3 matches, found {text.count(old_desc)}")
text = text.replace(old_desc, new_desc)

old_page = '''    {
      "@type": "WebPage",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/services.html#webpage",
      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/services.html",
      "name": "Limo Marketing Services | SEO, Google Ads & Booking Systems",
      "description": "Explore Google Ads, SEO, GEO, website design, booking systems, automation and analytics for limo, chauffeur, black car and airport transportation companies.",
      "about": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#organization"
      },
      "inLanguage": "en",
      "isPartOf": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#website"
      }
    },
'''

new_page = '''    {
      "@type": "CollectionPage",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/services.html#webpage",
      "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/services.html",
      "name": "Limo Marketing Services | SEO, Google Ads & Booking Systems",
      "description": "Explore Google Ads, SEO, GEO, website design, booking systems, automation and analytics for limo, chauffeur, black car and airport transportation companies.",
      "isPartOf": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#website"
      },
      "publisher": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/#organization"
      },
      "about": {
        "@type": "Thing",
        "name": "Limo Marketing Services"
      },
      "mainEntity": {
        "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/services.html#service-list"
      },
      "inLanguage": "en"
    },
    {
      "@type": "ItemList",
      "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/services.html#service-list",
      "name": "Core Limo Marketing Services",
      "numberOfItems": 6,
      "itemListOrder": "https://schema.org/ItemListOrderAscending",
      "itemListElement": [
        {
          "@type": "ListItem",
          "position": 1,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/google-ads-for-limo-companies.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/google-ads-for-limo-companies.html",
            "name": "Limo Google Ads & PPC"
          }
        },
        {
          "@type": "ListItem",
          "position": 2,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/seo-for-limo-companies.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/seo-for-limo-companies.html",
            "name": "Limo SEO Services"
          }
        },
        {
          "@type": "ListItem",
          "position": 3,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/geo-ai-search-optimization.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/geo-ai-search-optimization.html",
            "name": "GEO, AEO & AI Search Optimization"
          }
        },
        {
          "@type": "ListItem",
          "position": 4,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/limo-website-design.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/limo-website-design.html",
            "name": "Limo Website Design"
          }
        },
        {
          "@type": "ListItem",
          "position": 5,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/booking-systems.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/booking-systems.html",
            "name": "Limo Booking Software & System"
          }
        },
        {
          "@type": "ListItem",
          "position": 6,
          "item": {
            "@type": "WebPage",
            "@id": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/social-media-marketing-for-limo-companies.html#webpage",
            "url": "https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/social-media-marketing-for-limo-companies.html",
            "name": "Social Media Marketing for Limo Companies"
          }
        }
      ]
    },
'''
text = replace_once(text, old_page, new_page, "services schema hub")

text = replace_once(
    text,
    '<h1>Build. Fix. Grow. <span>Your Limo Business Digitally</span></h1>',
    '<h1>Limo Marketing Services Built as <span>One Connected Growth System.</span></h1>',
    "services H1",
)

old_hero = '''<p>
              From Google Ads and SEO to Premium Websites, Booking Systems, Automation and Admin Portals  we build the Digital Infrastructure that helps Limo and Black Car Companies get Discovered, Convert Demand and Operate more Efficiently.
            </p>'''
new_hero = '''<p><strong>Limo marketing services connect Google Ads, SEO, GEO and AI search, premium website design, booking systems, automation and measurement into one customer-acquisition and booking journey.</strong> We build that connected infrastructure for limo, chauffeur, black car and airport transportation operators so each channel supports the same path from discovery to customer action.</p>'''
text = replace_once(text, old_hero, new_hero, "services hero answer")

text = text.replace('href="index.html#process"', 'href="./#process"')

if text.count('<h1>') != 1:
    raise SystemExit("services.html must contain exactly one H1")
if 'index.html#process' in text:
    raise SystemExit("services.html still contains index.html#process")
if 'services.html#service-list' not in text or text.count('"numberOfItems": 6') != 1:
    raise SystemExit("services ItemList validation failed")
if text.count('rel="canonical"') != 1:
    raise SystemExit("services canonical count changed unexpectedly")
validate_jsonld(text, path.name)
path.write_text(text, encoding="utf-8")

print("P1 hub optimization complete: industries.html + services.html")
