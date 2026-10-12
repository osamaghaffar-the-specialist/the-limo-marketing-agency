from pathlib import Path

PAGE = Path('booking-systems.html')
text = PAGE.read_text(encoding='utf-8')


def replace_exact(old, new, expected=1):
    global text
    count = text.count(old)
    if count != expected:
        raise SystemExit(f'Expected {expected} occurrence(s), found {count}: {old[:120]}')
    text = text.replace(old, new)

# Search intent ownership: booking + reservation software, without claiming dispatch features.
replace_exact(
    '<meta content="Custom limo booking software with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies." name="description"/>',
    '<meta content="Custom limo booking and reservation software with live pricing, online payments, confirmations and Admin Portal workflows for limo and chauffeur companies." name="description"/>'
)
replace_exact(
    '<meta property="og:title" content="Limo Booking Software &amp; System | The Limo Marketing Agency"/>',
    '<meta property="og:title" content="Limo Booking &amp; Reservation Software | Chauffeur Companies"/>'
)
replace_exact(
    '<meta property="og:description" content="Custom limo booking software with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies."/>',
    '<meta property="og:description" content="Custom limo booking and reservation software with live pricing, online payments, confirmations and Admin Portal workflows for limo and chauffeur companies."/>'
)
replace_exact(
    '<title>Limo Booking Software &amp; System | The Limo Marketing Agency</title>',
    '<title>Limo Booking &amp; Reservation Software | Chauffeur Companies</title>'
)

# Structured data: align the real service entity with the same commercial intent.
replace_exact('"name": "Limo Booking Software and System",', '"name": "Limo Booking and Reservation Software",')
replace_exact(
    '"serviceType": "Custom limo booking software and automated booking system development",',
    '"serviceType": "Custom limo booking software, reservation system and booking automation development",'
)
replace_exact(
    '"description": "Custom limo booking software and booking systems with live pricing, online payments, booking confirmations and connected admin workflows for limo and black car companies.",',
    '"description": "Custom limo booking and reservation software with live pricing, online payments, booking confirmations and connected Admin Portal workflows for limo and chauffeur companies.",'
)
replace_exact('"name": "Limo Booking Software & System",', '"name": "Limo Booking and Reservation Software",')
replace_exact(
    '"description": "Custom limo booking software and booking systems with live pricing, online payments, confirmations and connected admin workflows for limo and black car companies.",',
    '"description": "Custom limo booking and reservation software with live pricing, online payments, confirmations and connected Admin Portal workflows for limo and chauffeur companies.",'
)

# Add a direct, useful definition to FAQ schema before the existing FAQs.
old_schema_start = '''      "mainEntity": [
        {
          "@type": "Question",
          "name": "Is this just a booking form?",'''
new_schema_start = '''      "mainEntity": [
        {
          "@type": "Question",
          "name": "What is limo booking and reservation software?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Limo booking and reservation software is a connected system that lets customers enter trip details, apply configured pricing, choose a vehicle, pay online and create a booking record for the operator's Admin Portal."
          }
        },
        {
          "@type": "Question",
          "name": "Is this just a booking form?",'''
replace_exact(old_schema_start, new_schema_start)

# Hero: preserve conversion framing while making the page owner explicit.
replace_exact(
    '<div class="eyebrow"><span class="dot"></span>Limo Booking Software &amp; Automation</div>',
    '<div class="eyebrow"><span class="dot"></span>Limo Booking &amp; Reservation Software</div>'
)
replace_exact(
    '<h1>Limo Booking Software That Turns Website Visits into <span>Paid Bookings.</span></h1>',
    '<h1>Limo Booking &amp; Reservation Software That Turns Website Visits into <span>Paid Bookings.</span></h1>'
)
replace_exact(
    '<p>Modern limo customers should not have to submit a form and wait for someone to calculate a price. Our limo booking software can collect the trip, apply your pricing rules, show the total, take card payment, confirm the reservation and update your Admin Portal in one connected journey.</p>',
    '<p>Modern limo customers should not have to submit a form and wait for someone to calculate a price. Our limo booking and reservation software can collect the trip, apply your pricing rules, show the total, take card payment, confirm the reservation and update your Admin Portal in one connected journey.</p>'
)

# Visible FAQ definition mirrors the schema answer and adds value for operators.
replace_exact(
    '<div class="faq-list reveal">\n<details class="faq" open=""><summary>Is this just a booking form?</summary>',
    '<div class="faq-list reveal">\n<details class="faq" open=""><summary>What is limo booking and reservation software?</summary><div class="answer">Limo booking and reservation software is a connected system that lets customers enter trip details, apply configured pricing, choose a vehicle, pay online and create a booking record for the operator\'s Admin Portal.</div></details>\n<details class="faq"><summary>Is this just a booking form?</summary>'
)

PAGE.write_text(text, encoding='utf-8')

Path('docs/seo-booking-reservation-owner-2026-10-12.md').write_text('''# Booking + Reservation Software Ownership Sprint — 2026-10-12

## Evidence

Google Search Console was settled through 2026-10-09 at analysis time.

- `/booking-systems.html` is indexed.
- The page recorded one impression at average position 8 on 2026-10-02.
- GSC did not expose the query text for that impression, so no hidden/anonymized query was guessed.
- Existing keyword research shows meaningful commercial demand around `limo booking software`, `limo reservation software`, `limo booking system` and related chauffeur software terms.
- Current 2026 SERP review shows product/service pages consistently framing the category around online booking, reservations, pricing, payments and connected operational/admin workflows.

## Decision

Own the truthful `limo booking + reservation software` intent on the existing indexed URL. Do not add `dispatch software` to the page because the current production page does not promise a dispatch board, driver assignment or live GPS dispatch feature set.

## Changes

- Title and Open Graph title aligned to Limo Booking & Reservation Software.
- Meta description aligned to booking/reservation software for limo and chauffeur companies.
- Service and WebPage schema names/descriptions aligned to the same intent.
- Hero eyebrow, H1 and intro aligned without changing the existing conversion proposition.
- Added one concise visible FAQ and matching FAQ schema definition for limo booking/reservation software.

## Guardrails

- No new production URL.
- No sitemap, robots or canonical change.
- No city/location pages.
- No dispatch claims.
- No fake reviews, metrics, integrations or performance guarantees.
- Measure future impact in GSC after Google recrawls the page.
''', encoding='utf-8')

# Remove one-time patch machinery so it cannot ship in the PR diff.
Path('scripts/seo_booking_reservation_owner_once.py').unlink(missing_ok=True)
Path('.github/workflows/seo-booking-reservation-owner-once.yml').unlink(missing_ok=True)
