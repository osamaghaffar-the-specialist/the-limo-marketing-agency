from pathlib import Path
import re, json

PATH = Path('booking-systems.html')
ROOT = 'https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/'
PAGE = ROOT + 'booking-systems.html'
ORG = ROOT + '#organization'
WEB = ROOT + '#website'
SERVICE = PAGE + '#service'
WEBPAGE = PAGE + '#webpage'

text = PATH.read_text(encoding='utf-8')
original = text

replacements = {
    '<title>Limo Booking System &amp; Automation | The Limo Marketing Agency</title>': '<title>Limo Booking Software &amp; System | The Limo Marketing Agency</title>',
    '<meta property="og:title" content="Limo Booking System &amp; Automation | The Limo Marketing Agency"/>': '<meta property="og:title" content="Limo Booking Software &amp; System | The Limo Marketing Agency"/>',
    '<meta content="Automated limo booking systems with live pricing, card payments, booking confirmation and connected admin operations for limo and black-car companies." name="description"/>': '<meta content="Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies." name="description"/>',
    '<meta property="og:description" content="Automated limo booking systems with live pricing, card payments, booking confirmation and connected admin operations for limo and black-car companies."/>': '<meta property="og:description" content="Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies."/>',
    '<div class="eyebrow"><span class="dot"></span>2026 Automated Booking Systems</div>': '<div class="eyebrow"><span class="dot"></span>Limo Booking Software &amp; Automation</div>',
    '<h1>From Website Visit to <span>Paid Booking.</span> Automatically.</h1>': '<h1>Limo Booking Software That Turns Website Visits into <span>Paid Bookings.</span></h1>',
    '<p>Modern limo customers should not have to submit a form and wait for someone to calculate a price. Your booking system can collect the trip, apply your pricing rules, show the total, take card payment, confirm the reservation and update your Admin Portal in one connected journey.</p>': '<p>Modern limo customers should not have to submit a form and wait for someone to calculate a price. Our limo booking software can collect the trip, apply your pricing rules, show the total, take card payment, confirm the reservation and update your Admin Portal in one connected journey.</p>',
}

for old, new in replacements.items():
    if old not in text:
        raise SystemExit(f'ERROR: expected source string not found: {old[:90]}')
    text = text.replace(old, new, 1)

# Normalize the existing JSON-LD graph for commercial booking-software intent.
ld_re = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)
matches = list(ld_re.finditer(text))
if not matches:
    raise SystemExit('ERROR: booking page JSON-LD block not found')

changed_schema = False

def rewrite(match):
    global changed_schema
    try:
        data = json.loads(match.group(1))
    except json.JSONDecodeError:
        return match.group(0)
    graph = data.get('@graph') if isinstance(data, dict) else None
    if not isinstance(graph, list):
        return match.group(0)
    booking_graph = any(isinstance(n, dict) and n.get('@type') == 'Service' and 'booking' in str(n.get('serviceType','')).lower() for n in graph)
    if not booking_graph:
        return match.group(0)

    service_node = None
    for n in graph:
        if isinstance(n, dict) and n.get('@type') == 'Service' and 'booking' in str(n.get('serviceType','')).lower():
            service_node = n
            break
    if service_node is None:
        raise SystemExit('ERROR: booking Service node missing')

    service_node['@id'] = SERVICE
    service_node['name'] = 'Limo Booking Software and System'
    service_node['serviceType'] = 'Custom limo booking software and automated booking system development'
    service_node['provider'] = {'@id': ORG}
    service_node['description'] = 'Custom limo booking software and booking systems with live pricing, online payments, booking confirmations and connected admin workflows for limo and black car companies.'

    if not any(isinstance(n, dict) and n.get('@type') == 'WebPage' and n.get('@id') == WEBPAGE for n in graph):
        # Insert before FAQPage when possible so page entity precedes supplemental FAQ data.
        page_node = {
            '@type': 'WebPage',
            '@id': WEBPAGE,
            'url': PAGE,
            'name': 'Limo Booking Software & System',
            'description': 'Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies.',
            'isPartOf': {'@id': WEB},
            'about': {'@id': SERVICE},
            'inLanguage': 'en'
        }
        idx = next((i for i,n in enumerate(graph) if isinstance(n,dict) and n.get('@type') == 'FAQPage'), len(graph))
        graph.insert(idx, page_node)
    else:
        for n in graph:
            if isinstance(n, dict) and n.get('@type') == 'WebPage' and n.get('@id') == WEBPAGE:
                n.update({
                    'url': PAGE,
                    'name': 'Limo Booking Software & System',
                    'description': 'Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies.',
                    'isPartOf': {'@id': WEB},
                    'about': {'@id': SERVICE},
                    'inLanguage': 'en'
                })
    changed_schema = True
    return '<script type="application/ld+json">\n' + json.dumps(data, indent=2, ensure_ascii=False) + '\n</script>'

text = ld_re.sub(rewrite, text)
if not changed_schema:
    raise SystemExit('ERROR: booking JSON-LD graph was not updated')

# Strict validation.
checks = [
    '<title>Limo Booking Software &amp; System | The Limo Marketing Agency</title>',
    'Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows',
    'Limo Booking Software That Turns Website Visits into <span>Paid Bookings.</span>',
    '"@type": "WebPage"',
    f'"@id": "{WEBPAGE}"',
    f'"about": {{\n        "@id": "{SERVICE}"',
    f'"isPartOf": {{\n        "@id": "{WEB}"',
]
for c in checks:
    if c not in text:
        raise SystemExit(f'ERROR: validation signal missing: {c}')
if text.count('<h1') != 1:
    raise SystemExit(f'ERROR: expected exactly one H1, found {text.count("<h1")}')
if '<link rel="canonical" href="' + PAGE + '"/>' not in text:
    raise SystemExit('ERROR: canonical changed or missing')
if text == original:
    raise SystemExit('ERROR: no changes produced')

PATH.write_text(text, encoding='utf-8')
print('P1 booking intent optimization PASS')
print('Title: Limo Booking Software & System | The Limo Marketing Agency')
print('Primary intent: limo booking software + limo booking system')
print('WebPage schema: present and linked to Service/WebSite')
