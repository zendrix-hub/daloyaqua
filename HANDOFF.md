# HANDOFF — DaloyAqua

> The single source of truth for continuing this work. If you are an AI agent (Claude, Codex, Gemini, or another) or a new collaborator, **read this file first, then `README.md`, then `docs/03-sdlc.md`.** Update the session log before you finish.

## Snapshot
| | |
|---|---|
| **Last updated** | 2026-11-08 |
| **Phase (SDLC)** | **0 — Research / Discover** |
| **Product stage** | S0 Family Farm Logbook (`v0.1`, *built with Mother's taohan turnover split & Spec 003 quality fields, not yet deployed*) |
| **Founder** | "Cowboy" (IT). Final semester in Cebu, graduating Jan 2027; interning at a Japanese company, then plans to work in Japan |
| **Team** | Mother: reviews *taohan* copra sales & allocates family vs worker shares. Brother: registered agriculturist (agronomy, field). Sister: management accounting student (finance). See `docs/02-strategy/team-roles.md` |
| **Place** | Baleno, Masbate, Philippines (Bicol, Region V). Family land: coconut/copra, rice/corn, idle parcels; a fishpond is planned |
| **Repo** | github.com/zendrix-hub/daloyaqua (root flattened & cleaned; push from personal machine only, never from the NEC work laptop) |

## What exists
| File | Purpose |
|---|---|
| `README.md` | Overview, spec status table, repo map |
| `docs/00-brand.md` | Name meaning (*daloy* = flow): water, data, cash and knowledge; principles |
| `docs/01-research/round1–5.md` | Cited, vote-verified desk research, with the rejected claims listed (round 4 = co-op bookkeeping landscape; round 5 = ground-level copra *pesada*/moisture, *tersya* labor, named Baleno DA-SAAD groups & CDA `MC 2022-24` crosswalk) |
| `docs/02-strategy/lean-canvas.md` | v2 business model, ✅ evidence vs 🧪 hypothesis |
| `docs/02-strategy/funding-roadmap.md` | Who pays and which funding fits each stage, eligibility blockers, contact list |
| `docs/02-strategy/team-roles.md` | Roles, operating rhythm, decision rules |
| `docs/03-sdlc.md` | SDLC (Phase 0–7) + spec-driven development, stage gates S0–S3 |
| `docs/04-innovation.md` | Innovation log: idea → experiment → spec or parked |
| `docs/05-fieldwork/interview-guides.md` | Interview guides G1–G6 (Mom Test style) mapped to F1–F6; notes go in `docs/05-fieldwork/notes/` |
| `specs/001-farm-logbook/` | spec, plan, tasks: the v0.1 logbook (Mother's *taohan* turnover calculator) |
| `specs/002-mobile-entry/spec.md` | Draft: offline-first, assisted entry (waits for the S0 gate) |
| `specs/003-copra-sale-quality/spec.md` | Built into v0.1 (awaiting brother/sister review): copra moisture and deduction fields |
| `tools/baleno-farm-logbook-v0.xlsx` | The v0.1 logbook workbook (2,194 formula cells tested, 0 errors) |
| `personal/vgmo-v2.md` | Cowboy's VGMO (personal; Cowboy decides whether to publish it) |

**Source of truth:** this repository root (`daloyaqua/`). The legacy `backend/` and `frontend/` prototype folders and duplicate `solving/` files have been removed.

## Key decisions (and why)
1. **First atomic problem:** "We don't know what we earn per parcel and per copra sale." Copra price volatility and input costs are the top verified pain points (round 1).
2. **Spreadsheet before app.** PhilRice AgriDoc had low adoption (round 1). There's no build without proven use.
3. **Association first, not app first.** Pooled volume, the JA bookkeeping service, and community organizing all point to delivery through groups (rounds 2–3).
4. **Offline-first, assisted entry.** In Bicol, 34% of farmers have reliable internet and 81–82% struggle with digital tools (round 2).
5. **The paying customer is the co-op, buying COC-compliance bookkeeping.** Co-ops must file annual financial statements to keep their CDA Certificate of Compliance (round 3). Farmers are not the payers. Round 4: CDA provides rules, templates and an online-only portal, not bookkeeping help; the only verified co-op software (NATCCO eKoopBanker) reaches about 1.5% of co-ops and targets credit co-ops → a **plausible, unproven gap**. The chart of accounts should follow CDA MC 2022-24.
6. **The fishpond is on hold** until the water source (fresh or brackish) is checked. Pond economics are unverified.
7. **Siblings in the Philippines are the named applicants** for YFC and KAYA while Cowboy works in Japan (inference, round 3).
8. **Don't push to GitHub from the NEC work laptop.** It's behind a corporate proxy and has a company git email.

## Verified / refuted / open
- **Verified:** see each round file. Confidence labels are in the files.
- **🚫 Do not use (refuted):** "CFIDP funds computerized accounting for co-ops" (round 3) · "94% of farmers sell to traders while millers pay more" · "buyer credit lowers price" · "traders pay ₱7–8/kg less than oil mills" · "micro co-ops must encode reports online" · "JICA NINJA is a current program" · the SEAFDEC tilapia model figures · "CY2024 micro co-op Google Form filing" · "CDA hard copies no longer required" · "eKoopBanker doesn't do bookkeeping" · "CAFSIS system" · the PIDS rural internet and 3G coverage statistics (round 1).
- **Open (desk research could not answer):** DOST SETUP/TAPI · LGU and DA-SAAD budgets in Masbate · Landbank/SURE · what farmers pay for digital services · Masbate copra buyers and mills · Masbate connectivity · pond costs.

## Field-validation checklist (exit criteria for Phase 0)
Use the matching guide in `docs/05-fieldwork/interview-guides.md`: F1→G1, F2→G2, F3→G3, F4→G4, F5→G5.

| # | Hypothesis | How to check | Owner | Status |
|---|---|---|---|---|
| F1 | An on-site logger will log every transaction the same day | Ask; then measure over 30 days | Cowboy → brother | ☐ |
| F2 | Baleno copra buyers grade moisture by eye and take 14–22% deductions | Ask the buyer on 3 sales (I-001) | Brother | ☐ |
| F3 | Baleno associations struggle to produce their annual CAPR/FS and would pay or try help | Interview 1 association officer (I-004) | Sister | ☐ |
| F4 | LGU Baleno MAO has budget for association capacity building or a price board | Visit in person | Brother | ☐ |
| F5 | CocoFarmCoop/CFIDP is active in Masbate | Contact CDA Region V / PCA Masbate | Brother/sister | ☐ |
| F8 | **Key rule:** whether Baleno micro co-ops must pay an external auditor, and what it costs | G5 question 3a | Sister | ☐ |
| F9 | Baleno target groups are CDA-registered (not DOLE/SEC/LGU), so COC pain applies | G3 question 2, G4 | Brother/sister | ☐ |
| F6 | The fishpond parcel has reliable fresh water | Site check + BFAR consult | Brother | ☐ |
| F7 | Siblings' ages and RSBSA status qualify for YFC/KAYA | Ask | Cowboy | ☐ |

## Next actions (in order)
1. **Cowboy:** upload `tools/baleno-farm-logbook-v0.xlsx` (now v0.1) to Google Sheets; confirm spec 001 AC5 (formulas calculate in Google Sheets). *(Repo upload & cleanup done 2026-11-06; v0.1 updated 2026-11-08.)*
2. **Cowboy → Mother & brother:** run G1 (10-min call): show how `Sales` calculates Mother's exact turnover allocation (`Net after transport` → `Taohan Share (₱)` → `Our Family Share (₱)`) when the *taohan* turns over a sale (`F1`).
3. **Cowboy + Mother + brother:** 30-minute call to fill in Parcels from Google Maps; delete the example rows; enter 1 real past copra sale turnover from Mother's records → spec 001 is **deployed**.
4. **Brother + sister:** review Spec 003 columns (`M:O` in `Sales`) and the `MC 2022-24` chart-of-accounts crosswalk in `docs/01-research/round5.md`.
5. **Brother (+ *taohan*):** F2 on the next copra sale (`G2`); F4 visit to LGU Baleno MAO.
6. **Sister:** F3 association interview (starting with **Maluy-a Proper Farmers Association** in Obongan Diot, **Madancalan FA**, or **Maan FFA**).

## Rules for AI agents
1. **Phase discipline:** we are in Research. Don't propose building new software until the Phase 0 exit criteria in `docs/03-sdlc.md` are met. Ideas go to `docs/04-innovation.md`.
2. **No build without a spec.** Follow `docs/03-sdlc.md`: spec.md → plan.md → tasks.md.
3. **Evidence:** cite a source URL for every factual claim. Mark hypotheses 🧪. **Never present a claim from the 🚫 list above as fact.** Prefer adversarial verification for new research.
4. **Regression values for the logbook** (must stay true after any change): 250 kg × ₱44 − ₱300 transport = **₱10,700** net, **₱42.80/kg**; parcel P1 profit **₱9,700**, **₱4,850/ha** on 2 ha.
5. **Spreadsheet formulas:** Excel-2007-era functions only (SUMIFS, INDEX/MATCH). MINIFS/MAXIFS need the `_xlfn.` prefix. No XLOOKUP/FILTER/UNIQUE.
6. **Tone:** call the founder **"Cowboy"**. Act as PM, agriculturist, senior IT, entrepreneur and researcher. Depth over hype; start small.
7. **Don't overwrite without looking.** Update status fields instead of deleting history.
8. **Before you finish:** update the Snapshot, the checklist statuses, Next actions, and add a Session log entry below.

## Session log
| Date | Who | What |
|---|---|---|
| 2026-11-04 | Claude + Cowboy | Round 1 deep research (problem discovery). Picked the first atomic problem. Built and formula-tested the v0 logbook xlsx. Rewrote the VGMO (v2). |
| 2026-11-05 | Claude + Cowboy | Push blocked by the NEC proxy; manual upload chosen. Created the repo skeleton (brand, SDLC+SDD, specs 001–003, lean canvas). Rounds 2 (value chain, users, Japan, pond) and 3 (who pays, funding); round 3 refuted a round 2 CFIDP claim, and it was corrected. Validation pass: phase set to Research, spec 001 → built, not deployed. Added the innovation log, HANDOFF.md, CLAUDE.md/AGENTS.md. VGMO v2.1 adds Innovation. |
| 2026-11-05 | Claude + Cowboy | Gap analysis. Wrote interview guides G1–G6 (`docs/05-fieldwork/`). Round 4 (co-op bookkeeping landscape): plausible, unproven gap; flagged that the micro-co-op audit rule is unresolved (round 3 note corrected). Added F8–F9 and ideas I-009, I-010. |
| 2026-11-06 | Antigravity + Cowboy | Cleaned and flattened repository root (`solving/daloyaqua/*` → `/`); removed legacy `backend/` (and tracked `venv`), `frontend/`, and duplicate `solving/` files; added root `.gitignore`. |
| 2026-11-08 | Antigravity + Cowboy | Research Round 5 (`docs/01-research/round5.md`): verified PCA AO 02 s. 2003 moisture rules (6% *resecada* base, ≥14% rejection) and village *pesada* deduction flow (*bawas sako* + *resiko*); identified the 3 Baleno DA-SAAD associations by name (`Maluy-a Proper FA`, `Madancalan FA`, `Maan FFA`) and Masbate→Legazpi/Lucena/Cebu copra routes; mapped Spec 001 `Lists` to CDA `MC 2022-24` (`50000`/`60000` series) and verified `Pinoy Coop Core` and `CoopBase` target credit co-ops. Cowboy shared the ground-truth Baleno workflow: the *taohan* cooks, transports, and bargains the copra, then turns over the sale to **Mother** to review and allocate between the family and the *taohan*. Updated `tools/baleno-farm-logbook-v0.xlsx` (v0.1), `Spec 001`, `Spec 003`, `team-roles.md`, and `interview-guides.md` to match Mother's turnover workflow and pass all formula/regression checks. |
