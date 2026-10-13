# TLMA Verified Capability Proof Pack — 2026-10-13

Purpose: document technical capability evidence that can support future authority/case-study content without turning implementation artifacts into unsupported business-performance claims.

## Publication status

**Safe for anonymous capability proof:** YES

**Safe for named-client promotion:** NO, not until the relevant client proof ledger entry is VERIFIED for public-use permission and exact claim wording.

---

## 1. Limo booking-flow implementation

Evidence repository: `osamaghaffar-the-specialist/nyc-lux-ride-booking-portal`

Source: `SETUP.txt`

Verified implementation scope documented in the repository:
- One Way booking flow
- enhanced Round Trip flow with separate outbound and return sections
- Hourly booking flow
- USA-only Google Places autocomplete
- Google Routes distance and ETA
- route map on review step
- additional stops
- international phone selector and validation
- customer contact form
- backend connection through a Supabase Edge Function
- booking persistence into `bookings` / `booking_stops`
- real request-code response for the success experience

### Safe authority claim
TLMA has implementation evidence for a limo-specific booking flow that handles multiple ride types, routing/location inputs, structured customer data and a Supabase-backed booking handoff.

### Do not claim from this evidence alone
- increased bookings
- increased revenue
- improved conversion rate
- reduced admin time by a percentage
- client satisfaction/testimonial

---

## 2. Secure booking finalization / persistence

Source: `FINAL-BOOKING-PERSISTENCE-V1-README.txt`

Verified behavior documented in the repository:
- browser sends a draft booking id and token;
- token is SHA-256 hashed server-side;
- server matches the existing draft row;
- saved trip/customer/vehicle data is validated;
- frozen pricing snapshot is validated against selected vehicle, trip type, estimated fare and currency;
- the same booking row transitions to `awaiting_payment` instead of inserting a duplicate row;
- request code, booking id, selected vehicle and pricing snapshot remain intact;
- Stripe checkout was intentionally not included in this V1 stage.

### Safe authority claim
TLMA has implementation evidence for server-validated booking-state progression that preserves the same booking record and validates the stored pricing context before finalization.

### Do not claim
Do not say online payment is implemented by this V1 evidence; the source explicitly says Stripe checkout is not included in that version.

---

## 3. Customer-visible pricing snapshot

Source: `PRICING-SNAPSHOT-V1-README.txt`

Verified behavior documented in the repository:
- structured pricing snapshot is persisted with a booking draft;
- snapshot includes version, source, capture time, vehicle, trip type, pricing mode, currency, customer total and raw pricing;
- server validates the snapshot object and size;
- autosave without valid pricing does not erase an existing snapshot;
- snapshot is historical/customer-visible data;
- final/payment pricing still requires server-side verification.

### Safe authority claim
TLMA has implementation evidence for preserving the exact pricing context shown during vehicle selection while keeping final price verification as a server-side responsibility.

### Do not claim
Do not call the snapshot itself a payment record or proof of completed revenue.

---

## 4. SEO measurement capability

Current TLMA production setup verified on 2026-10-13:
- Google Search Console property connected;
- 21 production URLs tracked for indexing;
- sitemap and robots discovery configured;
- GA4 property and web stream connected;
- successful lead flow verified through GA4 DebugView;
- `form_start` and `generate_lead` were observed during a live test;
- `generate_lead` still needs to propagate into standard GA4 Events reporting and be starred as a Key Event.

### Safe authority claim
TLMA measures crawl/indexing state, search visibility and successful form completions instead of relying only on rank screenshots.

### Do not claim
Do not report GA4 lead totals as production lead volume until non-debug/live reporting has accumulated and the key-event setup is confirmed.

---

## 5. Google Ads reporting evidence

The TLMA proof page contains anonymized Google Ads account screenshots with interface-level metrics including combinations of:
- clicks
- impressions
- conversions
- cost per conversion
- conversion rate
- conversion value
- spend

### Safe authority claim
TLMA can demonstrate Google Ads reporting/account evidence where conversion measurement is present.

### Required caveat
Google Ads `Conversions` and `Conversion value` depend on the actions and values configured in the account. Conversion value must not be presented as verified booked revenue unless separately reconciled with booking/payment data.

---

# Evidence-to-publication matrix

| Evidence | Anonymous capability proof | Named client story | Quantified business result |
|---|---|---|---|
| Booking-flow repository | YES | Permission required | KPI evidence required |
| Secure persistence docs | YES | Permission required | KPI evidence required |
| Pricing snapshot docs | YES | Permission required | KPI evidence required |
| Search Console / GA4 setup | YES for TLMA's own measurement method | N/A unless client-specific | Production data required |
| Anonymized Google Ads screenshots | YES with caveats | Account/client permission required | Metric definition + attribution required |
| Client testimonial | NO unless permission recorded | Permission required | Not performance proof by itself |

# Next proof milestone

The highest-value authority upgrade is one fully VERIFIED limo client case study with:
1. written public-use permission;
2. exact work scope;
3. approved screenshots/logo use;
4. KPI source and date range;
5. clear baseline/comparison definition;
6. approved public wording.

Until then, TLMA should win trust through implementation depth, transparent measurement and evidence discipline rather than inflated results claims.
