# P2 Round 4 Live URL / Redirect / 404 Audit

Audit target: `https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/`

## Verified live behavior

- `https://.../the-limo-marketing-agency` returns **301** to the slash-root `https://.../the-limo-marketing-agency/`.
- `http://.../the-limo-marketing-agency/` returns **301** to HTTPS.
- Preferred root `/` returns **200** and canonicalizes to the clean slash-root URL.
- `/index.html` returns **200**, serves the exact same body hash as `/`, and canonicalizes to `/`.
- `/index` also returns **200**, serves the same homepage body, and canonicalizes to `/`.
- Query variants such as `/?utm_source=test` and `/index.html?utm_source=test` return **200** while canonicalizing to `/`.
- `/services.html` returns **200** with self-canonical `/services.html`.
- `/services` also returns **200** with identical body and canonical `/services.html`.
- `/seo-for-limo-companies.html` returns **200** with self-canonical `.html` URL.
- `/seo-for-limo-companies` also returns **200** with identical body and canonical `.html` URL.
- Trailing-slash file variants such as `/services/`, `/index.html/`, and `/seo-for-limo-companies.html/` return **404**.
- Uppercase path variant `/SEO-FOR-LIMO-COMPANIES.HTML` returns **404**.
- A random nonexistent URL returns a real **404** and uses the custom 404 page with `noindex,follow`.
- Direct `/404.html` returns **200** (normal for directly requesting the physical custom 404 file) but carries `noindex,follow`.
- `/thank-you.html` returns **200** with `noindex,follow`.
- `/robots.txt` returns **200**.
- `/sitemap.xml` returns **200**.

## Homepage equivalence

- `/` and `/index.html` SHA-256 body hashes are identical.
- Both expose canonical `https://osamaghaffar-the-specialist.github.io/the-limo-marketing-agency/`.

## Decision

No production redirect or 404 code change is justified on GitHub Pages in this round. GitHub Pages exposes extensionless aliases for `.html` files, but the site already sends consistent canonical signals, uses the preferred URLs internally/sitemap-side, correctly redirects HTTP to HTTPS and the bare project path to the slash root, and returns a genuine 404 for nonexistent paths.

Do **not** add JavaScript/meta-refresh redirects solely to force `/index`, `/index.html`, or extensionless aliases because that would add unnecessary client-side behavior and could create more risk than benefit. Continue monitoring Google Search Console for the exact duplicate-canonical URL before taking any stronger action.
