# TLMA — Free GitHub Repositories for SEO, Qualified Leads and Growth

**Research date:** 2026-10-23.  
**Scope:** The Limo Marketing Agency (US/UK limo, chauffeur, black car). GitHub Pages static site, Google Search Console, GA4, FormSubmit form/thank-you flow, Google Sheets/Apps Script potential, limited budget.  
**Action status:** RESEARCH ONLY. No repositories or packages installed, no credentials entered, no customer emails sent, no site changes in this research PR.

## The decision

**Ship small operational improvements, not a stack rebuild.** The agency already has relevant money pages, 12-point booking conversion audit, real GitHub Pages deployment, a consultation form, GSC and GA4. Its bottleneck is **verified delivered enquiries, credible proof/industry recognition and qualified sales conversations** — not an absence of software.

### Free does not mean zero operations cost

- **Free code license**: permits running/modification within license terms, but may require server, database, SMTP account, backups, integrations and/or disclosure obligations.
- **$0 startup implementation feasible today**: browser-side JS, Apps Script subject to free consumer quotas, and GitHub Actions standard runners on a *public* repo.
- **Self-hosted code but extra infrastructure**: capable CRM, chat/inbox, marketing automation, analytics and rank tools. **Do not** install these on GitHub Pages alone: GitHub Pages is static hosting.
- **Email/WhatsApp/Google Maps APIs**: vendor usage, privacy, anti-spam rules and potential costs apply separately; having MIT/Apache code does not make third-party sending or data APIs free.
- **Never** put tokens, prospect/customer personal data, CRM exports or email inbox content in the public website repository, public Actions artifacts or Pages.

## Tier A — high-fit, software-license-free, no monthly hosting required

| Repository | License verified 23 Oct | Role for TLMA | $0 deployment path / caveat | Priority |
|---|---|---|---|---|
| [googleworkspace/apps-script-samples](https://github.com/googleworkspace/apps-script-samples) | Apache-2.0 | Build **private** Gmail→Sheets lead CRM: ingest confirmed enquiry, dedupe, stage, follow-up due date, qualified operator flags, deal won/lost, weekly summary | Use Google Apps Script/Sheets quota; not a plug-and-play CRM. Need owner access to *actual* FormSubmit receiving inbox and verify forwarding/activation first. Official quotas: https://developers.google.com/apps-script/guides/services/quotas | **P0** |
| [GoogleChrome/lighthouse-ci](https://github.com/GoogleChrome/lighthouse-ci) | Apache-2.0 | Detect regression in SEO/headings, core technical page quality, Lighthouse performance/accessibility | GitHub Actions on public repo. Initial baseline must be realistic; external render/flaky timing should be retried; lab scores are **not** GSC rankings | **P0** |
| [microsoft/playwright](https://github.com/microsoft/playwright) | Apache-2.0 | Browser automation regression tests: nav/booking CTA, consultation field validation, mobile overlap; mock FormSubmit success and failure *without sending real form or creating fake GA4 leads* | GitHub Actions standard runners. Browser download/runtime and occasional flaky network need maintenance | **P0** |
| [lycheeverse/lychee-action](https://github.com/lycheeverse/lychee-action) / [lycheeverse/lychee](https://github.com/lycheeverse/lychee) | Apache-2.0 (lychee also MIT option) | Scheduled broken-link checker for 22 sitemap URLs, resources, CTA destinations, editorial links | GitHub Actions. Rate-limit/403/temporary outages must not be counted as confirmed broken links without follow-up | **P1** |
| [calcom/cal.diy](https://github.com/calcom/cal.diy) | MIT | Open-source appointment scheduling engine; useful functionality for **15-minute audit calls**, automatic timezone support | **Practical $0 route:** use [Cal.com free individual hosted plan](https://cal.com/pricing) for 1 scheduler, not self-hosting Cal.diy. Hosted provider terms apply; team functionality paid. Cal.com separated the production codebase into private managed code and Cal.diy open-source project **in April 2026**. Integrate verified booking URL after owner creates it; don't invent one | **P1** |
| [apify/crawlee](https://github.com/apify/crawlee) | Apache-2.0 | Controlled research of **public, permitted** operator website text to prepare individualized audit observations | Run locally/short approved Actions job; respect site terms, robots and rate limits, verify each finding manually; **not permission to scrape Google Maps or send mass unsolicited email** | **P2** |

GitHub standard runners free and unlimited for **public** repos per https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job (subject to current platform rules and abuse protections). TLMA repository currently public.

## Tier B — license free or open core but server/SMTP/operations required

| Repository | License | Value | Why NOT phase 1 |
|---|---|---|---|
| [krayin/laravel-crm](https://github.com/krayin/laravel-crm) | MIT | Full lead/contact/opportunity pipeline | Needs PHP/Laravel, DB, server hosting and maintenance; existing Sheets CRM cheaper initially |
| [espocrm/espocrm](https://github.com/espocrm/espocrm) | AGPL-3.0 | Leads, contacts, sales, opportunities and customizable workflows | PHP/DB/server, AGPL obligations for software modifications/network use; overbuilt for current near-zero organic leads |
| [frappe/crm](https://github.com/frappe/crm) | AGPL-3.0 | Open CRM focused on sales pipeline | Frappe stack hosting/admin effort |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | Mixed / project-specific, verify selected version | Modern extensible CRM | Server stack, possible non-uniform licensing/features; not $0 turnkey on GitHub Pages |
| [chatwoot/chatwoot](https://github.com/chatwoot/chatwoot) | MIT **community core**, enterprise proprietary | Inbound website chat/shared inbox/WhatsApp integrations | Rails, PostgreSQL, Redis, storage and 24/7 uptime needed; hosted WhatsApp messaging/provider/API fees may apply; **AI agent (Captain) is not free Community Edition**. Source https://www.chatwoot.com/community |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | MIT **core**, enterprise modules commercial | Visual automation/CRM and inbox workflows | Requires hosted workflow server; cloud and enterprise terms are distinct. Official https://www.activepieces.com/docs/about/license |
| [umami-software/umami](https://github.com/umami-software/umami) | MIT | Privacy-friendly events/campaign conversion analytics | Self-hosted DB/server; GA4 already connected and works, so redundant at this stage |
| [knadh/listmonk](https://github.com/knadh/listmonk) | AGPL-3.0 | Opt-in newsletter, segmentation and drip campaigns | Needs hosting, database and SMTP; should use **permissioned subscribers**, not scraped contacts or purchased cold-email lists |
| [towfiqi/serpbear](https://github.com/towfiqi/serpbear) | MIT | Search ranking monitoring | Server and SERP data scraping/third-party data services; anti-bot, regional accuracy, terms/cost issues; GSC remains free baseline |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | **Sustainable Use / fair-code, not OSI open source** | Workflow automation | Self-host may be free within license terms, but license limits and infrastructure are real; use Apps Script first |

## What should be built first

### P0. No lost lead / no fake lead system
- Confirm the website's actual **FormSubmit target Gmail account** receives real submitted enquiries. The currently connected agency Gmail account is different, so inspecting the connected mailbox does *not* verify the active recipient inbox.
- After owner authorization, set up **private** Google Sheets lead log and Apps Script inbox polling. Capture source URL/UTMs where available, submission date, email ID, business/site, service need, qualified state and owner assignment. De-duplicate messages by Gmail message ID plus appropriate fields. Keep private identifiers out of public repo and logs.
- Optional operator alerts and due-date reminders. **Never claim live delivery** based only on a GitHub code read or success event, and never send fake production enquiries to test without owner consent.
- Determine a compliant feedback response practice and consent; US/UK market and business data both matter.

### P0. Free website conversion protection with CI
- Add opt-in workflow on PR/manual run with Playwright for homepage/SEO/Google Ads/Services/Black Car/contact/mobile. Assertions: primary H1 is present, CTA destinations load, FormSubmit POST is mocked success/failure, failed send doesn't show success, thank-you event only fires after valid state, no mobile overflow.
- Run Lighthouse CI on at least homepage/contact/SEO/Google Ads with conservative budgets initially; avoid false failures and any published fake score claims.
- Run Lychee weekly with sensible external-request rate limits and explicit exclusions for links requiring login, JS and redirects.
- **No public API secrets or customer form data in screenshots/CI logs.**

### P1. Reduce time from enquiry to scheduled call
- Register one free individual Cal.com organizer. Create **15-minute Limo Growth / Booking Funnel Review** with local timezone auto-conversion. Share only its verified real booking URL.
- Include scheduling option on `thank-you.html` **after successful enquiry** once end-to-end form/email delivery and event attribution have been verified. Avoid bypassing lead tracking on initial main form.

### P1. First-party proof + earned backlinks
- Use actual de-identified request→operator quote/admin notification flow to make a useful walkthrough. Permission and metric publication are gated by `docs/client-proof-ledger.md`.
- Promote useful first-party audit to real editorial industry publications; no bulk backlink requests. Publication/backlink needs exact live referring URL verified.
- Engage 5 individual, human-reviewed US/UK operators per working day *only after* outreach sender, domain, privacy and opt-out practices are ready. Treat this as target activity, not guaranteed sales.

### P2. Conditional upgrades after a real pipeline exists
- Scale to a hosted CRM (Krayin, EspoCRM or Frappe) if Sheets cannot support follow-ups/owners, company records and reporting.
- Evaluate Chatwoot only when recurring inbound chat volume justifies server administration and response staffing.
- Evaluate opt-in Listmonk automation when the subscriber list and deliverability are established.
- **Do not** install Umami, SerpBear, n8n and Chatwoot just because Github stars are high.

## 14-day execution order (targets, not results)

| Days | Deliverable | Definition of done |
|---|---|---|
| 1–2 | Confirm form recipient and inbox delivery | Owner verifies receiving inbox and alert path; no silent destination switch |
| 2–4 | CI smoke and link checks on safe test branch | PR checks run successfully; mock tests don't email a rider, don't create fake GA4 events |
| 4–6 | Private Gmail→Sheets mini CRM | Real permitted inbox messages deduplicated; private sheet; no secrets exposed |
| 6–8 | Lighthouse baseline + mobile QA | Issues ranked by effect on visitor trust and conversion; no guarantee to achieve arbitrary score |
| 8–10 | Owner-created free 15-min scheduling link | Working verified URL and time-zone presentation; meeting workflow doesn't bypass lead accounting |
| 10–14 | Anonymized first-party case asset + five tailored website audits | Claims approved/traceable; no spammy outreach and no fictitious bookings |

## Evaluation scorecard

Measure **real qualified operator enquiries received**, **booked consultations**, **attended calls**, **proposal requests**, and **signed clients**. Separately measure 28-day GSC impressions/clicks, indexed URL states, real Google Organic sessions and UX QA failures. Attribute only with consent and reliable first-party evidence.

**Never confuse:** a tool's popularity with reliability; free code with zero hosting/usage cost; a test `generate_lead` event with a genuine prospect; a successful email-send API with a human response; an editorial pitch with a published backlink; crawlable with indexed; sample `PAID` UI with an actual card charge.

## Deferred security/operational gates

- Any new app/tool requires dependency review, license check, data/privacy impact review and rollback procedure.
- Public repo must never store Google API credentials, OAuth tokens, SMTP secrets, payment keys or personal customer records.
- Any new form endpoint or CRM migration is **owner-approved**, receives a controlled end-to-end test, and has a rollback path. DNS/email infrastructure preserved.
- Do not automate mass Google Maps collection or use insecure strangers' lead-scraper repositories with unreviewed exfiltration paths.
