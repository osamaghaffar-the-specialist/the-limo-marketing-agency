# TLMA SEO Operating Baseline — 2026-10-13

Purpose: preserve a dated measurement baseline after the Authority & Proof Sprint so future ranking, indexing, authority and lead changes can be compared against a fixed state instead of memory.

## Search Console baseline

Property:
`https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/`

Settled GSC window: 2026-09-13 through 2026-10-10.

- Clicks: 0
- Impressions: 117
- CTR: 0%
- Average position: 59.79
- Branded impressions: 0
- Non-branded impressions: 117
- Named-query rows scanned: 18
- Named-query position distribution: 100% of measured impressions currently in position 21+
- Search Console also reports 18 anonymized impressions; the underlying queries are not exposed and must not be guessed.

## Topic-cluster baseline

| Cluster | Impressions | Avg position | Matched queries | Clicks |
|---|---:|---:|---:|---:|
| Core Limo Marketing | 5 | 33.80 | 2 | 0 |
| Limo Google Ads | 28 | 66.89 | 2 | 0 |
| Limo SEO | 44 | 67.36 | 5 | 0 |
| Limo Website & Booking | 6 | 82.33 | 2 | 0 |
| Unclustered | 16 | 85.69 | 7 | 0 |

Interpretation: Google is already testing the site against the correct commercial themes, but authority, indexing depth, brand demand and competitive strength remain the primary constraints.

## Indexing baseline

Tracked URLs: 21

- Submitted and indexed: 8
- URL is unknown to Google: 13
- Active warnings: 0
- Lost pages: 0
- Warning-free rate: 100%
- Indexing health score: 50

Newly indexed on 2026-10-13:
- `/case-studies-results.html`

Do not repeatedly inspect the 13 never-crawled URLs. The indexing tracker and normal discovery should be allowed to work unless a warning appears or a high-value page materially changes.

## GA4 baseline

GA4 property: `The Limo Marketing Agency`

Fresh collection check, 2026-10-11 through 2026-10-13:

- Sessions: 1
- Active users: 1
- Engagement rate: 100%
- Event count in key-event segmentation read: 14
- Key events: 0
- Channel: Organic Search
- Source / medium: google / organic
- Country: United States
- Device: desktop
- AI-assistant referral sessions: 0

Current GA4 key-event names exposed by the property:
- `close_convert_lead`
- `purchase`
- `qualify_lead`

`generate_lead` is implemented on the thank-you page but has not yet appeared in GA4 reporting. Do not generate a fake production lead solely to populate analytics.

## Lead-measurement implementation state

The website's form flow records successful submission state before redirecting to the thank-you page. The thank-you page checks that state before emitting `generate_lead`, preventing a direct visit to the thank-you URL from being counted as a confirmed lead.

Publication / QA rule:
- Test actual lead tracking only with a clearly documented QA submission or a genuine lead.
- Do not count a dataLayer push as a GA4 conversion unless GA4 actually receives the event.
- Once `generate_lead` appears in GA4, verify it and mark it as a key event through an authorized GA4 admin action.

## Authority state

Editorial outreach sent: 4

- Chauffeur Driven
- PHTM
- TaxiPoint
- Professional Driver

Reply check on 2026-10-13: no replies from those four publishers yet.

Do not send immediate duplicate follow-ups. Follow-up should provide a useful additional angle and respect a reasonable editorial response window.

## Trust / proof controls now live

- Public case-study page converted to evidence-first positioning.
- Permission-unverified named-client amplification removed.
- Named-client CreativeWork schema removed until verification is complete.
- Homepage dashboard metrics explicitly labeled illustrative.
- `Verified Capability Proof Pack` recorded internally.
- `Brand Authority Prospect Map` recorded internally.

## Homepage image-alt QA

The live crawler reports six images as missing alt text because it treats empty alt values as missing. Source QA confirmed:

- total img tags: 21
- missing alt attributes: 0
- empty alt values: 6
- all six empty-alt images are explicitly `aria-hidden="true"` decorative assets

No SEO keyword text should be forced into those decorative images. The current markup is intentional.

## Release gates

### New production content
Keep the normal new-page release gate closed while 13 tracked URLs remain unknown to Google, unless a concrete editorial/link opportunity justifies a specific asset.

### UK dispatch pricing page
Do not merge the pre-release page until:
- vendor pricing is freshly reverified;
- indexing/discovery is healthier or a real authority opportunity justifies release;
- noindex/pre-release banner/sitemap/internal-link release steps are performed as one controlled launch.

### Verified case study
Do not publish a named transformation until the client-proof ledger has:
- relationship evidence;
- exact scope;
- written public-use permission;
- screenshot/logo permission where applicable;
- metric source, definition and date range;
- approved claim wording.

## Next measurement checkpoints

Compare future performance against this baseline using:
- indexed URL count;
- branded impressions and branded queries;
- non-branded impressions;
- page-one / top-20 query count;
- cluster impressions and positions;
- editorial mentions / referring domains;
- organic GA4 sessions;
- `generate_lead` events;
- qualified consultation requests.

Rankings remain a diagnostic metric. Qualified leads and booked business are the commercial outcomes.
