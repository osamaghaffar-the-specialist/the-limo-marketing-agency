from pathlib import Path
import json
import re

page = Path('case-studies-results.html')
text = page.read_text(encoding='utf-8')
original = text

# --- Metadata: keep the ranking intent, remove unsupported client-result framing.
text = text.replace(
    '<title>Limo Marketing Case Studies & Results | TLMA</title>',
    '<title>Limo Marketing Case Studies, Work & Proof | TLMA</title>'
)
text = text.replace(
    '<meta name="description" content="See selected limo marketing, website, booking-system and Google Ads account examples from The Limo Marketing Agency."/>',
    '<meta name="description" content="Evidence-first limo marketing case study examples, implementation proof, Google Ads account snapshots, booking systems and measurement standards from TLMA."/>'
)
text = text.replace(
    '<meta property="og:title" content="Limo Marketing Case Studies & Results | TLMA"/>',
    '<meta property="og:title" content="Limo Marketing Case Studies, Work & Proof | TLMA"/>'
)
text = text.replace(
    '<meta property="og:description" content="See selected limo marketing, website, booking-system and Google Ads account examples from The Limo Marketing Agency."/>',
    '<meta property="og:description" content="Evidence-first limo marketing case study examples, implementation proof, Google Ads account snapshots, booking systems and measurement standards from TLMA."/>'
)

# --- Structured data: remove named CreativeWork case studies until permission/evidence is VERIFIED.
ld_pattern = re.compile(r'(<script type="application/ld\+json">\s*)(\{.*?\})(\s*</script>)', re.S)
match = ld_pattern.search(text)
if not match:
    raise SystemExit('JSON-LD block not found')

data = json.loads(match.group(2))
graph = data.get('@graph', [])
data['@graph'] = [node for node in graph if node.get('@type') != 'CreativeWork']
for node in data['@graph']:
    if node.get('@type') == 'CollectionPage':
        node['name'] = 'Limo Marketing Case Studies, Work & Proof'
        node['description'] = 'Evidence-first examples of limo marketing work, implementation systems, Google Ads account snapshots and measurement standards, with named client claims held until proof and permission are verified.'

new_ld = json.dumps(data, indent=2, ensure_ascii=False)
text = text[:match.start()] + match.group(1) + new_ld + match.group(3) + text[match.end():]

# --- Hero: authority without unsupported named-client amplification.
text = text.replace('<div class="eyebrow">Real Client Case Studies</div>', '<div class="eyebrow">Evidence-First Work &amp; Proof</div>')
text = text.replace(
    '<h1>Different Limo Businesses. <span>Different Problems. Different Growth Systems.</span></h1>',
    '<h1>Limo Marketing Work &amp; Proof. <span>What We Can Verify, What We Measure, and What We Refuse to Inflate.</span></h1>'
)
text = text.replace(
    '<p>Every client arrived with a different starting point. Some needed an outdated website rebuilt. Some needed stronger organic search architecture and Google Ads. Others needed the booking and operational system behind the website. These stories show what changed for each business without pretending every client had the same problem.</p>',
    '<p>This portfolio separates implementation evidence, live systems, account screenshots and measurement standards from claims that still need client permission or KPI verification. Named client stories are amplified only after the relationship, public-use permission and supporting evidence are recorded.</p>'
)
text = text.replace('>Explore Client Stories</a>', '>Explore Verified Work</a>')
text = text.replace('<strong>4 Client Stories</strong><span>Each discussed separately</span>', '<strong>Evidence First</strong><span>Work is separated from performance claims</span>')
text = text.replace('<strong>Website + SEO + Ads</strong><span>Where those services were delivered</span>', '<strong>Implementation Proof</strong><span>Systems, pages, tracking and account evidence</span>')
text = text.replace('<strong>No Fake KPIs</strong><span>Public proof separated from causation</span>', '<strong>Permission Gated</strong><span>Named stories wait for verified public-use approval</span>')

old_client_index = '''<div class="client-index">
<a class="index-card" href="#nyc-united"><span class="brand-badge sm"></span><div><strong>NYC United Limo</strong><span>Website · SEO · Google Ads</span></div></a>
<a class="index-card" href="#king-queen"><span class="brand-badge sm"></span><div><strong>King &amp; Queen Limo</strong><span>Website · SEO · Google Ads</span></div></a>
<a class="index-card" href="#nyc-executive"><span class="brand-badge sm"></span><div><strong>NYC Executive Limo</strong><span>Website · SEO · Google Ads</span></div></a>
<a class="index-card" href="#nyc-lux"><span class="brand-badge sm"></span><div><strong>NYC Lux Ride</strong><span>Booking · Admin · Automation</span></div></a>
</div>'''
new_client_index = '''<div class="client-index">
<a class="index-card" href="#case-studies"><span class="brand-badge sm"></span><div><strong>Booking &amp; Operations</strong><span>Structured trip, quote and admin workflow evidence</span></div></a>
<a class="index-card" href="#google-ads-performance"><span class="brand-badge sm"></span><div><strong>Google Ads Evidence</strong><span>Anonymized account snapshots and metric definitions</span></div></a>
<a class="index-card" href="seo-for-limo-companies.html"><span class="brand-badge sm"></span><div><strong>SEO Methodology</strong><span>Intent mapping, indexing, architecture and measurement</span></div></a>
<a class="index-card" href="booking-systems.html"><span class="brand-badge sm"></span><div><strong>Booking System Demo</strong><span>Customer journey and operational-system capability</span></div></a>
</div>'''
if old_client_index not in text:
    raise SystemExit('Hero client index block not found')
text = text.replace(old_client_index, new_client_index)
text = text.replace('CLIENT TRANSFORMATION LIBRARY', 'EVIDENCE LIBRARY')
text = text.replace('From Legacy Websites to Connected Growth Systems.', 'From Search Visibility to Booking &amp; Operations.')
text = text.replace('Website Design · SEO · Google Ads · Booking Technology · Operations', 'SEO · Google Ads · Booking Technology · Measurement · Operations')

text = text.replace(
    '<h2>What will these limo marketing case studies show?</h2><p>Each story separates the starting problem, the work delivered, the customer-journey change and current public proof. Review counts and public reputation are shown as context, not automatically claimed as results caused by our work. Where exact campaign KPIs are not available, we do not invent ROAS, revenue or booking-growth percentages.</p>',
    '<h2>What makes a limo marketing case study credible?</h2><p>A credible case study separates the work delivered from the business outcome, identifies where the evidence came from, defines each metric and records permission before attaching a client name to the story. Until those checks are complete, we publish the methodology and implementation evidence without inventing ROAS, revenue, booking growth or testimonials.</p>'
)

# --- Replace the named-client section with a publishable evidence-first portfolio block.
start_marker = '<section class="section soft" id="case-studies">'
end_marker = '<section class="google-ads-proof" id="google-ads-performance">'
start = text.find(start_marker)
end = text.find(end_marker)
if start == -1 or end == -1 or end <= start:
    raise SystemExit('Case-study section markers not found')

replacement = '''<section class="section soft" id="case-studies">
<div class="container">
<div class="section-head"><div><div class="kicker"><span class="dot"></span>PUBLISHABLE PROOF</div><h2>Proof We Can Stand Behind <span>Today.</span></h2></div><p>We publish implementation evidence and measurable systems now, while named client transformations remain permission-gated until the proof ledger is complete.</p></div>
<article class="case-study reveal" id="verified-work">
<div class="case-bar"><div class="case-no"><span class="brand-badge sm"></span><b>EVIDENCE STANDARD · CURRENT</b></div><div class="case-tags"><span class="case-tag">Implementation</span><span class="case-tag">Measurement</span><span class="case-tag">No Unsupported KPIs</span></div></div>
<div class="case-intro">
<div class="case-copy"><div class="kicker"><span class="dot"></span>FROM MARKETING CLAIMS TO VERIFIABLE SYSTEMS</div><h3>What TLMA Can Demonstrate without Inflating the Story</h3><p>Our strongest publishable proof right now is the work itself: booking and admin workflows, search architecture, live measurement, conversion tracking and Google Ads account evidence. Client-attributed growth claims stay off the page until permission and KPI evidence are verified.</p><a class="live-link" href="booking-systems.html">Explore the Booking System Capability →</a></div>
<div class="visual-frame"><div class="browser"><div class="browser-top"><i></i><i></i><i></i><span>TLMA · Evidence-First Growth System</span></div><div style="height:300px;padding:22px;background:linear-gradient(145deg,#f7fbff,#eaf3ff);display:grid;align-content:center;gap:12px"><div style="padding:16px;border-radius:16px;background:#fff;border:1px solid rgba(81,112,254,.12);font-size:12px;font-weight:900">Search → Landing Page → Lead / Booking → Measurement</div><div style="display:grid;grid-template-columns:repeat(3,1fr);gap:9px"><div style="padding:13px;border-radius:13px;background:#fff;font-size:8px">SEO Architecture</div><div style="padding:13px;border-radius:13px;background:#fff;font-size:8px">Booking Workflow</div><div style="padding:13px;border-radius:13px;background:#fff;font-size:8px">GA4 Lead Tracking</div></div><div style="padding:14px;border-radius:15px;background:#112b61;color:#fff;font-size:9px">Evidence before claims. Measurement before optimization.</div></div></div><div class="visual-note">Capability visualization based on systems and measurement implemented in the TLMA project stack.</div></div>
</div>
<div class="case-body">
<div class="story-grid">
<div class="story-card"><span class="brand-badge"></span><h4>Booking &amp; Operations Implementation</h4><p>A verified implementation trail exists for a limo booking project that includes structured trip details, customer booking flow, quote/admin workflow, booking-data persistence and notification logic. The client identity and outcome claims remain permission-gated.</p><div class="story-list"><div><span class="brand-badge sm"></span><div><strong>Structured trip data</strong><span>Ride type, customer details and booking context move through a defined workflow.</span></div></div><div><span class="brand-badge sm"></span><div><strong>Admin-side workflow</strong><span>Quote and operational handling are connected to the customer journey.</span></div></div></div></div>
<div class="story-card dark"><span class="brand-badge"></span><h4>SEO + Measurement System</h4><p>TLMA uses one-intent-per-URL architecture, Search Console indexing tracking, GA4 and success-only lead measurement. That means SEO decisions can be tied to crawl status, queries, landing pages and real form completions instead of rank screenshots alone.</p><div class="story-list"><div><span class="brand-badge sm"></span><div><strong>Search Console</strong><span>Indexing, query visibility and landing-page movement are monitored.</span></div></div><div><span class="brand-badge sm"></span><div><strong>Success-only leads</strong><span>A lead event fires only after a successful form submission reaches the thank-you flow.</span></div></div></div></div>
<div class="story-card"><span class="brand-badge"></span><h4>Google Ads Account Evidence</h4><p>Selected anonymized Google Ads screenshots show real interface metrics such as clicks, impressions, conversions, cost per conversion, conversion rate and configured conversion value. They are evidence of account reporting, not automatic proof of booked revenue.</p><div class="story-list"><div><span class="brand-badge sm"></span><div><strong>Metric definitions matter</strong><span>Conversion actions and assigned values depend on account configuration.</span></div></div><div><span class="brand-badge sm"></span><div><strong>No revenue inflation</strong><span>Conversion value is not called booked revenue unless reconciled with booking/payment data.</span></div></div></div></div>
</div>
<div class="proof-row">
<div class="proof-panel"><h4>Publication Rule</h4><div class="review-snapshot"><div class="stars">✓</div><div><strong>Evidence → Permission → Claim</strong><span>Named client stories and quantified outcomes require a completed proof record before amplification.</span></div><span class="source-pill">TRUST CONTROL</span></div><p>This standard is intentionally stricter than simply showing a screenshot or a public review count. An artifact proves the artifact exists; causation needs separate evidence.</p></div>
</div>
<div class="flow-line"><strong>Evidence Workflow</strong><span>Artifact → Source → Permission → Metric Definition → Approved Claim → Publication</span></div>
</div>
</article>
</div>
</section>
'''
text = text[:start] + replacement + text[end:]

# --- Reframe anonymized Google Ads screenshots conservatively.
text = text.replace('Selected Account Snapshots with <span>Real Reported Metrics.</span>', 'Selected Anonymized Account Snapshots with <span>Reported Metrics.</span>')
text = text.replace(
    'These supplied Google Ads screenshots add paid-search proof to the portfolio. They document click volume, conversions, cost efficiency, conversion rate and conversion-value tracking across selected monthly account views.',
    'These anonymized Google Ads screenshots document interface-level reporting such as click volume, conversions, cost efficiency, conversion rate and configured conversion value. They are presented as account evidence, not as a named-client revenue claim.'
)
text = text.replace(
    'They strengthen the case-study page by showing actual Google Ads interface data rather than relying only on descriptive marketing claims.',
    'They strengthen the proof library by showing Google Ads interface data rather than relying only on descriptive marketing claims. Account identity and client-attributed outcomes are intentionally not asserted here.'
)

# --- Replace the permission-unverified testimonial with the public evidence standard.
testimonial_start = '<section class="section">\n<div class="container">\n<div class="section-head"><div><div class="kicker"><span class="dot"></span>CLIENT TESTIMONIAL'
faq_marker = '<section class="section soft" id="faq">'
ts = text.find(testimonial_start)
fe = text.find(faq_marker)
if ts == -1 or fe == -1 or fe <= ts:
    raise SystemExit('Testimonial section markers not found')

evidence_section = '''<section class="section">
<div class="container">
<div class="section-head"><div><div class="kicker"><span class="dot"></span>EVIDENCE STANDARD</div><h2>What Has to Be True before We Publish a <span>Named Client Result.</span></h2></div><p>Strong proof becomes clearer under scrutiny. Our publication gate is designed to keep implementation evidence, testimonials and business outcomes from being mixed together.</p></div>
<div class="quote-grid">
<article class="quote-card reveal"><div class="quote-mark">✓</div><blockquote>A named case study is publishable only when the relationship, exact work delivered and public-use permission are recorded. A numerical result also needs its source, metric definition, timeframe and comparison basis.</blockquote><div class="client-line"><span class="brand-badge sm"></span><div><strong>TLMA Proof Standard</strong><span>Evidence-first authority control</span></div></div></article>
<aside class="truth-card reveal"><span class="brand-badge"></span><h3>What We Will Not Do</h3><p>We will not turn a live website, public review count, ad screenshot or booking system into a causal growth claim without separate supporting evidence.</p><div class="truth-list"><div class="truth-row"><span class="brand-badge sm"></span><span>No invented ROAS, revenue or booking-growth percentages</span></div><div class="truth-row"><span class="brand-badge sm"></span><span>No client testimonial without recorded permission</span></div><div class="truth-row"><span class="brand-badge sm"></span><span>No conversion value presented as booked revenue without reconciliation</span></div><div class="truth-row"><span class="brand-badge sm"></span><span>No named-client amplification while the proof ledger is HOLD / PARTIAL</span></div></div></aside>
</div>
</div>
</section>
'''
text = text[:ts] + evidence_section + text[fe:]

# --- Keep FAQ and form source labels consistent with the page framing.
text = text.replace('Limo Marketing Case Studies &amp; Client Results', 'Limo Marketing Case Studies, Work &amp; Proof')
text = text.replace('New Website Lead - Limo Marketing Case Studies &amp; Client Results', 'New Website Lead - Limo Marketing Case Studies, Work &amp; Proof')

# --- Safety assertions: the permission-unverified names/testimonial must not remain in public HTML.
blocked = ['NYC United Limo', 'King & Queen Limo', 'NYC Executive Limo', 'NYC Lux Ride']
for name in blocked:
    if name in text:
        raise SystemExit(f'Blocked named-client reference remains: {name}')
if '"@type": "CreativeWork"' in text:
    raise SystemExit('CreativeWork client schema remains')
if 'CLIENT TESTIMONIAL' in text:
    raise SystemExit('Unverified testimonial section remains')
if text.count('<h1') != 1:
    raise SystemExit(f'Expected one H1, found {text.count("<h1")}')

# Re-validate JSON-LD after transformation.
check = ld_pattern.search(text)
json.loads(check.group(2))

if text == original:
    raise SystemExit('No changes made')

page.write_text(text, encoding='utf-8')
print('Authority/proof cleanup applied successfully.')
print('Named client references removed:', ', '.join(blocked))
print('CreativeWork client schema removed.')
print('Evidence-first portfolio section installed.')
