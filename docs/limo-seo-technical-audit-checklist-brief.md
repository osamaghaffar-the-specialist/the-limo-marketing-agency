# Limo SEO Technical Audit Checklist — Linkable Asset Brief

**Status:** Research brief only. Do not publish as a new production URL until the indexing release gate is satisfied.  
**Provisional future URL:** `/limo-seo-technical-audit-checklist.html`  
**Primary intent:** practical SEO audit/checklist for limo, chauffeur and black-car operators.  
**Primary conversion goal:** Free Growth Audit / SEO consultation.  
**Owner relationship:** supports `/seo-for-limo-companies.html`; it must not compete with that commercial service page.

## Why this asset exists

The current SEO service page is already well aligned with its commercial query family. The next authority lever is a useful, citable operator resource rather than another title/H1 rewrite.

The asset should be valuable even if the reader never hires TLMA. It should help an operator identify what is blocking discovery, rankings, local visibility, trust or booking conversion, then prioritize fixes.

## Search / SERP observation

Current limo-SEO content commonly covers:
- Google Business Profile and local visibility;
- service, airport, route and city-page architecture;
- reviews and business-information consistency;
- technical crawl/index issues;
- backlinks / local authority;
- measurement.

TLMA's differentiation should be a **repeatable audit framework with severity, evidence, test method and booking impact**, not another generic “do SEO” article.

## Source standard

Use primary sources for technical guidance where possible. Recommended official references:
- Google Search Essentials / Search Central Help: https://developers.google.com/search/help
- Helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Search appearance / structured data overview: https://developers.google.com/search/docs/appearance
- Page experience guidance: https://developers.google.com/search/docs/appearance/page-experience
- Organization structured data: https://developers.google.com/search/docs/appearance/structured-data/organization
- LocalBusiness structured data: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Spam policies / doorway abuse: https://developers.google.com/search/docs/essentials/spam-policies

Do not turn third-party claims into Google rules. Competitor observations can inform coverage, but technical claims should be supported by authoritative documentation or clearly labelled TLMA methodology.

## Direct-answer block

**What should a limo SEO audit check?**  
A limo SEO audit should check whether Google can crawl and index the site, whether each high-value service or local intent has one useful page, whether business and local signals are accurate, whether the site is fast and usable on mobile, whether internal links and structured data clarify the business, whether relevant external authority exists, and whether calls, quote requests and bookings can be measured from organic landing pages.

## Severity model

Every check gets one status:
- **P0 — Blocking:** can prevent crawling, indexing, security or core conversion.
- **P1 — Revenue / visibility:** high-impact issue affecting money pages, local visibility or booking actions.
- **P2 — Growth:** meaningful improvement, but not a blocker.
- **P3 — Enhancement:** useful polish after higher-impact items are stable.

Every finding should show:
1. check;
2. evidence;
3. pass/fail/needs-review;
4. why it matters;
5. recommended action;
6. owner;
7. priority.

# Checklist

## A. Business truth & search-intent foundation

1. Confirm the exact services the operator genuinely provides. **P1**
2. Confirm actual service cities / service areas. **P1**
3. Confirm airports the operator genuinely serves. **P1**
4. Confirm route-specific services that can be operationally fulfilled. **P1**
5. Confirm fleet types, passenger capacity and luggage guidance used on the site are accurate. **P1**
6. Confirm business name, phone, email and contact details are consistent on the website. **P1**
7. Confirm business hours / availability claims are accurate. **P1**
8. Confirm booking, quote, payment and cancellation claims match the real workflow. **P1**
9. List the highest-value search intents: service, airport, route, corporate, wedding/event, hourly, point-to-point and local. **P1**
10. Assign one intended landing page to each material search-intent family. **P1**

## B. Crawlability, indexability & canonical control

11. Verify the correct Search Console property is active. **P0**
12. Check important URLs return the expected successful HTTP status. **P0**
13. Confirm `robots.txt` does not block pages that should rank. **P0**
14. Confirm indexable pages do not carry accidental `noindex`. **P0**
15. Confirm legal / utility pages use noindex only where intentionally appropriate. **P2**
16. Check self-referencing canonicals on unique indexable pages. **P1**
17. Check duplicate URL variants such as `/`, `/index.html`, extensionless and trailing-slash forms. **P1**
18. Review Google-selected canonical on important URLs when GSC data exists. **P1**
19. Confirm XML sitemap contains only intended canonical indexable URLs. **P1**
20. Confirm sitemap `lastmod` values are truthful when used. **P2**
21. Check for orphan money pages. **P1**
22. Check important commercial pages are reachable within a sensible click depth. **P1**
23. Check broken internal links and broken fragments. **P1**
24. Check true 404 handling for nonexistent URLs. **P1**

## C. Technical performance & mobile usability

25. Test Core Web Vitals / lab performance on priority landing pages. **P1**
26. Identify the probable LCP element and avoid unnecessary lazy loading on it. **P1**
27. Add stable image dimensions / aspect ratios where missing. **P2**
28. Compress oversized images while preserving required quality and transparency. **P2**
29. Check mobile viewport and horizontal overflow. **P1**
30. Check tap targets, readable font sizes and mobile navigation. **P1**
31. Review render-blocking CSS/JS only where evidence shows meaningful savings. **P2**
32. Keep key service copy and internal links crawlable in semantic HTML. **P1**
33. Verify HTTPS and mixed-content behavior. **P0**

## D. On-page intent & content architecture

34. Check every priority page has one clear primary intent. **P1**
35. Check one descriptive H1 per priority page. **P1**
36. Check title accurately describes the page and matches user intent. **P1**
37. Check meta description supports CTR without stuffing. **P2**
38. Add a concise answer-first block where it helps the user. **P2**
39. Check headings describe real subtopics rather than repeat keywords. **P2**
40. Ensure service pages answer what is offered, who it is for, where it applies and the next action. **P1**
41. Ensure airport pages include genuine pickup / route / service details, not only keyword text. **P1**
42. Ensure city/service-area pages have distinct customer value and real coverage. **P1**
43. Prevent mass-produced near-duplicate city pages / doorway patterns. **P0**
44. Check fleet pages use real vehicle/capacity information where relevant. **P2**
45. Check thin pages that overlap stronger pages for possible merge, expansion or redirect. **P2**
46. Check informational articles do not cannibalize commercial service pages. **P1**
47. Add useful internal links from informational resources to the correct money page. **P1**

## E. Local SEO & business consistency

48. Review Google Business Profile business name, category choices, services, phone, website and service-area information for accuracy. **P1**
49. Compare website business information with major legitimate profiles/citations. **P1**
50. Flag conflicting business name / address / phone data. **P1**
51. Review whether local landing pages match real service coverage. **P1**
52. Review genuine fleet, team and service photography opportunities. **P2**
53. Review how customers are asked for legitimate reviews; never incentivize or fabricate reviews. **P1**
54. Review response process for genuine customer reviews. **P2**
55. Identify industry/local citation gaps that are actually relevant to the operator. **P2**
56. Identify local partner / venue / travel / business relationships that could create legitimate mentions. **P2**

## F. Structured data & entity clarity

57. Validate Organization schema where appropriate. **P2**
58. Validate WebSite / WebPage relationships where used. **P2**
59. Use Service schema only for services genuinely described on the page. **P2**
60. Use LocalBusiness schema only when the business facts are accurate and applicable. **P2**
61. Validate BreadcrumbList where breadcrumbs exist. **P2**
62. Do not fabricate `AggregateRating`, reviews, prices, locations or service facts. **P0**
63. Keep structured-data claims consistent with visible page content. **P1**
64. Validate markup after deployment and re-check in URL Inspection where useful. **P2**

## G. Authority, citations & backlink quality

65. Inventory referring domains / known inbound links using available tools. **P2**
66. Separate relevant industry/editorial mentions from low-value directories. **P2**
67. Check whether important service pages have any contextual third-party mentions. **P2**
68. Identify real client implementation pages that could support a natural attribution. **P2**
69. Identify real booking/dispatch/CRM/payment vendor relationships suitable for a case study. **P2**
70. Identify transportation-industry publications, associations and supplier directories where TLMA/operator participation is legitimate. **P2**
71. Avoid bulk backlink packages, PBNs, automated guest posts and exact-match anchor schemes. **P0**
72. Prefer links that would still be valuable if Google ignored the ranking effect. **P2**

## H. GEO / AI-search readiness

73. State the business entity, services and service areas clearly and consistently. **P2**
74. Give important customer questions concise direct answers before deeper detail. **P2**
75. Keep important facts crawlable and visible, not only inside decorative UI. **P1**
76. Link supporting pages so entity/service relationships are understandable. **P2**
77. Add source links and methodology to research/comparison assets. **P2**
78. Avoid claiming guaranteed inclusion in AI Overviews, ChatGPT, Gemini, Perplexity or other answer systems. **P0**

## I. Booking / conversion path

79. Confirm the primary CTA is obvious on priority organic landing pages. **P1**
80. Confirm mobile users can call, request a quote or start booking without hunting. **P1**
81. Check form fields are necessary and usable. **P2**
82. Check booking links/forms reach the intended workflow without dead ends. **P0**
83. Check service/location pages route users to the correct quote or booking action. **P1**
84. Review trust content near conversion points: service facts, policies, real proof and contact information. **P1**

## J. Measurement & prioritization

85. Verify Search Console is collecting data. **P1**
86. Verify GA4 / GTM setup if used. **P1**
87. Verify meaningful conversion events: form submit, call action, booking/demo click and completed booking where technically measurable. **P1**
88. Check query-to-page ownership in GSC. **P1**
89. Check page cannibalization before creating new URLs. **P1**
90. Separate impressions/rankings from actual business outcomes. **P1**
91. Record a baseline before major changes. **P2**
92. Re-check indexing, crawl status and query ownership after deployment. **P2**

# Audit output template

Each completed audit should end with four short outputs:

### 1. Executive diagnosis
Example structure: `Indexing is clean; the main growth constraint is local authority + weak airport/service architecture + untracked booking actions.`

### 2. Priority queue
- P0 blockers
- P1 revenue / visibility
- P2 growth
- P3 enhancements

### 3. URL ownership map
`Keyword / intent | Current URL | Intended owner | Conflict | Action`

### 4. 30-day action plan
Week 1: blockers + indexing  
Week 2: money pages + local accuracy  
Week 3: authority + content gaps  
Week 4: measurement + validation

# Linkable-asset page brief

## Recommended title
`Limo SEO Audit Checklist: 90+ Technical, Local & Booking Checks`

## Recommended meta description
`Use this limo SEO audit checklist to review indexing, local SEO, service and airport pages, site speed, authority, structured data and booking conversion.`

## Recommended H1
`The Limo SEO Audit Checklist: From Google Visibility to Booked Rides`

## Recommended page structure
1. Direct answer
2. How to use the checklist
3. Severity system
4. 90+ checklist grouped by audit area
5. Download / copy checklist option (future)
6. Common limo-specific red flags
7. Example audit output
8. Sources / methodology
9. CTA: Free Growth Audit

## Internal links
- `/seo-for-limo-companies.html` — commercial service owner
- `/limo-website-design.html` — performance / conversion implementation
- `/booking-systems.html` — booking-path implementation
- `/resources.html` — content hub
- `/case-studies-results.html` — verified examples only

## Schema plan when published
- `Organization`
- `WebSite`
- `WebPage`
- `Article` if the final page is editorial/resource content
- `BreadcrumbList`

Do not add FAQ schema merely because the page contains questions. Do not add ratings or review markup without valid visible evidence.

## Proof / evidence requirements

Before publication:
- use only checks TLMA can explain and execute;
- cite official Google documentation for technical guidance;
- clearly label TLMA methodology vs Google requirements;
- include a visible “last reviewed” date only when the content is actually reviewed;
- do not use invented benchmark percentages or ranking timelines;
- do not claim a fixed word count, review count or city-page count as a Google requirement.

## Release gate

Publish only when:
1. the indexing watch shows healthier discovery of the existing architecture, **or** the asset has a concrete outreach/link opportunity that justifies release;
2. the asset has a distinct intent and does not compete with `/seo-for-limo-companies.html`;
3. sources and methodology are complete;
4. internal links and CTA are ready;
5. the final production page passes the same technical audit used elsewhere on TLMA.

## Immediate outreach use

Even before public release, this brief can support outreach preparation. Once published, suitable outreach targets are:
- real limo/chauffeur clients that receive an audit;
- transportation-industry publications covering digital growth;
- booking/dispatch vendors whose customers need website/search guidance;
- relevant supplier directories / associations where educational resources are allowed;
- local-business / travel marketing publications discussing service-area SEO.

The pitch is the **checklist's utility**, not “please give us a backlink.”