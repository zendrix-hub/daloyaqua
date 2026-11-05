# Spec 001 — Family Farm Logbook

**Status:** built, awaiting deployment (v0 built 2026-11-04; AC5/AC6 pending) · **Stage:** S0 · **Role in Research phase:** research instrument for Baleno price and cost data · **Owner:** Cowboy · **Reviewers:** brother (agronomy), sister (accounting)

## Problem
"We don't know what we actually earn per parcel and per copra sale."
Evidence: copra farmgate price volatility (₱12–58/kg, 2019–2025) and high input costs are the top verified pain points. No Baleno copra price data exists. See `docs/01-research/round1.md`.

## Users
- **On-site logger** (brother or a parent): records sales and expenses the same day.
- **Cowboy:** reviews weekly, maintains the tool.
- **Sister:** reviews profit per parcel monthly.

## User stories
1. As the logger, I record a sale (date, parcel, crop, kg, ₱/kg, buyer, transport cost) in under 2 minutes.
2. As the logger, I record an expense (date, parcel, crop, category, item, amount, paid to) in under 2 minutes.
3. As the family, we see net income, costs, profit, and profit per hectare for each parcel.
4. As the family, we see our copra price history: count, kg, weighted average, net after transport, lowest and highest.
5. As the sister, I can edit cost categories (chart of accounts) without touching formulas.

## Acceptance criteria
- AC1: Gross = kg × ₱/kg; Net = Gross − transport; Net ₱/kg = Net ÷ kg. *(Tested: 250 kg × ₱44 − ₱300 = ₱10,700 → ₱42.80/kg ✅)*
- AC2: Summary profit per parcel = sales net − costs. *(Tested: P1 = ₱10,700 − ₱1,000 = ₱9,700; ₱4,850/ha on 2 ha ✅)*
- AC3: Costs without a valid Parcel ID show up as "Unassigned costs". ✅
- AC4: Parcel, crop, category and buyer fields offer dropdowns. ✅
- AC5: Opens and recalculates in Google Sheets. ⏳ Cowboy to confirm after upload.
- AC6 (usage): 90 days of logging with ≥80% of transactions captured. ⏳ Stage S0 gate.

## Non-goals
Mobile app, multiple farms, weather, inventory, harvest forecasting, pond monitoring. Each one waits for its own spec.

## Open questions
- Who is the on-site logger?
- Should rice and corn also be logged in kg, or in cavans? (brother to decide)
