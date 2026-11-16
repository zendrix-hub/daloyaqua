# Spec 001 — Family Farm Logbook

**Status:** built (v0.1 with Mother's turnover allocation & Spec 003 quality fields, 2026-11-08; AC5/AC6 pending) · **Stage:** S0 · **Role in Research phase:** research instrument for Baleno price and cost data · **Owner:** Cowboy · **Reviewers:** Mother (sale turnover & allocation), brother (agronomy), sister (accounting)

## Problem
"We don't know what we actually earn per parcel and per copra sale."
Evidence: copra farmgate price volatility (₱12–58/kg, 2019–2025) and high input costs are the top verified pain points. No Baleno copra price data exists. See `docs/01-research/round1.md` and `docs/01-research/round5.md`.

## Users
- **Mother (Sale Reviewer & Allocator):** receives the receipt (*pesada*) and cash turnover from the *taohan* (who cooked, transported, and bargained the copra), calculates and reviews the sale, and allocates the proceeds between our family and the *taohan*.
- **On-site logger** (Mother or brother): records the sale row right at Mother's turnover calculation, plus standalone expenses on the `Costs` sheet.
- **Cowboy:** reviews weekly, maintains the tool.
- **Sister:** reviews profit per parcel and chart of accounts monthly.

## User stories
1. As Mother / the logger, when the *taohan* turns over a sale, I record one row on `Sales` (date, parcel, crop, net kg paid, ₱/kg, buyer, transport cost, and the *taohan* share allocated by Mother) in under 2 minutes, and immediately see `Gross (₱)`, `Net after transport (₱)`, and `Our Family Share (₱)`.
2. As the logger, I record standalone farm expenses not deducted inside a sale turnover (fertilizer, tools, clearing, seeds) on `Costs` in under 2 minutes.
3. As the family, we see net income, total costs (including *taohan* shares + standalone parcel costs), our family profit, and profit per hectare for each parcel.
4. As the family, we see our copra price & turnover history: count, kg, weighted average, net after transport, lowest and highest, total *taohan* share, our family share, and average net ₱/kg by moisture grading method (`Spec 003`).
5. As the sister, I can edit cost categories (aligned with CDA `MC 2022-24`) without touching formulas.

## Acceptance criteria
- AC1: Gross = kg × ₱/kg; Net = Gross − transport; Net ₱/kg = Net ÷ kg; Our Family Share = Net − Taohan Share. *(Tested: 250 kg × ₱44 − ₱300 = ₱10,700 → ₱42.80/kg; minus ₱1,000 Taohan Share = ₱9,700 Our Family Share ✅)*
- AC2: Summary profit per parcel = sales net − (taohan shares + standalone parcel costs). *(Tested: P1 = ₱10,700 − ₱1,000 = ₱9,700; ₱4,850/ha on 2 ha ✅)*
- AC3: Standalone costs without a valid Parcel ID show up as "Unassigned costs". *(Tested: ₱250 unassigned example row ✅)*
- AC4: Parcel, crop, category, buyer, and moisture method fields offer dropdowns. ✅
- AC5: Opens and recalculates in Google Sheets. ⏳ Cowboy to confirm after upload.
- AC6 (usage): 90 days of logging with ≥80% of transactions captured. ⏳ Stage S0 gate.

## Non-goals
Mobile app, multiple farms, weather, inventory, harvest forecasting, pond monitoring. Each one waits for its own spec.

## Open questions
- Will Mother log directly in Google Sheets during the *taohan* turnover, or will brother encode Mother's turnover calculation the same day? (`F1` / `G1`)
- Should rice and corn also be logged in kg, or in cavans? (brother to decide)
