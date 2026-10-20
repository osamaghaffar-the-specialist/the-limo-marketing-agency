# TLMA SEO + GEO Continuity Checkpoint — 2026-10-20

**Business:** The Limo Marketing Agency  
**Production repository:** `osamaghaffar-the-specialist/the-limo-marketing-agency` (`main`)  
**Site:** https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/  
**Verified main baseline when preparing this checkpoint:** `14257f4a15b5cbe7e7b461af7c1df2600ee8b57e` (PR #53; 2026-10-19)  
**Primary success criterion:** qualified limo/chauffeur/black-car/taxi operator enquiries, then paying clients — not impression volume alone.

## Why the earlier 21-URL handoff must not be replayed literally

The handoff stopped at commit `7a5bde1e49a54724b4baba16c81ca1b59383ab82`, when the external US/UK keyword map was described as unmerged. That status is obsolete:

- [PR #20](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/20) **merged** the first external keyword map on 2026-10-10.
- [PR #27](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/27) **merged** the verified/finalized map on 2026-10-10.
- The current source of truth is `docs/seo-external-keyword-gap-war-map.md` on `main`; the old `seo-external-keyword-gap-war-map` branch has diverged and **must not be merged again**.
- [PR #28](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/28) merged the UK dispatch-pricing research brief.
- [PR #48](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/48) published the UK taxi dispatch prices page on 2026-10-14 after the documented indexing release gate improved.
- [PR #49](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/49) completed the UK pricing-page meta-description QA.
- The sitemap at this checkpoint has **22** indexable listed URLs, not 21.

## Latest available *recorded* GSC snapshot (not a fresh live API pull)

Source: `docs/seo-top20-authority-sprint-2026-10-19.md`, which documents the user's exported `Performance-on-Search-2026-10-19.zip`, property URL prefix matching the site, last 28 days through **2026-10-17**.

| Metric | Recorded value |
|---|---:|
| Web clicks | 1 |
| Impressions | 221 |
| CTR | 0.45% |
| Average position | 59.54 |
| Homepage clicks / impressions | 1 / 16 |
| `limo marketing agency` named-query impressions / avg position | 3 / 27.67 |
| `limo seo` impressions / avg position | 16 / 54.62 |
| `limo service google ads` impressions / avg position | 56 / 67.04 |
| US impressions / clicks | 180 / 1 |

**Latest documented individual URL inspection (2026-10-19):** **17 of 22 indexed**, five pending/not indexed: `services.html`, `black-car-services.html`, `social-media-marketing-for-limo-companies.html`, `privacy-policy.html`, and `uk/taxi-dispatch-system-prices/`. Requesting indexing is not proof of indexing. These numbers are historical dated observations; recheck before drawing a current conclusion.

**Current integration limitation (2026-10-20):** The connected GSC Wizard service refused property access with `subscription_required`. No direct fresh GSC indexing or GA4 query was possible through that connector during this checkpoint. Do **not** present historical counts as live results. Refresh with direct user-side Search Console export or another working authorized connection if needed.

## Tracking and conversion implementation

- [PR #40](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/40): GA4 installation and initial success-only lead instrumentation.
- [PR #51](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/51): confirmed-success session flags added across twelve landing-page consultation forms; thank-you flow consumes the flags before `generate_lead`.
- `docs/seo-top20-authority-sprint-2026-10-19.md` reports that `generate_lead` is marked as a GA4 key event. **This is an implementation/recorded-setting milestone, not evidence of actual new leads.** Validate in live GA4 when access is available; do not generate dummy production conversions.
- [PR #52](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/52): an interactive, browser-only **12-point Booking Conversion Audit** was added to `resources.html#limo-booking-conversion-audit`; an internal link was added from the proof page.
- [PR #53](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/53): linked the Booking Systems page to the existing audit.

## Current SEO ownership and release gates

- Homepage: `limo marketing agency`.
- SEO page: `limo seo` and `SEO for limo companies`.
- Google Ads page: `Google Ads for limo companies`.
- Website design page: `limo website design`.
- Booking Systems page: `limo booking software / booking system`, limited to proven quote/booking/payment/admin capabilities.
- GEO page: AI-search/GEO services for limo operators.
- UK pricing guide: `taxi dispatch system prices` and UK-price comparison intent. **It is now published**, even though its indexing was still pending on the last recorded inspection.
- Full taxi/limo dispatch software, fleet-management and accounting software are **not** TLMA product claims absent real implementation proof.
- Do not publish multiple near-duplicate UK/US pages or change homepage title/H1 solely because of a low-sample average rank.

## Authority and proof state

- Editorial/association outreach to named publishers and industry associations was logged as **sent** in `docs/seo-authority-outreach-log.md` (2026-10-12), not as earned backlinks or live placements.
- Client proof, permissions and metric-source requirements are tracked in `docs/client-proof-ledger.md`; never attribute client results or imply affiliations without evidence/approval.
- [PR #50](https://github.com/osamaghaffar-the-specialist/the-limo-marketing-agency/pull/50) established the homepage Top-20/editorial authority sprint, with **no homepage title/H1 rewrite through 2026-10-26** absent a real defect.
- Do not send further editorial pitches, follow-ups, memberships or paid requests without explicit owner approval. Free organic/earned authority is the default.

## Prioritized next actions from this verified checkpoint

1. **2026-10-26 to 2026-11-02:** compare *like-for-like* 7-day/28-day GSC exports on the same property and search type. Check the 5 pending URLs with URL Inspection before using new indexing percentages; avoid repetitive indexing submissions.
2. Recheck GA4 live `generate_lead` key-event health and attribution from real successful submissions. A measurement event does not prove a qualified prospect.
3. Review UK pricing-page discovery and current first-party vendor citations; do not invent vendor prices and do not release the second UK comparison page until current indexing, search intent and evidence justify it.
4. Build **permission-safe, first-party proof**: product walkthroughs, scope/limitations, and original audit methodology. Named client/metric claims require the proof ledger.
5. Earn relevant authority through owner-approved industry/editorial relationships, independent research and useful resources; record actual live published URL/referring domain separately from merely sent outreach.
6. Reassess the homepage's `limo marketing agency` ownership after recrawl/meaningful repeated impressions; do not overfit 3 exact-query impressions.
7. Keep technical/performance foundation intact; do not redo old Base64, canonical, logo-schema, sitewide H1 or mass meta audits without a newly observed defect.

## Exact repository change in the checkpoint PR

- This document records verified project state without changing page content.
- The sitemap's `resources.html` `<lastmod>` may be corrected from **2026-10-14** to **2026-10-19** because PR #52 substantially expanded Resources on October 19 with a real interactive worksheet. The change is based on a dated actual content edit, **not** a fictitious freshness signal.
- No production HTML, forms, GA4 code, money-page titles, canonicals, robots rules, or new indexable URLs should change in this housekeeping PR.

## Verification principle

GitHub PR merge history and `main` files support deployment-source facts. Google Search Console and GA4 outcomes require their own dated measurements; a GitHub merge, sitemap entry, or indexed-looking search snippet does **not** establish actual Google indexing or lead attribution.
