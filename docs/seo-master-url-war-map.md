# TLMA Master URL & Keyword War Map

**Property:** https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/  
**Baseline:** GSC settled data through 2026-10-06; fresh URL Inspection run 2026-10-10.  
**Purpose:** Give every indexable URL one clear job before creating, merging, redirecting, or geographically splitting pages.

## Rules

1. One primary commercial intent per money page. Supporting variants may map to the same URL when the search intent is materially the same.
2. The homepage owns the **agency/category** intent (`limo marketing agency`, broad `limousine marketing`), not specialist service queries such as `limo SEO` or `limo Google Ads`.
3. Specialist service pages own their service families: SEO, Google Ads, website design, booking systems, GEO/AI Search, social media.
4. Industry pages support entity/vertical relevance. They must not simply duplicate the homepage or service pages.
5. Informational articles may support a service topic but must not compete with the commercial service page for the same primary query.
6. Hub pages (`services.html`, `industries.html`, `resources.html`) organize discovery and internal linking; they are not substitutes for their child money pages.
7. Legal, contact and about pages are not keyword acquisition targets.
8. Do not create `/us/` or `/uk/` clones until the existing architecture is sufficiently discovered/indexed and the keyword gap is validated.
9. Do not target `dispatch software` on the booking page unless the product capabilities genuinely support that intent.
10. Do not invent case-study outcomes, ratings, testimonials, client counts, pricing or update dates.

## Current 21-URL Map

| URL | Page role | Primary keyword / intent owner | Supporting keyword family | Intent / funnel | Market role | 90d GSC signal | Fresh index status | Decision | Cannibalization guardrail | Priority |
|---|---|---|---|---|---|---|---|---|---|---|
| `/` | Homepage / category money page | **limo marketing agency** | limousine marketing; limo marketing services; black car/chauffeur growth overview | Commercial / BOFU | Global, strongest current US signal | 15 impressions, avg pos 36.7 | Indexed | **KEEP + OPTIMIZE** | Do not make homepage the primary SEO/Ads/website/booking page. Link to specialist pages with descriptive anchors. | P1 |
| `/about.html` | Entity / trust page | Brand/entity intent only | The Limo Marketing Agency; company/about intent | Navigational / trust | Global | — | Unknown to Google | **KEEP** | No generic money-keyword targeting. | P3 |
| `/airport-transportation-companies.html` | Industry money/support page | **airport transportation marketing** | airport transfer marketing; airport transportation SEO; airport Google Ads; route demand | Commercial / BOFU | Global; US first | — | Unknown to Google | **KEEP + VALIDATE DEMAND** | Own the airport-operator vertical, not generic Google Ads/SEO queries. | P2 |
| `/black-car-services.html` | Industry money/support page | **black car service marketing** | black car marketing agency; black car SEO; black car Google Ads | Commercial / BOFU | US-led | Homepage currently has 2 impressions for `black car service marketing` | Unknown to Google | **KEEP + OPTIMIZE AFTER DISCOVERY** | Once indexed, this page should own black-car-specific marketing intent; homepage remains category/agency page. | P1 |
| `/booking-systems.html` | Product/service money page | **limo booking software** | limo booking system; limousine booking software; limo reservation/booking workflow | Commercial / BOFU | US/global | 1 impression, avg pos 8 | Indexed | **KEEP + OPTIMIZE** | Do not broaden into dispatch-software claims unless functionality supports them. | P1 |
| `/case-studies-results.html` | Proof / conversion asset | **limo marketing case studies** | limo marketing results; Google Ads examples; website/booking examples | Commercial investigation / BOFU | Global | — | Unknown to Google | **KEEP** | Evidence page, not a generic service page. Use verified proof only. | P2 |
| `/chauffeur-companies.html` | Industry money/support page | **marketing for chauffeur companies** | chauffeur marketing; chauffeur SEO; chauffeur Google Ads; executive/airport demand | Commercial / BOFU | UK/global relevance | — | Unknown to Google | **KEEP + VALIDATE DEMAND** | Own chauffeur-specific vertical context; do not duplicate global homepage/service copy. | P2 |
| `/contact.html` | Conversion / contact page | Brand contact intent only | contact TLMA; consultation | Navigational / BOFU | Global | — | Unknown to Google | **KEEP** | No acquisition keyword target. | P3 |
| `/geo-ai-search-optimization.html` | Specialist service money page | **GEO / AI search optimization for limo companies** | generative engine optimization; AI search visibility; AEO/GEO for limo companies | Commercial / MOFU-BOFU | Global | 9 impressions, avg pos 53; 5 from unrelated `aviation search engine optimization` query | Indexed | **KEEP + DEEP OPTIMIZE** | Keep AI/GEO intent distinct from traditional SEO page; reduce ambiguous aviation relevance if content causes it. | P1 |
| `/google-ads-for-limo-companies.html` | Specialist service money page | **Google Ads for limo companies** | limo service Google Ads; limo PPC; limousine Google Ads | Commercial / BOFU | US/global | 18 impressions, avg pos 64.8; 17 impressions for `limo service google ads` | Indexed | **KEEP + OPTIMIZE** | Own commercial paid-search service queries. Articles must link here and stay informational. | P1 |
| `/industries.html` | Industry hub | **No standalone money keyword required** | limo/chauffeur/black car/airport industries overview | Navigational / MOFU | Global | — | Unknown to Google | **KEEP AS HUB** | Avoid competing with homepage and child industry pages for generic `limo marketing` terms. | P2 |
| `/limo-website-design.html` | Specialist service money page | **limo website design** | limousine website design; limo company website design services; conversion-focused limo websites | Commercial / BOFU | US/global | 6 impressions, avg pos 44.5 | Indexed | **KEEP + OPTIMIZE** | This page owns design/development intent; homepage only summarizes. | P1 |
| `/limousine-companies.html` | Industry money/support page | **marketing for limousine companies** | limousine company growth strategy; limo-company channel mix; booking growth | Commercial / BOFU | US/global | Homepage currently has 2 impressions for `limousine marketing` | Unknown to Google | **KEEP, BUT HOLD MAJOR REWRITE UNTIL DEMAND/INDEXING DATA** | Homepage owns broad `limo marketing agency` / `limousine marketing`; this page must stay vertical/use-case specific. Merge later only if it proves redundant. | P2 |
| `/privacy-policy.html` | Legal | No acquisition target | privacy policy | Navigational / legal | Global | — | Unknown to Google | **KEEP** | Do not optimize for commercial queries; not an indexing priority. | P4 |
| `/resources.html` | Content hub | **limo marketing resources** (hub intent) | Google Ads guides; SEO/GEO guides; booking/automation guides | Informational / TOFU-MOFU | Global | — | Unknown to Google | **KEEP AS HUB** | Child articles own informational queries; hub organizes discovery. | P2 |
| `/seo-for-limo-companies.html` | Specialist service money page | **SEO for limo companies** | limo SEO; limo company SEO; limo service SEO; SEO limousine company | Commercial / BOFU | US/global | 25 impressions, avg pos 69.6 | Indexed | **KEEP + HIGH-PRIORITY OPTIMIZE** | Dedicated SEO page must own SEO family. Homepage SEO overlap is being reduced via contextual internal linking; wait for recrawl before heavier edits. | P1 |
| `/services.html` | Service hub | **limo marketing services** | Google Ads; SEO; GEO; web design; booking systems; automation | Commercial investigation / MOFU | Global | — | Unknown to Google | **KEEP AS HUB** | Do not target `limo marketing agency` more aggressively than homepage or exact specialist terms more aggressively than child pages. | P2 |
| `/social-media-marketing-for-limo-companies.html` | Specialist service page | **social media marketing for limo companies** | limo social media management; chauffeur/black car social media | Commercial / BOFU | Global | — | Unknown to Google | **KEEP + VALIDATE DEMAND** | Own social-media service intent only. | P3 |
| `/terms.html` | Legal | No acquisition target | terms and conditions | Navigational / legal | Global | — | Unknown to Google | **KEEP** | Not an indexing/ranking priority. | P4 |
| `/why-limo-google-ads-get-expensive.html` | Diagnostic article | **why limo Google Ads get expensive** | limo Google Ads cost; expensive limo PPC; wasted ad spend diagnosis | Informational / MOFU | US/global | — | Unknown to Google | **KEEP + DISCOVERY SUPPORT** | Do not optimize this article for the primary commercial `Google Ads for limo companies` query. Link users to the service page. | P2 |
| `/how-much-should-limo-company-spend-google-ads-2026.html` | Budget article | **limo Google Ads budget** | how much should a limo company spend on Google Ads; limo advertising budget; limo PPC budget | Informational / MOFU | US/global | 6 impressions, avg pos 33.7; 3 impressions for `limo service google ads` | Indexed | **KEEP + OPTIMIZE** | Budget intent stays informational; commercial service page owns `Google Ads for limo companies`. | P1 |

## Current Cannibalization Decisions

### 1. Homepage vs SEO service page
- Observed overlap: `limo seo` and `seo limousine company` surfaced both URLs.
- **Owner:** `/seo-for-limo-companies.html`.
- Homepage remains the agency/category page.
- First corrective signal already implemented: homepage contextual card now uses `Limo SEO` + `Explore Limo SEO Services` and points to the specialist page.
- **Next action:** wait for fresh crawl/indexing data before removing additional homepage mentions.

### 2. Google Ads service vs budget article
- `limo service google ads` produced 17 impressions on the service page and 3 on the budget article.
- **Owner:** `/google-ads-for-limo-companies.html` for commercial service intent.
- `/how-much-should-limo-company-spend-google-ads-2026.html` owns budgeting/informational intent.
- **Decision:** no aggressive consolidation now; intent separation is defensible.

### 3. Homepage vs limousine industry page
- Homepage currently surfaces for `limousine marketing`; `/limousine-companies.html` is still unknown to Google.
- **Owner:** homepage for broad agency/category intent.
- Industry page should focus on limousine-operator use cases and growth strategy, not duplicate the homepage.
- **Decision:** keep page, but do not expand it until indexing and keyword-demand evidence is available.

### 4. Homepage vs black-car industry page
- Homepage currently has impressions for `black car service marketing` while `/black-car-services.html` is unknown to Google.
- **Intended owner after discovery:** `/black-car-services.html` for black-car-specific marketing intent.
- **Decision:** keep homepage as broad category page; strengthen child-page discovery rather than rewriting both pages at once.

## Current Indexing Reality

Fresh URL Inspection on 2026-10-10 showed **7 of the 21 sitemap URLs indexed** and **14 reported as `URL is unknown to Google`**.

Indexed set:
- `/`
- `/booking-systems.html`
- `/geo-ai-search-optimization.html`
- `/google-ads-for-limo-companies.html`
- `/limo-website-design.html`
- `/seo-for-limo-companies.html`
- `/how-much-should-limo-company-spend-google-ads-2026.html`

The sitemap has been resubmitted after adding per-URL `lastmod` values. Indexing is being monitored separately. Do **not** interpret sitemap submission as an indexing guarantee.

## Next Keyword Gap Phase

After this architecture is locked, build the external keyword war map in this order:

1. **US money gaps:** limo marketing, limo SEO, limo Google Ads, limo website design, limo booking system/software, black car marketing.
2. **US booking/software support:** reservation/booking/management terms only where product capability matches intent.
3. **UK commercial gaps:** taxi booking software/system, taxi dispatch system/pricing/comparison, chauffeur growth and booking-stack intent.
4. Map every validated keyword to exactly one existing or proposed URL.
5. Only then approve `NEW` URLs. Country folders such as `/us/` and `/uk/` remain provisional until demand + indexing evidence justifies them.

## Status Key

- **KEEP:** URL role is defensible; preserve it.
- **OPTIMIZE:** same URL should be improved for its assigned intent.
- **VALIDATE DEMAND:** page is structurally useful but keyword demand needs confirmation before major investment.
- **HUB:** discovery/internal-link page; not the primary owner of child money terms.
- **MERGE / REDIRECT:** not assigned yet. No existing URL has enough evidence to justify destructive consolidation at this stage.
