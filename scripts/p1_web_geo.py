from pathlib import Path
import re


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'MISSING:{label}')
    return text.replace(old, new, 1)


def validate(filename, title_fragment, h1_fragment, answer_fragment):
    text = Path(filename).read_text(encoding='utf-8')
    if len(re.findall(r'<h1\b', text, flags=re.I)) != 1:
        raise SystemExit(f'H1_COUNT_FAIL:{filename}')
    if '<link rel="canonical"' not in text:
        raise SystemExit(f'CANONICAL_FAIL:{filename}')
    if '#website' not in text or '#service' not in text or '#webpage' not in text:
        raise SystemExit(f'SCHEMA_GRAPH_FAIL:{filename}')
    for fragment in [title_fragment, h1_fragment, answer_fragment]:
        if fragment not in text:
            raise SystemExit(f'CONTENT_FAIL:{filename}:{fragment}')


# ---------------- WEBSITE DESIGN PAGE ----------------
p = Path('limo-website-design.html')
text = p.read_text(encoding='utf-8')
text = replace_once(text,
    '<title>Limo Website Design | The Limo Marketing Agency</title>',
    '<title>Limo Website Design | Limousine Website Design</title>',
    'web-title')
text = replace_once(text,
    '<meta name="description" content="High-converting limo and chauffeur website design built for search visibility, trust, mobile performance, lead generation and automated bookings."/>',
    '<meta name="description" content="Limo and limousine website design services built for SEO, GEO, mobile performance, trust, lead generation, booking-system integration and measurable conversions."/>',
    'web-meta')
text = replace_once(text,
    '<meta property="og:title" content="Limo Website Design | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="Limo Website Design | Limousine Website Design"/>',
    'web-og-title')
text = replace_once(text,
    '<meta property="og:description" content="High-converting limo and chauffeur website design built for search visibility, trust, mobile performance, lead generation and automated bookings."/>',
    '<meta property="og:description" content="Limo and limousine website design services built for SEO, GEO, mobile performance, trust, lead generation, booking-system integration and measurable conversions."/>',
    'web-og-desc')
text = replace_once(text,
    '"name": "Limo Website Design",\n      "serviceType": "Website design and development for limo, chauffeur, black car and airport transportation companies"',
    '"name": "Limo and Limousine Website Design Services",\n      "serviceType": "Limo website design, limousine web design and website development for limo, chauffeur, black car and airport transportation companies"',
    'web-schema-service')
text = replace_once(text,
    '<h1>Websites Built to <span>Rank, Convert &amp; Book Rides.</span></h1>',
    '<h1>Limo Website Design Built to <span>Rank, Convert &amp; Book Rides.</span></h1>',
    'web-h1')
text = replace_once(text,
    '<div class="container"><div class="answer-card reveal"><span aria-hidden="true" class="brand-badge"></span><div><h2>What should a limo company website include?</h2><p>A strong limo website should clearly explain services and service areas, establish trust, work perfectly on mobile, load quickly, use crawlable SEO-friendly HTML, support local and AI-search understanding, connect visitors to calls or online booking, and measure the actions that create leads and paid rides. The visual design matters, but the business system behind the design matters more.</p></div></div></div>',
    '<div class="container"><div class="answer-card reveal"><span aria-hidden="true" class="brand-badge"></span><div><h2>What is limo website design?</h2><p><strong>Limo website design is the planning, design and development of a website specifically for limousine, chauffeur, black car and airport transportation companies.</strong> A strong limo website should explain services and service areas clearly, establish trust, work well on mobile, load quickly, use crawlable SEO-friendly HTML, support local and AI-search understanding, connect visitors to calls or online booking, and measure the actions that create leads and paid rides.</p></div></div></div>',
    'web-answer')
p.write_text(text, encoding='utf-8')


# ---------------- GEO PAGE ----------------
p = Path('geo-ai-search-optimization.html')
text = p.read_text(encoding='utf-8')
text = replace_once(text,
    '<title>GEO & AI Search for Limo Companies | The Limo Marketing Agency</title>',
    '<title>GEO, AEO &amp; AI Search Optimization for Limo Companies</title>',
    'geo-title')
text = replace_once(text,
    '<meta name="description" content="GEO and AI search optimization for limo, chauffeur and black car companies, designed to improve how search and AI systems understand your business."/>',
    '<meta name="description" content="GEO, AEO and AI search optimization for limo, chauffeur and black car companies using entity clarity, answer-ready content, structured data, evidence and technical SEO."/>',
    'geo-meta')
text = replace_once(text,
    '<meta property="og:title" content="GEO &amp; AI Search for Limo Companies | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="GEO, AEO &amp; AI Search Optimization for Limo Companies"/>',
    'geo-og-title')
text = replace_once(text,
    '<meta property="og:description" content="GEO and AI search optimization for limo, chauffeur and black car companies, designed to improve how search and AI systems understand your business."/>',
    '<meta property="og:description" content="GEO, AEO and AI search optimization for limo, chauffeur and black car companies using entity clarity, answer-ready content, structured data, evidence and technical SEO."/>',
    'geo-og-desc')
text = replace_once(text,
    '<h1>Make Your Limo Business Easier for AI Search to <span>Understand, Retrieve &amp; Reference.</span></h1>',
    '<h1>GEO &amp; AI Search Optimization for Limo Companies That Need to Be <span>Understood, Retrieved &amp; Referenced.</span></h1>',
    'geo-h1')
text = replace_once(text,
    '<div class="container"><div class="answer-box"><span aria-hidden="true" class="brand-badge"></span><div><h2>What is GEO / AEO for limo companies?</h2><p>GEO and AEO are ways of preparing a limo, chauffeur, black car or airport transportation business to be clearly understood and usefully represented in AI-powered search and answer experiences. In practice, that means strong SEO foundations, unambiguous entity and service information, useful answer-style content, technical accessibility, evidence, structured relationships and measurement of the visibility that current webmaster tools actually expose.</p></div></div></div>',
    '<div class="container"><div class="answer-box"><span aria-hidden="true" class="brand-badge"></span><div><h2>What are GEO and AEO for limo companies?</h2><p><strong>GEO (generative engine optimization) and AEO (answer engine optimization) help a limo, chauffeur, black car or airport transportation business become easier for AI-powered search and answer systems to understand, retrieve and reference.</strong> In practice, that means strong SEO foundations, clear entity and service information, answer-ready content, crawlable pages, structured relationships, first-party evidence and careful measurement of the visibility that current platforms actually expose.</p></div></div></div>',
    'geo-answer')
text = replace_once(text,
    '"name": "GEO / AI Search Optimization for Limo Companies",',
    '"name": "GEO, AEO and AI Search Optimization for Limo Companies",',
    'geo-webpage-name')
p.write_text(text, encoding='utf-8')

validate('limo-website-design.html', 'Limo Website Design | Limousine Website Design', 'Limo Website Design Built to', 'What is limo website design?')
validate('geo-ai-search-optimization.html', 'GEO, AEO &amp; AI Search Optimization for Limo Companies', 'GEO &amp; AI Search Optimization for Limo Companies', 'What are GEO and AEO for limo companies?')
print('P1_WEB_GEO_PASS')
