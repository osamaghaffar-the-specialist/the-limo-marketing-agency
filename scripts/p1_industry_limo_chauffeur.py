from pathlib import Path
import re


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'MISSING:{label}')
    return text.replace(old, new, 1)


def validate(path, title_fragment, h1_fragment, answer_fragment, about_fragment, mentions_fragment):
    text = Path(path).read_text(encoding='utf-8')
    if len(re.findall(r'<h1\b', text, flags=re.I)) != 1:
        raise SystemExit(f'H1_COUNT_FAIL:{path}')
    if '<link rel="canonical"' not in text:
        raise SystemExit(f'CANONICAL_FAIL:{path}')
    if '#website' not in text or '#webpage' not in text:
        raise SystemExit(f'ENTITY_GRAPH_FAIL:{path}')
    for fragment in [title_fragment, h1_fragment, answer_fragment, about_fragment, mentions_fragment]:
        if fragment not in text:
            raise SystemExit(f'CONTENT_FAIL:{path}:{fragment}')


# ---------------- LIMOUSINE INDUSTRY PAGE ----------------
p = Path('limousine-companies.html')
text = p.read_text(encoding='utf-8')
text = replace_once(text,
    '<title>Limousine Company Marketing | The Limo Marketing Agency</title>',
    '<title>Marketing for Limousine Companies | Growth &amp; Booking Strategy</title>',
    'limo-title')
text = replace_once(text,
    '<meta content="Google Ads, SEO, GEO, website design and booking systems for limousine companies seeking more qualified traffic, enquiries and ride bookings." name="description"/>',
    '<meta content="Growth strategy for limousine companies across Google Ads, SEO, GEO, website design and booking systems, built around airport, corporate, hourly and event demand." name="description"/>',
    'limo-meta')
text = replace_once(text,
    '<meta property="og:title" content="Limousine Company Marketing | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="Marketing for Limousine Companies | Growth &amp; Booking Strategy"/>',
    'limo-og-title')
text = replace_once(text,
    '<meta property="og:description" content="Google Ads, SEO, GEO, website design and booking systems for limousine companies seeking more qualified traffic, enquiries and ride bookings."/>',
    '<meta property="og:description" content="Growth strategy for limousine companies across Google Ads, SEO, GEO, website design and booking systems, built around airport, corporate, hourly and event demand."/>',
    'limo-og-desc')
text = replace_once(text,
    '"name": "Marketing for Limousine Companies",',
    '"name": "Growth and Marketing for Limousine Companies",',
    'limo-webpage-name')
text = replace_once(text,
    '''"about": [
        {
          "@type": "Thing",
          "name": "Limousine Companies"
        },
        {
          "@type": "Thing",
          "name": "Limo Marketing"
        },
        {
          "@type": "Thing",
          "name": "Limo Booking Systems"
        }
      ],''',
    '''"about": [
        {
          "@type": "Thing",
          "name": "Limousine Companies"
        },
        {
          "@type": "Thing",
          "name": "Limousine Services"
        }
      ],
      "mentions": [
        {
          "@type": "Thing",
          "name": "Google Ads for Limousine Companies"
        },
        {
          "@type": "Thing",
          "name": "Search Engine Optimization for Limousine Companies"
        },
        {
          "@type": "Thing",
          "name": "Generative Engine Optimization for Limousine Companies"
        },
        {
          "@type": "Thing",
          "name": "Limo Website Design"
        },
        {
          "@type": "Thing",
          "name": "Limo Booking Systems"
        }
      ],''',
    'limo-about-mentions')
text = replace_once(text,
    '<h1>Build a Limo Business That Is Easier to <span>Find, Trust and Book.</span></h1>',
    '<h1>Marketing for Limousine Companies Built Around <span>Search, Trust and Booking.</span></h1>',
    'limo-h1')
text = replace_once(text,
    '<div class="container"><div class="answer-card reveal"><span class="brand-badge"></span><div><h2>What marketing does a limousine company actually need?</h2><p>A limo company typically needs a combination of high-intent demand generation, strong local and organic visibility, a premium mobile-first website, service-specific landing pages, a clear fleet presentation, measurable conversion tracking and a booking experience that fits its ride types and pricing model. The right mix depends on where the current customer journey is breaking.</p></div></div>',
    '<div class="container"><div class="answer-card reveal"><span class="brand-badge"></span><div><h2>What is marketing for limousine companies?</h2><p><strong>Marketing for limousine companies is the coordinated system used to attract high-intent riders, prove service fit and move them into a measurable call, inquiry or booking path.</strong> It can combine Google Ads for immediate demand, SEO for long-term discovery, GEO/AEO for clearer AI-search understanding, service-specific landing pages, premium website design, fleet presentation, conversion tracking and booking infrastructure. The right mix depends on the operator\'s services, market and current customer-journey bottleneck.</p></div></div>',
    'limo-answer')
p.write_text(text, encoding='utf-8')


# ---------------- CHAUFFEUR INDUSTRY PAGE ----------------
p = Path('chauffeur-companies.html')
text = p.read_text(encoding='utf-8')
text = replace_once(text,
    '<title>Chauffeur Company Marketing | The Limo Marketing Agency</title>',
    '<title>Marketing for Chauffeur Companies | Executive Growth Strategy</title>',
    'chauffeur-title')
text = replace_once(text,
    '<meta content="Google Ads, SEO, GEO, websites and booking systems for chauffeur companies seeking more corporate, airport and premium ride bookings." name="description"/>',
    '<meta content="Marketing for chauffeur companies focused on corporate, airport, executive and repeat-client demand using Google Ads, SEO, GEO, premium websites and booking systems." name="description"/>',
    'chauffeur-meta')
text = replace_once(text,
    '<meta property="og:title" content="Chauffeur Company Marketing | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="Marketing for Chauffeur Companies | Executive Growth Strategy"/>',
    'chauffeur-og-title')
text = replace_once(text,
    '<meta property="og:description" content="Google Ads, SEO, GEO, websites and booking systems for chauffeur companies seeking more corporate, airport and premium ride bookings."/>',
    '<meta property="og:description" content="Marketing for chauffeur companies focused on corporate, airport, executive and repeat-client demand using Google Ads, SEO, GEO, premium websites and booking systems."/>',
    'chauffeur-og-desc')
text = replace_once(text,
    '"name": "Marketing for Chauffeur Companies",',
    '"name": "Growth and Marketing for Chauffeur Companies",',
    'chauffeur-webpage-name')
text = replace_once(text,
    '''"about": [
        {
          "@type": "Thing",
          "name": "Chauffeur Companies"
        },
        {
          "@type": "Thing",
          "name": "Executive Transportation Marketing"
        },
        {
          "@type": "Thing",
          "name": "Corporate Chauffeur Services"
        }
      ],''',
    '''"about": [
        {
          "@type": "Thing",
          "name": "Chauffeur Companies"
        },
        {
          "@type": "Thing",
          "name": "Executive Chauffeur Services"
        },
        {
          "@type": "Thing",
          "name": "Corporate Chauffeur Services"
        }
      ],
      "mentions": [
        {
          "@type": "Thing",
          "name": "Google Ads for Chauffeur Companies"
        },
        {
          "@type": "Thing",
          "name": "Search Engine Optimization for Chauffeur Companies"
        },
        {
          "@type": "Thing",
          "name": "Generative Engine Optimization for Chauffeur Companies"
        },
        {
          "@type": "Thing",
          "name": "Chauffeur Website Design"
        },
        {
          "@type": "Thing",
          "name": "Chauffeur Booking Systems"
        }
      ],''',
    'chauffeur-about-mentions')
text = replace_once(text,
    '<h1>Position Your Chauffeur Business for <span>Premium, Corporate and Repeat Clients.</span></h1>',
    '<h1>Marketing for Chauffeur Companies Built for <span>Premium, Corporate and Repeat Clients.</span></h1>',
    'chauffeur-h1')
text = replace_once(text,
    '<h2>What makes chauffeur company marketing different?</h2>\n<p>Chauffeur companies often compete for executive travelers, corporate accounts, airport transfers, roadshows and premium point-to-point work. That means the marketing must do more than attract clicks. It needs to communicate professionalism, service standards, fleet quality, operational reliability and a credible booking or account experience.</p>',
    '<h2>What is marketing for chauffeur companies?</h2>\n<p><strong>Marketing for chauffeur companies is the system used to attract executive, corporate, airport and premium travel demand while communicating the reliability and professionalism required by higher-value buyers.</strong> It combines demand capture, premium positioning, search visibility, service and fleet clarity, conversion tracking, booking workflows and corporate-account pathways so the business is evaluated on fit and trust rather than price alone.</p>',
    'chauffeur-answer')
p.write_text(text, encoding='utf-8')

validate('limousine-companies.html', 'Marketing for Limousine Companies | Growth &amp; Booking Strategy', 'Marketing for Limousine Companies Built Around', 'What is marketing for limousine companies?', '"name": "Limousine Companies"', '"mentions": [')
validate('chauffeur-companies.html', 'Marketing for Chauffeur Companies | Executive Growth Strategy', 'Marketing for Chauffeur Companies Built for', 'What is marketing for chauffeur companies?', '"name": "Chauffeur Companies"', '"mentions": [')
print('P1_INDUSTRY_LIMO_CHAUFFEUR_PASS')
