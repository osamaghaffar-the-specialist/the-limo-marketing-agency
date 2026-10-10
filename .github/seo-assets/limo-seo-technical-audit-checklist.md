# Limo SEO Technical Audit Checklist

**Status:** Internal linkable-asset draft — not approved for production publishing yet.  
**Audience:** Limo, chauffeur, black car and airport transportation operators.  
**Purpose:** A practical audit framework for finding the SEO issues that can block qualified search visibility, local discovery and booking conversion.

> This checklist is diagnostic, not a ranking guarantee. A pass/fail result should be based on the operator’s real website, market, service coverage and measurement setup.

## How to Use This Checklist

Work in this order:

- **P0 — Blocking:** crawling, indexing, canonicalization, broken templates, mobile usability or tracking defects that can invalidate later work.
- **P1 — Money-page intent:** the pages that should rank for high-value services, airports, routes and markets.
- **P2 — Authority & expansion:** internal linking, proof, content depth, GEO/AI-search clarity and external authority.
- **P3 — Ongoing measurement:** query ownership, conversion tracking, content decay and recrawl/indexing checks.

Do not create new pages simply because a keyword exists. Every proposed URL needs a distinct search intent, useful customer value and a role in the booking journey.

---

# 1. Crawlability & Indexing — P0

## Robots and index controls
- [ ] `robots.txt` returns HTTP 200.
- [ ] Important service pages are not blocked by `robots.txt`.
- [ ] Important pages do not contain an accidental `noindex` directive.
- [ ] Thank-you, internal utility and other non-search pages use intentional indexing rules.
- [ ] Staging/test URLs are not indexable.

## XML sitemap
- [ ] XML sitemap returns HTTP 200.
- [ ] Sitemap contains only canonical, indexable URLs.
- [ ] No 404, redirect, duplicate or `noindex` URLs are submitted.
- [ ] `lastmod` values are used only when they represent real page changes.
- [ ] Sitemap is submitted in Google Search Console.
- [ ] Sitemap processing errors and warnings are checked after Google fetches it.

## Google Search Console indexing
- [ ] Core money pages have been inspected individually.
- [ ] Indexed, discovered, crawled-not-indexed and unknown URLs are separated rather than treated as one problem.
- [ ] Google-selected canonical matches the intended canonical on important pages.
- [ ] Duplicate URL variants are understood before redirects or canonical changes are made.
- [ ] Indexing changes are monitored after deployment instead of assumed from sitemap submission.

---

# 2. Canonical & URL Architecture — P0

- [ ] Every indexable page has one self-referencing canonical, except intentional duplicate variants.
- [ ] Homepage variants (`/`, `/index.html`, extensionless forms where applicable) consolidate to one preferred URL.
- [ ] HTTP consistently resolves to HTTPS.
- [ ] Trailing-slash behavior is predictable.
- [ ] Uppercase/lowercase variants do not create duplicate indexable pages.
- [ ] Parameter/query-string URLs do not become accidental duplicates.
- [ ] Internal links point to canonical URLs rather than duplicate variants.
- [ ] Redirect chains are avoided.
- [ ] 404 pages return an actual 404 status rather than a soft 404.

---

# 3. One Search Intent Per Money Page — P1

Create a keyword-to-URL ownership map before changing copy.

For every important URL, record:
- [ ] Primary keyword family.
- [ ] Supporting variants.
- [ ] Search intent: commercial, comparison, informational or navigational.
- [ ] Funnel stage.
- [ ] Market/country relevance.
- [ ] Internal-link sources.
- [ ] Current GSC queries and average positions.
- [ ] Whether another URL is competing for the same query.

## Guardrails
- [ ] Homepage owns broad agency/category intent rather than every specialist service term.
- [ ] SEO service queries map to the SEO page.
- [ ] Google Ads service queries map to the paid-search service page.
- [ ] Website-design queries map to the website page.
- [ ] Booking-system queries map only to a page whose functionality genuinely supports them.
- [ ] Informational articles support service pages without becoming duplicate commercial pages.
- [ ] Industry pages add vertical context rather than repeating generic service copy.

---

# 4. Limo Service Architecture — P1

A limo website normally has multiple commercial intents. Audit whether the structure gives each justified intent a useful destination.

## Core service intent
Examples to evaluate based on real service capability:
- [ ] Airport transfers.
- [ ] Corporate / executive transportation.
- [ ] Point-to-point service.
- [ ] Hourly chauffeur service.
- [ ] Events / weddings where actually offered.
- [ ] Black car service.
- [ ] Group / SUV / van service where actually offered.

## Market intent
- [ ] Primary market has a genuinely useful landing page where justified.
- [ ] Location pages are unique and useful—not spun city-name templates.
- [ ] Neighborhood pages exist only where customer demand and service coverage justify them.
- [ ] Service-area language matches the operator’s real coverage.

## Airport and route intent
- [ ] Airport pages answer actual airport-transfer questions.
- [ ] Route pages are created only for real, meaningful demand.
- [ ] Route pages include useful pickup/drop-off context rather than keyword-swapped text.
- [ ] Airport/route pages link into the booking or quote journey.
- [ ] Thin doorway-page patterns are avoided.

---

# 5. On-Page SEO — P1

For every money page:
- [ ] Title clearly reflects the page’s primary intent.
- [ ] Meta description is useful and specific rather than keyword-stuffed.
- [ ] Exactly one clear H1 is present.
- [ ] H2/H3 structure follows the customer’s decision journey.
- [ ] Intro explains who the service is for and what problem it solves.
- [ ] Primary topic appears naturally in visible copy.
- [ ] Supporting entities and services are covered where relevant.
- [ ] Copy answers commercial objections and next-step questions.
- [ ] The page has a clear CTA.
- [ ] CTA matches the intent: booking, quote, consultation, demo or audit.
- [ ] No ranking guarantees or unverifiable claims are used.

---

# 6. Local SEO & Google Business Profile — P1

- [ ] Google Business Profile name matches the real business name.
- [ ] Primary/secondary categories accurately reflect the operator.
- [ ] Address/service-area configuration is truthful.
- [ ] Phone, website and business information are consistent.
- [ ] Services are accurately described.
- [ ] GBP landing URL points to the strongest relevant canonical page.
- [ ] Local landing pages support—not contradict—GBP service areas.
- [ ] Reviews are acquired legitimately and never fabricated.
- [ ] Review replies are natural and specific.
- [ ] Photos and business information are kept current.
- [ ] Local citations are evaluated for accuracy, relevance and legitimacy rather than raw quantity.

---

# 7. Technical Performance & Mobile UX — P0/P1

## Core Web Vitals / page experience
- [ ] LCP candidate identified and not unnecessarily lazy-loaded.
- [ ] Large hero/background images are compressed appropriately.
- [ ] Images have intrinsic width/height or stable aspect ratios to reduce CLS.
- [ ] Below-the-fold imagery uses lazy loading where appropriate.
- [ ] Excessive embedded Base64 assets are avoided.
- [ ] Unused JavaScript is reviewed before adding more scripts.
- [ ] Render-blocking CSS/JS is measured before restructuring.
- [ ] Mobile layout has no horizontal overflow.
- [ ] Tap targets and forms are usable on phones.

## Booking-path performance
- [ ] Booking/quote flow works on mobile.
- [ ] Autocomplete/maps do not block basic form completion if they fail.
- [ ] Important form controls remain responsive on slower networks.
- [ ] Confirmation/thank-you flow works after submission.

---

# 8. Internal Linking — P1/P2

- [ ] Homepage links to specialist service pages using descriptive anchors.
- [ ] Service hub links to each specialist service.
- [ ] Industry hub links to each relevant vertical page.
- [ ] Resource hub links to current guides.
- [ ] Informational articles link to the correct commercial owner.
- [ ] Related service pages cross-link where the customer journey justifies it.
- [ ] Important money pages are within a shallow click depth.
- [ ] No sitemap URL is orphaned.
- [ ] Broken internal links = 0.
- [ ] Broken fragment links = 0.
- [ ] Generic `Learn More` anchors are replaced when a descriptive anchor improves context naturally.

---

# 9. Cannibalization Control — P1/P3

Use Search Console query-by-page data before changing URLs.

- [ ] Identify queries where multiple pages receive impressions.
- [ ] Confirm whether the overlap is harmful or simply adjacent intent.
- [ ] Assign one preferred owner for each commercial keyword family.
- [ ] Strengthen contextual internal links toward the owner.
- [ ] Re-scope supporting pages before considering a merge.
- [ ] Do not redirect a page solely because two URLs share a few impressions.
- [ ] Wait for recrawl after material internal-link/on-page changes before making another destructive change.

---

# 10. Structured Data & Entity Graph — P1/P2

Use structured data only when the visible page supports it.

- [ ] Stable Organization `@id` is used sitewide.
- [ ] Organization has a real logo reference.
- [ ] WebSite references the Organization as publisher.
- [ ] WebPage references the WebSite.
- [ ] Service pages use defensible Service markup.
- [ ] Service provider references the Organization.
- [ ] BreadcrumbList matches visible/site architecture.
- [ ] Article schema is used only for actual articles.
- [ ] Article dates are truthful.
- [ ] Article image represents the article rather than using an unrelated logo merely to silence a warning.
- [ ] FAQ schema is used only when current Google eligibility and visible-content requirements justify it; visible FAQ content remains useful even without rich-result eligibility.
- [ ] No fake AggregateRating, Review, Offer, price or location data is added.

---

# 11. GEO / AI Search Readiness — P2

AI visibility is not a guaranteed placement. Audit whether the content is easy to understand, retrieve and verify.

- [ ] Business entity is described consistently across important pages.
- [ ] Audience is explicit: limo, chauffeur, black car, airport transportation, taxi/private hire where relevant.
- [ ] Important questions have concise answer-first blocks.
- [ ] Deeper supporting detail follows direct answers.
- [ ] Claims can be traced to real evidence or clearly labelled methodology.
- [ ] Sources are cited on research/comparison pages.
- [ ] Vendor pricing uses retrieval dates and source links.
- [ ] Comparison methodology is transparent.
- [ ] Content is present in crawlable semantic HTML.
- [ ] Important facts are not hidden only inside images or decorative interactions.
- [ ] Organization → WebSite → WebPage → Service/Article relationships are coherent.
- [ ] Update dates are changed only when meaningful content actually changes.

---

# 12. Trust, Proof & E-E-A-T Signals — P2

- [ ] About page clearly explains who operates the business and what it specializes in.
- [ ] Contact information is real and consistent.
- [ ] Privacy and terms pages are accessible.
- [ ] Case studies use verified projects only.
- [ ] Results include enough context to understand what was measured.
- [ ] Screenshots are genuine and appropriately redacted.
- [ ] Client quotes are published only with real permission/source.
- [ ] Vendor partnerships/memberships are claimed only when verifiable.
- [ ] Methodology is published for original research.
- [ ] Content distinguishes observed data from estimates/opinion.

---

# 13. Backlink & Authority Audit — P2

Do not judge links by DR/DA alone.

For each referring domain, record:
- [ ] Referring page.
- [ ] Destination URL.
- [ ] Anchor text.
- [ ] Topical relevance.
- [ ] Editorial context.
- [ ] Whether a real user could reasonably discover/click it.
- [ ] Whether the mention is legitimate and current.

## Preferred authority sources
- [ ] Real client implementation/case-study attributions.
- [ ] Transportation industry organizations/publications.
- [ ] Software/vendor implementation case studies.
- [ ] Original-research citations.
- [ ] Select legitimate business/agency profiles.

## Avoid
- [ ] Bulk backlink packages.
- [ ] PBNs.
- [ ] Automated guest-post networks.
- [ ] Exact-match anchor spam.
- [ ] Irrelevant directory blasts.
- [ ] Fake memberships, awards or partner badges.

---

# 14. Booking & Conversion Measurement — P1/P3

Traffic without conversion measurement is incomplete.

- [ ] GA4 is installed once and firing correctly.
- [ ] Google Tag Manager setup is documented if used.
- [ ] Search Console is connected and monitored.
- [ ] Consultation/lead form submissions are measured.
- [ ] Phone-click events are measured where calls are a desired action.
- [ ] Booking-demo / booking-start actions are measured.
- [ ] Booking completion is tracked where the booking platform allows it.
- [ ] Form-start events are treated as diagnostic—not equal to bookings.
- [ ] UTM parameters survive the path where technically possible.
- [ ] Organic landing pages can be tied to downstream actions.
- [ ] Duplicate event firing is checked.
- [ ] Test submissions are separated from real leads where practical.

---

# 15. Search Console Operating Review — P3

Run this review on a repeatable cadence rather than reacting to one-day movement.

- [ ] Top queries by impressions and clicks.
- [ ] Top landing pages.
- [ ] Country split.
- [ ] Device split.
- [ ] New query families.
- [ ] Page/query cannibalization.
- [ ] Position-3–30 opportunities.
- [ ] Indexed vs unknown/not-indexed sitemap URLs.
- [ ] Google-selected canonical exceptions.
- [ ] Search appearance changes where relevant.
- [ ] Content/ranking decay over meaningful comparison windows.
- [ ] Changes are annotated so rankings can be compared against deployments.

---

# 16. Audit Deliverable Template

For every confirmed issue, document:

| Field | What to record |
|---|---|
| Issue | Specific verified problem |
| URL(s) | Exact affected page(s) |
| Evidence | Crawl, GSC, analytics, source or reproducible observation |
| Severity | P0 / P1 / P2 / P3 |
| Business impact | Indexing, visibility, conversion, trust or maintainability |
| Recommended fix | Exact action, not generic advice |
| Risk | What could regress if changed |
| QA | How the fix will be verified |
| Status | Open / Implemented / Verified / Monitoring |

Do not mark an item “fixed” merely because code was changed. Verify the live deployment and, where relevant, wait for search-engine recrawl before judging the search outcome.

---

# 17. Stop Conditions — When Not to Make Another SEO Change

Do **not** keep editing a page when:

- [ ] Google is already surfacing it for the correct query family and the next bottleneck is authority/site maturity.
- [ ] A warning is only a tool recommendation and the suggested property would require fabricated data.
- [ ] The page has just been materially changed and has not been recrawled yet.
- [ ] A redirect/merge decision is based on too little query data.
- [ ] A new location page would be thin or duplicative.
- [ ] A software keyword implies capabilities the product does not actually have.
- [ ] A backlink opportunity would have no value if Google ignored the link.

---

## Final Audit Question

Before approving any SEO task, ask:

**“Does this change make the operator’s website easier for a real customer and a search/retrieval system to understand, trust and use — and can we verify that without inventing evidence?”**

If the answer is no, the task should not be prioritized simply because an SEO tool produced a warning.
