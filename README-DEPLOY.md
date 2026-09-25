# The Limo Marketing Agency - GitHub Pages Ready

## Main deployment files
Upload everything in this folder to the root of your GitHub repository.

GitHub Pages entry page:
- index.html

GitHub Pages custom error page:
- 404.html

## Clean production filenames
- index.html
- services.html
- booking-systems.html
- google-ads-for-limo-companies.html
- seo-for-limo-companies.html
- geo-ai-search-optimization.html
- limo-website-design.html
- social-media-marketing-for-limo-companies.html
- case-studies-results.html
- industries.html
- limousine-companies.html
- chauffeur-companies.html
- black-car-services.html
- airport-transportation-companies.html
- about.html
- contact.html
- resources.html
- why-limo-google-ads-get-expensive.html
- privacy-policy.html
- terms.html
- thank-you.html
- 404.html

## What was integrated
- Latest approved versions were copied to clean filenames.
- Internal aliases were normalized.
- Main CTAs route to the correct page.
- Service cards now route to relevant service pages.
- Industry pages are connected to the Industries hub and the rest of the site.
- A compact site-wide directory was added so every major page is reachable.
- Dead `href="#"` article buttons were removed.
- The published Google Ads resource article is connected from Resources.
- Internal implementation copy was removed from the Contact privacy/meeting text.
- External links open safely in a new tab.
- GitHub Pages `.nojekyll` and `robots.txt` were added.

## Important form note
GitHub Pages is static hosting. It cannot receive consultation form submissions by itself.

This bundle centralizes consultation intent into `contact.html`, but the final Contact form still needs a real form endpoint before public launch, such as:
- Formspree
- Web3Forms
- your own Supabase / serverless endpoint
- another CRM/email form endpoint

Once that endpoint is supplied, connect the Contact form and redirect successful submissions to `thank-you.html`.

## Before final SEO launch
When the real production domain is known:
1. replace relative canonical URLs with the final absolute domain URLs;
2. generate sitemap.xml using that domain;
3. add the sitemap URL to robots.txt;
4. connect GA4 / GTM / Google Ads / Meta tracking IDs as required.
