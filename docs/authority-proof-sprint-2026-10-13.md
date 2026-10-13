# TLMA Authority & Proof Sprint — 2026-10-13

## Objective
Strengthen TLMA's trust and authority signals without disturbing recently optimized keyword ownership or publishing unsupported client/results claims.

## Current SEO context
- Primary commercial battle: `limo marketing agency`.
- Existing indexed money pages are in a recrawl/measurement window and should not be repeatedly rewritten.
- Indexing remains the immediate technical bottleneck; authority and proof are the next ranking layer.

## Rules for this sprint
1. Evidence before claims.
2. Permission before named-client amplification.
3. A screenshot proves the screenshot/account/system exists; it does not automatically prove causation.
4. Conversion value is not booked revenue unless reconciled with booking/payment records.
5. No fake testimonials, fake reviews, invented ROAS, invented lead growth, or invented booking growth.
6. No paid memberships, new outreach emails, PBNs, bulk backlinks, or doorway/city-page scaling in this sprint.
7. Do not rewrite indexed homepage/SEO/Google Ads money-page keyword ownership while Google is still recrawling recent changes.
8. One search intent = one primary owner URL.

## Sprint 1 — Case-study trust cleanup
Status: prepared on branch `seo-authority-proof-cleanup-2026-10-13`.

Changes:
- remove permission-unverified named-client amplification from the public case-study portfolio;
- remove named CreativeWork schema until proof/permission is VERIFIED;
- remove the permission-unverified named testimonial;
- preserve anonymized implementation evidence;
- preserve anonymized Google Ads account screenshots with metric-definition caveats;
- make the public standard explicit: Evidence → Permission → Claim.

## Sprint 2 — Homepage proof hardening
Status: HOLD until the current recrawl window is evaluated.

Finding:
The homepage contains illustrative dashboard-style numbers such as `+421%` Organic Traffic and conversion counts. A disclaimer exists, but the visual can still be interpreted as client performance proof.

Next safe options after the recrawl gate:
- label those modules clearly as `Illustrative dashboard` / `Demo metric`, or
- replace unverified numeric values with non-numeric system/capability visuals.

Do not attach those numbers to a client or result without evidence.

## Sprint 3 — First VERIFIED client case study
Status: evidence collection required.

Minimum gate:
- relationship verified;
- exact scope verified;
- public-use permission recorded;
- screenshot/logo permission recorded if used;
- every KPI has a source, timeframe and definition;
- claim wording approved.

Preferred case-study structure:
Problem → Baseline → Work delivered → Evidence → Outcome → Measurement definition → Client approval.

## Sprint 4 — Authority assets
Release only after indexing health improves or a concrete authority opportunity justifies the release.

Planned assets:
- UK Taxi Dispatch System Prices research page;
- Limo SEO Technical Audit Checklist — 90+ checks.

## Measurement
Track:
- indexed URLs / 21;
- branded searches;
- non-brand impressions;
- primary cluster average position;
- page-one and top-three keyword count;
- referring domains and earned mentions;
- organic landing-page sessions;
- successful `generate_lead` events once marked as a GA4 key event;
- consultation / booked-call outcomes where available.

## Current next action
Merge Sprint 1 after final diff validation, then allow Google to crawl the cleaned evidence-first portfolio. Do not open a new content-production sprint until indexing and recrawl data are checked.
