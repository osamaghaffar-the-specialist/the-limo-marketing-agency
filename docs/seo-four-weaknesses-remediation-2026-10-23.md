# TLMA — Four Weaknesses: Evidence-Based Remediation

**Audited:** 2026-10-23  
**Scope:** US/UK limo/chauffeur/black-car marketing agency, GitHub Pages.  
**Goal:** Qualified, genuine operator enquiries and paying clients; do not substitute visibility metrics for client results.  
**Release:** Booking trust fix, contextual audit links and factual sitemap `lastmod`; no form destinations, scripts, tokens or production booking APIs touched.

## 1. Google Indexing — two previously pending URLs

**Historical evidence (20 Oct GSC user screenshots):** `/services.html` and `/black-car-services.html` were not indexed in the Google Index tab but their Live Test said eligible to index. Another three previously unindexed pages were later individually confirmed indexed, making **~20/22 historical estimated** rather than a current authoritative count.

**23 Oct code/read checks:** Both pages are public, render readable crawlable English content, have own self-referencing canonical, `index,follow` meta, sitemap entries and links from homepage/services/industries/navigation. No confirmed technical block. A public crawler being able to read a page is **not** Google Index confirmation.

**Change:** Add one natural contextual link to the existing first-party [12-point booking conversion audit](../resources.html#limo-booking-conversion-audit) from each pending page. Update sitemap `lastmod` for the genuinely changed pages, including these two. No repeated indexing requests or keyword-stuffed duplicate pages.

**Still needs proof:** Owner's GSC URL Inspection → *Google Index* screenshot for each URL after Google recrawls. Separate index verdict from the Live Test. If not indexed and a reason appears, address exact reason; don't assume a canonical, technical or content problem without evidence. Check GSC 26 Oct checkpoint.

## 2. External Authority — weak earned references

**Historical GSC (20 Oct):** 0 **reported** external backlinks, 164 reported internal links. Not proof that zero links exist anywhere. Existing TLMA [authority outreach log](seo-authority-outreach-log.md) lists sent pitches: Chauffeur Driven, Professional Driver, TaxiPoint, PHTM and TheChauffeur editorial/associations. ILLBA declined. No published backlink verified.

**Existing shareable, useful asset:** Browser-only operator [12-point booking conversion audit](../resources.html#limo-booking-conversion-audit), independently usable without testimonials or fictitious results. Now linked contextually from SEO, Google Ads, Booking Systems, Services and Black Car pages.

**Next eligible authority action:** Monitor responses to existing individualized editorial pitches; where editor wants an article, contribute a genuinely useful, non-promotional explanation of the booking enquiry → operator quote → confirmation evidence hierarchy. Do not send duplicate pitches or outreach without approval. Don't buy PBN/low-quality directory links or promise any backlink. After publication verify exact live URL and genuine referring link in browser, *then* record authority progress.

**Status:** Relevant resource and internal discoverability improved; **external authority still not independently earned/verified**.

## 3. Genuine Organic Leads — no qualified client evidence yet

**Owner GA4 screenshots (23 Sep–20 Oct):** 11 GA4 sessions total, 2 Google organic (one United States, one India), 2 `generate_lead` events attributed to **the owner's own tests**. Not 2 genuine prospects. GA4 Traffic Acquisition key-event count was 0, so event/key-event configuration deserves follow-up but avoid counting tests.

**Implementation state:** Home and contact consultation forms use a FormSubmit AJAX endpoint with `response.ok`/failure checking; only after successful response do they set sessionStorage success flags and redirect to `thank-you.html`, whose logic consumes those flags before firing `generate_lead`. This is a code-path inspection, not a new production test or verified real inbox receipt.

**Critical delivery check:** Live form code is configured to deliver to `osamaghaffar001@gmail.com`, while the *connected Gmail account* is `limomarketingagencyinfo@gmail.com`. No `New Website Lead` FormSubmit messages were visible in the connected TLMA Gmail search from Oct 1. **Do not change the recipient silently:** changing FormSubmit targets can require email verification/activation and risks losing enquiries. Owner must verify the destination inbox is actively monitored, FormSubmit is activated and legitimate form messages arrive; configure forwarding/routing to agency inbox *after* confirmation, or approve a controlled migration with a test.

**Leads pipeline:** Five individual US/UK operator prospect candidates documented in `docs/seo-operator-prospects-research-2026-10-23.md`, no emails sent. For business value, only count identified operators with a substantive request and confirmed receipt/callback. Do not treat Tag Assistant referrals, newsletter `sign_up`, test events or blog impressions as leads.

**Status:** Tracking code exists and historic tests fired; **real organic leads/delivery in intended inbox still to be verified**.

## 4. Booking & Payment Claims — trust remediation

**Before:** Homepage claimed website traffic turned into automatic confirmed bookings; booking service page prominently displayed `PAID`, `LIVE`, card checkout, instant confirmation, a $228 total and FAQs/schema implying currently working checkout. Internal [client proof ledger](client-proof-ledger.md) only substantiates anonymized ride-request, operator quote logic and notification flow for an implementation in `PARTIAL` state. No recorded live-payment processor, approved customer receipt, payment/refund reconciliation or instantaneous booking confirmation end-to-end test.

**Change:**
- Homepage: limit *booking showcase section* to request, operator quote, routing and notification capabilities; say payments/automatic confirmation are **optional integrations** rather than an already delivered live workflow. Homepage SEO `<title>`, H1, canonical, script and forms untouched.
- Booking Systems page: service remains positioned for custom limo reservation software, but hero describes documented request → operator quote. Example quote UI labeled **illustrative**, fake `LIVE`/`PAID` hero states removed, optional-payment roadmap and price formula clearly marked as demo; card checkout and paid confirmation consistently conditional in sections, human-readable FAQs and schema FAQ answers.
- Explicitly separate potential future payment feature from verified production capability. Payment integration is *not* added or tested; no billing credentials requested, no real charges generated.

**Still needs proof:** If claiming a deployed/operational integrated customer checkout, provide redacted approved demo of payment processor integration, actual test transaction state, successful operator/admin status transition, failed-payment state, confirmation, and approved scope/permission. No invented results.

## 5. Release QA and measurement gates

- Exact changes: `booking-systems.html`, `index.html`, `services.html`, `black-car-services.html`, `sitemap.xml`, this internal document.
- Booking FAQ JSON-LD parses and matches updated visible FAQ answers; preserve canonical, title, GA4 instrumentation, navigation and consultation forms.
- Inspect all modified pages visually on mobile/desktop after publication; no page-speed guarantee is made from static code alone.
- 26 Oct: GSC URL Inspection for two pending pages; GSC performance two nonoverlapping weekly windows where settled, plus 28-day directional trend; GA4 organic countries, non-test `generate_lead`, verified emails. See [26 Oct tracker](seo-ranking-comparison-checkpoint-2026-10-26.md).
- Do not count authority improvement until an external referring URL exists; do not count leads until a real operator contacts the agency.
