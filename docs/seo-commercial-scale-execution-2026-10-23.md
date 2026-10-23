# TLMA — Commercial SEO Scale Sprint: Execution & Proof Gates

**Audit date:** 2026-10-23  
**Status:** INTERNAL WORKING DOCUMENT — first safe changes implemented on a PR branch, not evidence of ranking growth.  
**Site:** https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/  
**Business north star:** *qualified US/UK limo/chauffeur/black-car operators requesting a consultation; followed by a real sales discussion or a paying client.*  
**Recorded baseline:** `docs/seo-ranking-comparison-checkpoint-2026-10-26.md` (GSC settled through Oct 17 and owner GA4 screenshots through Oct 20).

## 1. What is proven and what is not

- GSC historical 28-day **221 impressions, 1 click, 0.45% CTR, avg position 59.54**, not freshly fetched on Oct 23.
- `limo marketing agency`: **3** impressions, ~27.7 avg position; the homepage is the only URL visible in the exact-query Pages report. Too few impressions for an on-page rewrite decision.
- `limo seo`: **16** impressions, ~54.6 avg position; exact-query Pages showed homepage 7 impressions (~27.3 pos), SEO specialist 9 (~75.9 pos). *Overlap requires more samples before diagnosing damage.*
- `limo service google ads`: **56** impressions, ~67.0 avg position, relevant Ads specialist page visible.
- `limo website design`: **7** impressions, ~82.7 avg position, specialist page sole visible owner.
- URL Inspection: **20/22 estimated indexed** from combined 19–20 October evidence; `services.html` and `black-car-services.html` were index-eligible but not indexed in last screenshots. Do not claim this is a fresh 22-URL check.
- GA4 (Sep 23–Oct 20): 11 sessions, including **2 Google organic sessions** (one US, one India) and **5 Tag Assistant referrals**. Owner confirmed two `generate_lead` events were *test form submissions*; **no verified paying client / qualified organic enquiry demonstrated**.
- GSC Links 20 October: **0 external links reported** and 164 internal links reported. Not evidence that zero links exist anywhere on the web.
- UK/US editorial outreaches are **SENT** in `docs/seo-authority-outreach-log.md`; none may be claimed as a backlink/placement without exact published URL and permission. ILLBA declined the education proposal.

## 2. Money-page diagnosis

| URL | Current strength | Found gap | Safe action now | Owner-gated follow-up |
|---|---|---|---|---|
| `seo-for-limo-companies.html` | Intent-focused service content, headings, canonical, consultation flow | The original 12-point operator audit lacked a contextual link from the SEO diagnostic section | Add one useful internal contextual link in the relevant audit paragraph; preserve title, H1, scripts and CTA | Add redacted first-party engineering evidence once approved |
| `google-ads-for-limo-companies.html` | High-intent PPC content and conversion measurement framework | Same operator audit was not linked from the search-to-landing-page section | Add one relevant free-audit link; no new keyword repetitions or fictitious results | Confirm which Ads screenshots may be published as attributable, with metric definitions |
| `booking-systems.html` | Service-intent page with a link to 12-point worksheet and detailed feature examples | Live pricing, checkout/card payment, instant booking confirmation and paid-booking visuals go beyond current **documented implementation evidence** | **Do not rewrite without capability verification.** Prepare a concrete feature-evidence gate below | Only publish claims of working modules after demonstration/reproduction and client permissions |

**Why only 2 on-page changes in this sprint?** Both links give agency buyers access to a useful checklist at the exact decision point and strengthen existing topic relationships. No new page, thin city content, title/H1 rewrite, revised conversion trigger or tracking experiment is justified by the current sample.

## 3. Booking-system product claim evidence gate (urgent)

Current `booking-systems.html` contains: "live pricing," "online payments," "card payment," "instant confirmation," "Paid Bookings," a `$228.00` sample payable total, and a visual sample showing **PAID** status. Those are *marketing-page claims/illustrations*, not proof that live production customer payments have been processed.

| Capability or outcome | Evidence available in internal proof ledger | Publication rule |
|---|---|---|
| Customer booking-request collection and trip details | Project implementation trail; **PARTIAL** | Describe *anonymized* implemented workflow only; no client-name attribution until permission |
| Admin-side quotation/quote management | Project implementation trail; **PARTIAL** | Describe workflow scope conservatively; do not imply every client has all modules |
| Quote calculations / logic | Project implementation trail; **PARTIAL** | Show rules or de-identified step logic only after validating current behavior |
| Customer/operator notification workflow | Project implementation trail; **PARTIAL** | Verify live delivery/reliability before claiming production-scale results |
| Customer-facing guaranteed real-time payable fare | **Not substantiated by current ledger** | Show configurable/design possibility; claim operational only with recorded test evidence |
| Card payment processor integration, successful live charge and refund state | **Not substantiated by current ledger** | Do not say *already live* or use a paid receipt as client proof until demonstrated and authorized |
| Instant confirmed reservation after successful payment | **Not substantiated by current ledger** | Confirm end-to-end server-side states and confirmation pathway before promising |
| Published `$228.00` sample fare or `PAID` UI | Illustration on page, not a validated production receipt | Label visibly **illustrative example** unless real approved evidence is produced |
| Client name, testimonial, bookings uplift, ROAS | `docs/client-proof-ledger.md`: unrecorded permission/results | HOLD; never add client-specific claims without written permission |

**Owner decision requested before revising product copy:** Which payment/instant-confirmation modules are **working and demonstrable today**, which are **planned/in scope for a custom build**, and is this a demo vs live production case? No need to expose keys, personal data, payments or customer records.

**If live-payment proof unavailable:** Review and adjust relevant meta-description and structured data, hero wording, paid-status demo illustration, confirmation FAQs, and payment sections *consistently*, not just a tiny disclaimer. Suggest: "Customer request → operator quote → customer approval" as the demonstrated core, with "automated pricing/online payment available as scoped integrations" **only** when capability is actually offered and verified as such. Keep service value clear without false outcomes.

## 4. First-party anonymized booking/quotation workflow: evidence pack preparation

One genuine asset worth publishing, not another generic article:

**Working title:** “From Ride Enquiry to Operator Quote: A Limo Booking Workflow Walkthrough.”

Purpose: show the exact operational stages, failure states and who does what—useful to a prospective limo operator regardless of backlinks.

Document these screens/steps with dummy/redacted details and owner-approved usage rights:

1. Customer selects trip type and enters pickup/drop-off, journey date/time, passengers and luggage.
2. Form validation and request creation; distinguish *enquiry* from *quote*.
3. Operator sees request and constructs quote, including explicit pricing assumptions.
4. Customer receives/responds to quote; distinguish *quote sent* from *quote accepted*.
5. Confirmation and notifications only where genuinely implemented. If payment is future-scope, omit it from the illustrated path.
6. Demonstrate exception handling: missing address, round-trip rule, callback, duplicate submission or failed notification where evidence exists.
7. Show handoff outcome and constraints. **No invented lead volume, ROI, booking growth, percentages, customer or company names.**
8. Offer the existing [12-point audit](../resources.html) and consultation call as next useful steps.

**Before public release:** Confirm exact build state and allowed screenshots; remove IDs, tokens, email/phone details and private rider/customer information; get written client-name/logo permission if ever named. Publish as an anonymized *capability walkthrough*, not a named client success story.

## 5. What to measure next

**26 October checkpoint (already prepared in repo and scheduled):**
- Same-property Search Console Web data export, all queries and Pages for last 28 *settled* days.
- Where feasible, separate non-overlapping 7-day windows for Oct 11–17 and Oct 18–24 once the latter is fully settled.
- Recheck `services.html` and `black-car-services.html` Google Index states without repeating indexing requests blindly.
- Track US and UK query impressions, specialist-page rankings and Google organic sessions; record form submissions verified against actual inbox records.
- Separate internal Tag Assistant traffic, test `generate_lead` events and newsletter `sign_up` from business enquiries.
- A SERP appearance or backlink should never be asserted as a conversion or customer without evidence.

**30-day scale operating targets** (not performance forecasts): 25 specifically researched prospects/week; 2 owner-approved first-party evidence assets; 3 commercial pages assessed; weekly GSC and GA4 check. No outreach is authorized or sent by this documentation.

## 6. Publication and link safety

- Never buy automated/PBN/backlink packages or publish thin city/airport doorway pages.
- One intent = one primary URL owner; do not clone SEO/Google Ads/booking pages just to rank extra terms.
- The latest GSC is too small to justify repeating homepage title/H1 revisions; let recently published changes recrawl.
- Editorial outreach requires a grounded real target, a useful non-promotional pitch and owner approval; use `docs/seo-authority-outreach-log.md` to avoid duplicates.
- Link equity and rankings are not guaranteed by internal links or industry pitches.
- GA4 connected or configured does not prove real clients; only a qualified operator inquiry in the actual inbox/CRM does.

**Release scope of this sprint:** two contextual HTML links to an existing worksheet plus this internal documented capability/measurement gate. No changes to booking system page, other service claims, analytics scripts, forms, sitemaps or production payment flows.
