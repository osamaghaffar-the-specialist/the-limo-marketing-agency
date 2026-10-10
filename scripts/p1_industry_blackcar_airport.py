from pathlib import Path


def replace_once(text, old, new, label):
    if old not in text:
        raise SystemExit(f'MISSING {label}: {old[:120]}')
    return text.replace(old, new, 1)

# BLACK CAR
p = Path('black-car-services.html')
text = p.read_text(encoding='utf-8')
repls = [
    ('<title>Black Car Marketing Services | The Limo Marketing Agency</title>', '<title>Marketing for Black Car Services | Growth &amp; Booking Strategy</title>', 'black title'),
    ('<meta content="Google Ads, SEO, GEO, website design and booking systems for black car services seeking more airport, corporate and local ride bookings." name="description"/>', '<meta content="Marketing for black car services focused on airport, corporate, local and point-to-point demand using Google Ads, SEO, GEO, mobile-first websites and booking systems." name="description"/>', 'black meta'),
    ('<meta property="og:title" content="Black Car Marketing Services | The Limo Marketing Agency"/>', '<meta property="og:title" content="Marketing for Black Car Services | Growth &amp; Booking Strategy"/>', 'black og title'),
    ('<meta property="og:description" content="Google Ads, SEO, GEO, website design and booking systems for black car services seeking more airport, corporate and local ride bookings."/>', '<meta property="og:description" content="Marketing for black car services focused on airport, corporate, local and point-to-point demand using Google Ads, SEO, GEO, mobile-first websites and booking systems."/>', 'black og desc'),
    ('"name": "Marketing for Black Car Services",', '"name": "Growth and Marketing for Black Car Services",', 'black webpage name'),
    ('          "name": "Airport Black Car Marketing"\n        },\n        {\n          "@type": "Thing",\n          "name": "Business Transportation Marketing"', '          "name": "Airport Black Car Services"\n        },\n        {\n          "@type": "Thing",\n          "name": "Corporate Black Car Services"', 'black about entities'),
    ('      ],\n      "description": "A dedicated industry page for black car services covering local search, airport demand, point-to-point trips, Google Ads, SEO, GEO, websites and booking systems.",', '      ],\n      "mentions": [\n        {\n          "@type": "Thing",\n          "name": "Google Ads for Black Car Services"\n        },\n        {\n          "@type": "Thing",\n          "name": "Search Engine Optimization for Black Car Services"\n        },\n        {\n          "@type": "Thing",\n          "name": "Generative Engine Optimization for Black Car Services"\n        },\n        {\n          "@type": "Thing",\n          "name": "Black Car Website Design"\n        },\n        {\n          "@type": "Thing",\n          "name": "Black Car Booking Systems"\n        }\n      ],\n      "description": "A dedicated industry page for black car services covering local search, airport demand, point-to-point trips, Google Ads, SEO, GEO, websites and booking systems.",', 'black mentions'),
    ('<h1>Turn Local and Airport Search Demand into <span>Booked Black Car Rides.</span></h1>', '<h1>Marketing for Black Car Services Built to Turn <span>Search Demand into Booked Rides.</span></h1>', 'black h1'),
    ('<h2>What does a black car service need from its marketing?</h2>\n<p>A black car service needs to capture high-intent local and airport demand, explain its service area and vehicle options clearly, build trust quickly on mobile and move the customer into a fast booking or inquiry path. Google Ads, SEO, GEO, local search, route pages and conversion tracking should all support that same customer journey.</p>', '<h2>What is marketing for black car services?</h2>\n<p><strong>Marketing for black car services is the system used to capture high-intent airport, local, corporate and point-to-point demand and move those searches into measurable ride inquiries or bookings.</strong> It combines search visibility, route and service-area relevance, mobile-first trust, fleet clarity, conversion tracking and a fast booking path so customers can confirm that the operator serves the trip they need without unnecessary friction.</p>', 'black answer'),
]
for old, new, label in repls:
    text = replace_once(text, old, new, label)
p.write_text(text, encoding='utf-8')

# AIRPORT TRANSPORTATION
p = Path('airport-transportation-companies.html')
text = p.read_text(encoding='utf-8')
repls = [
    ('<title>Airport Transportation Marketing | The Limo Marketing Agency</title>', '<title>Airport Transportation Marketing | Growth &amp; Booking Strategy</title>', 'airport title'),
    ('<meta name="description" content="Google Ads, SEO, GEO, websites and booking systems for airport transportation companies seeking more qualified transfer and corporate bookings."/>', '<meta name="description" content="Airport transportation marketing focused on airport, route, corporate and transfer demand using Google Ads, SEO, GEO, mobile-first websites and booking systems."/>', 'airport meta'),
    ('<meta property="og:title" content="Airport Transportation Marketing | The Limo Marketing Agency"/>', '<meta property="og:title" content="Airport Transportation Marketing | Growth &amp; Booking Strategy"/>', 'airport og title'),
    ('<meta property="og:description" content="Google Ads, SEO, GEO, websites and booking systems for airport transportation companies seeking more qualified transfer and corporate bookings."/>', '<meta property="og:description" content="Airport transportation marketing focused on airport, route, corporate and transfer demand using Google Ads, SEO, GEO, mobile-first websites and booking systems."/>', 'airport og desc'),
    ('"name": "Marketing for Airport Transportation Companies",', '"name": "Growth and Marketing for Airport Transportation Companies",', 'airport webpage name'),
    ('          "name": "Airport Transfer Marketing"\n        },\n        {\n          "@type": "Thing",\n          "name": "Airport Booking Systems"', '          "name": "Airport Transfer Services"\n        },\n        {\n          "@type": "Thing",\n          "name": "Corporate Airport Transportation"', 'airport about entities'),
    ('      ],\n      "description": "A dedicated industry page for airport transportation companies covering airport search demand, route pages, Google Ads, SEO, GEO, websites and booking systems.",', '      ],\n      "mentions": [\n        {\n          "@type": "Thing",\n          "name": "Google Ads for Airport Transportation Companies"\n        },\n        {\n          "@type": "Thing",\n          "name": "Search Engine Optimization for Airport Transportation Companies"\n        },\n        {\n          "@type": "Thing",\n          "name": "Generative Engine Optimization for Airport Transportation Companies"\n        },\n        {\n          "@type": "Thing",\n          "name": "Airport Transportation Website Design"\n        },\n        {\n          "@type": "Thing",\n          "name": "Airport Transportation Booking Systems"\n        }\n      ],\n      "description": "A dedicated industry page for airport transportation companies covering airport search demand, route pages, Google Ads, SEO, GEO, websites and booking systems.",', 'airport mentions'),
    ('<h1>Own the Airport Search. Build Trust. Make the <span>Transfer Easy to Book.</span></h1>', '<h1>Airport Transportation Marketing Built Around <span>Search, Trust and Booking.</span></h1>', 'airport h1'),
    ('<h2>What does an airport transportation company need from its marketing?</h2>\n<p>An airport transportation company needs strong visibility for airport and route searches, clear pickup and service information, a mobile-first website, vehicle and luggage guidance, reliable customer trust signals and a booking journey that captures the trip details the operator actually needs. Google Ads, SEO, GEO and booking technology should all support that same transfer experience.</p>', '<h2>What is airport transportation marketing?</h2>\n<p><strong>Airport transportation marketing is the system used to capture airport, route, corporate and transfer demand and turn it into measurable inquiries or bookings.</strong> It combines search visibility, airport and route relevance, pickup clarity, mobile-first trust, fleet and luggage guidance, conversion tracking and a booking journey that preserves the flight, pickup and destination details the operator actually needs.</p>', 'airport answer'),
]
for old, new, label in repls:
    text = replace_once(text, old, new, label)
p.write_text(text, encoding='utf-8')

print('P1_BLACKCAR_AIRPORT_PASS')
