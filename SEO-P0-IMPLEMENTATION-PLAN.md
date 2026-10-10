# SEO / GEO P0 Foundation

Date: 2026-10-10

This branch normalizes the homepage entity URL and core technical SEO/GEO signals before content expansion.

## Locked canonical convention

Primary homepage URL:
`https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/`

`/index.html` remains a physically served GitHub Pages file, but must not be presented as the preferred canonical homepage URL.

## P0 scope

1. Homepage canonical, Open Graph URL and structured-data entity IDs use the clean root URL.
2. Sitemap lists the clean root URL once and does not list `/index.html` as a separate homepage.
3. Internal Home/logo links point to the clean homepage path instead of `index.html` where practical.
4. Breadcrumb Home items use the clean root URL.
5. WebPage `isPartOf` points to a WebSite entity; Service `provider` continues to point to Organization.
6. Booking Systems receives complete metadata / structured-data parity with the other core service pages.
7. No fabricated reviews, ratings, client outcomes, locations, addresses or pricing are added.
