from pathlib import Path
import json, re, sys

PATH = Path('seo-for-limo-companies.html')
text = PATH.read_text(encoding='utf-8')

TITLE = '<title>Limo SEO Services | SEO for Limo Companies</title>'
CANONICAL = '<link rel="canonical" href="https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/seo-for-limo-companies.html"/>'
MARKER = '<!-- SEO RANKING BRIEF ADDITIONS: 2026-10-10 -->'
ANCHOR = '<section class="section soft" id="services">'

if MARKER in text:
    print('Already applied; nothing to do.')
    sys.exit(0)
if text.count(ANCHOR) != 1:
    raise SystemExit(f'Expected exactly one services anchor, found {text.count(ANCHOR)}')
if TITLE not in text or CANONICAL not in text:
    raise SystemExit('Title/canonical prerequisite mismatch; aborting.')

css = r'''
/* SEO ranking brief additions */
.seo-brief-shell{padding:30px;border:1px solid var(--line);border-radius:28px;background:#fff;box-shadow:var(--shadow)}
.seo-brief-intro{display:grid;grid-template-columns:1fr minmax(300px,.72fr);gap:28px;align-items:start;margin-bottom:24px}
.seo-brief-intro h2{margin:12px 0 10px;font-size:clamp(34px,4vw,50px);line-height:1;letter-spacing:-.045em}.seo-brief-intro p{margin:0;color:var(--muted);font-size:13px;line-height:1.72}
.opportunity-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.opportunity-card{padding:19px;border:1px solid var(--line);border-radius:19px;background:#fbfdff;min-height:190px}.opportunity-card h3{margin:12px 0 7px;font-size:17px}.opportunity-card p{margin:0;color:var(--muted);font-size:11px;line-height:1.62}.opportunity-card ul{margin:12px 0 0;padding-left:18px;color:#65738a;font-size:10px;line-height:1.65}
.audit-decision-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(340px,.92fr);gap:14px}.audit-first,.decision-panel{padding:24px;border-radius:25px;border:1px solid var(--line);background:#fff;box-shadow:0 16px 46px rgba(18,35,78,.06)}.audit-first h2,.decision-panel h2{margin:12px 0 9px;font-size:28px;letter-spacing:-.035em}.audit-first>p,.decision-panel>p{margin:0 0 18px;color:var(--muted);font-size:12px;line-height:1.68}
.audit-check-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}.audit-check{padding:13px;border:1px solid var(--line);border-radius:14px;background:#fbfdff}.audit-check strong{display:block;font-size:10px}.audit-check span{display:block;margin-top:4px;color:#7e8ba0;font-size:9px;line-height:1.45}
.channel-table{width:100%;border-collapse:separate;border-spacing:0;overflow:hidden;border:1px solid var(--line);border-radius:16px;font-size:10px}.channel-table th,.channel-table td{padding:11px 10px;text-align:left;vertical-align:top;border-bottom:1px solid var(--line)}.channel-table th{background:#f5f8ff;font-size:9px;text-transform:uppercase;letter-spacing:.08em}.channel-table tr:last-child td{border-bottom:0}.channel-table a{color:var(--blue);font-weight:850}
.answer-mini-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:11px;margin-top:16px}.answer-mini{padding:16px;border-radius:17px;background:#0f224d;color:#fff}.answer-mini h3{margin:0 0 7px;font-size:14px}.answer-mini p{margin:0;color:#c4d3eb;font-size:10px;line-height:1.55}
.trust-note{margin-top:14px;padding:17px 19px;border-radius:18px;border:1px solid rgba(81,112,254,.15);background:linear-gradient(135deg,#f5f8ff,#fff)}.trust-note strong{display:block;font-size:12px}.trust-note p{margin:6px 0 0;color:#63728a;font-size:10.5px;line-height:1.6}
@media(max-width:900px){.seo-brief-intro,.audit-decision-grid{grid-template-columns:1fr}.opportunity-grid,.answer-mini-grid{grid-template-columns:1fr 1fr}.audit-check-grid{grid-template-columns:1fr}}
@media(max-width:620px){.seo-brief-shell{padding:20px}.opportunity-grid,.answer-mini-grid{grid-template-columns:1fr}.channel-table{display:block;overflow-x:auto;white-space:normal}}
'''

if text.count('</style>') < 1:
    raise SystemExit('No closing style tag found.')
text = text.replace('</style>', css + '\n</style>', 1)

block = r'''
<!-- SEO RANKING BRIEF ADDITIONS: 2026-10-10 -->
<section class="section soft" id="seo-opportunity-map">
<div class="container">
<div class="seo-brief-shell">
<div class="seo-brief-intro">
<div><div class="kicker"><span class="dot"></span>OPERATOR SEO PRIORITIES</div><h2>What Should a Limo Company <span>Optimize First?</span></h2><p><strong>Start with crawlability and indexability, then make the core service and local intent easy to understand.</strong> For most limo operators, that means checking technical access, Google Business Profile relevance, high-value service pages, airport or route pages that reflect real coverage, internal links and conversion tracking before expanding content.</p></div>
<p>SEO works best when the site mirrors how customers actually search. A useful structure usually separates the core service offer from airport, route, corporate, hourly and event demand instead of forcing every intent onto one homepage.</p>
</div>
<div class="opportunity-grid">
<article class="opportunity-card"><span aria-hidden="true" class="brand-badge sm"></span><h3>Core Service Pages</h3><p>Give major commercial services a clear owner page with one primary purpose.</p><ul><li>Airport transportation</li><li>Corporate / executive service</li><li>Point-to-point</li><li>Hourly chauffeur</li></ul></article>
<article class="opportunity-card"><span aria-hidden="true" class="brand-badge sm"></span><h3>Airport &amp; Route Demand</h3><p>Build airport or route pages only where the operator genuinely serves the trip and can add useful, distinct customer information.</p><ul><li>Airport-specific pickup details</li><li>Real destination / route coverage</li><li>Vehicle and booking context</li><li>No mass doorway pages</li></ul></article>
<article class="opportunity-card"><span aria-hidden="true" class="brand-badge sm"></span><h3>Local &amp; Market Relevance</h3><p>Match local content to actual service areas, not a generated list of cities.</p><ul><li>Google Business Profile alignment</li><li>Accurate service areas</li><li>Distinct local value</li><li>Consistent business information</li></ul></article>
<article class="opportunity-card"><span aria-hidden="true" class="brand-badge sm"></span><h3>Commercial Supporting Content</h3><p>Answer real buying questions that help customers choose the right service or booking path.</p><ul><li>Airport transfer guidance</li><li>Corporate travel questions</li><li>Vehicle / luggage fit</li><li>Booking and cancellation guidance</li></ul></article>
<article class="opportunity-card"><span aria-hidden="true" class="brand-badge sm"></span><h3>Internal Linking</h3><p>Connect related service, airport, route and resource pages so users and search systems can understand the hierarchy.</p><ul><li>Descriptive anchor text</li><li>Relevant parent / child links</li><li>No orphan money pages</li><li>Clear booking path</li></ul></article>
<article class="opportunity-card"><span aria-hidden="true" class="brand-badge sm"></span><h3>Measurement</h3><p>Organic traffic is useful only when the business can see what happens next.</p><ul><li>Search Console visibility</li><li>GA4 / GTM events</li><li>Calls and quote requests</li><li>Booking-path actions</li></ul></article>
</div>
<div class="answer-mini-grid">
<article class="answer-mini"><h3>Does a limo company need city pages?</h3><p>Only when the company genuinely serves the market and the page can provide distinct, useful customer information. Repeating the same page across dozens of cities creates weak content and can blur page ownership.</p></article>
<article class="answer-mini"><h3>Can SEO help airport-transfer demand?</h3><p>Yes, when the operator truly serves the airport or route and the page answers the trip with useful service, pickup, vehicle and booking information rather than generic location text.</p></article>
<article class="answer-mini"><h3>SEO or Google Ads?</h3><p>Google Ads can capture paid demand quickly; SEO builds organic and local visibility over time. Many operators can use both around the same high-value service intent while measuring each channel separately.</p></article>
</div>
</div>
</div>
</section>
<section class="section" id="seo-audit-decision">
<div class="container">
<div class="audit-decision-grid">
<article class="audit-first"><div class="kicker"><span class="dot"></span>WHAT WE AUDIT FIRST</div><h2>Find the Constraint Before Adding More Pages.</h2><p>Our first pass checks whether Google can access the site, whether each important query has one clear owner page and whether organic visits have a measurable path toward a call, quote or booking.</p><div class="audit-check-grid">
<div class="audit-check"><strong>Crawl &amp; Indexing</strong><span>Robots, indexability, canonicals, sitemap coverage and duplicate variants.</span></div>
<div class="audit-check"><strong>Page Ownership</strong><span>Keyword-to-URL mapping, cannibalization and intent conflicts.</span></div>
<div class="audit-check"><strong>On-Page Alignment</strong><span>Title, H1, headings, content purpose and internal anchors.</span></div>
<div class="audit-check"><strong>Local Relevance</strong><span>Google Business Profile, service areas and real market coverage.</span></div>
<div class="audit-check"><strong>Technical Experience</strong><span>Core Web Vitals, mobile usability, image weight and rendering issues.</span></div>
<div class="audit-check"><strong>Entity &amp; Schema Clarity</strong><span>Organization, service, page and breadcrumb relationships where appropriate.</span></div>
<div class="audit-check"><strong>Conversion Readiness</strong><span>Calls, forms, quote requests, booking actions and analytics setup.</span></div>
<div class="audit-check"><strong>Content Gaps</strong><span>Missing service, airport, route or buyer-help content supported by real demand.</span></div>
</div></article>
<article class="decision-panel"><div class="kicker"><span class="dot"></span>CHANNEL DECISION</div><h2>SEO vs Ads vs GEO</h2><p>These channels solve different parts of the search journey. Clear ownership helps avoid turning every page into a mixed-intent landing page.</p><table class="channel-table"><thead><tr><th>Channel</th><th>Best use</th><th>Time horizon</th><th>TLMA owner</th></tr></thead><tbody>
<tr><td><strong>SEO</strong></td><td>Organic and local visibility for service, airport, route and market intent.</td><td>Builds over time; no fixed ranking timeline.</td><td><strong>This page</strong></td></tr>
<tr><td><strong>Google Ads</strong></td><td>Paid capture of high-intent searches with measurable conversion paths.</td><td>Can launch quickly; performance depends on market, offer and account quality.</td><td><a href="google-ads-for-limo-companies.html">Google Ads for Limo Companies</a></td></tr>
<tr><td><strong>GEO / AI Search</strong></td><td>Clear entity, service and evidence signals that answer systems can retrieve and understand.</td><td>Ongoing; no AI citation guarantee.</td><td><a href="geo-ai-search-optimization.html">GEO &amp; AI Search</a></td></tr>
</tbody></table>
<div class="trust-note"><strong>What SEO cannot guarantee</strong><p>No ethical SEO provider can guarantee a #1 ranking, a fixed ranking date or an AI citation. The objective is to improve technical accessibility, relevance, evidence, authority and conversion paths around commercially useful searches—and measure the resulting visibility and actions.</p></div>
</article>
</div>
</div>
</section>
'''

text = text.replace(ANCHOR, block + '\n' + ANCHOR, 1)

# Guardrails
if text.count(MARKER) != 1:
    raise SystemExit('Marker count failed.')
if TITLE not in text or CANONICAL not in text:
    raise SystemExit('Title/canonical changed unexpectedly.')
if len(re.findall(r'<h1\b', text, flags=re.I)) != 1:
    raise SystemExit('H1 count changed unexpectedly.')
if 'href="google-ads-for-limo-companies.html"' not in text or 'href="geo-ai-search-optimization.html"' not in text:
    raise SystemExit('Required internal links missing.')

for raw in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', text, flags=re.I|re.S):
    json.loads(raw)

PATH.write_text(text, encoding='utf-8')
print('Applied SEO ranking brief additions successfully.')
print('H1 count:', len(re.findall(r'<h1\b', text, flags=re.I)))
print('Marker count:', text.count(MARKER))
