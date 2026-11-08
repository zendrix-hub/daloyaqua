# Spec 003 — Copra Sale Quality Fields

**Status:** built into `tools/baleno-farm-logbook-v0.xlsx` (v0.1, 2026-11-08) — awaiting review by brother (agronomy) and sister (accounting) · **Stage:** S0 (v0.1 of the logbook) · **Owner:** Cowboy

## Problem
Round 2 found that copra graded for moisture by eye sold for about 7.7% less than metered copra, and most sales took a 14–22% moisture deduction (`docs/01-research/round2.md`, A1). Round 5 verified the official PCA AO 02 s. 2003 threshold (6% *resecada* base, ≥14% rejection) and the village *pesada* deduction flow (*bawas sako* + *resiko* %). Our logbook needs to record how moisture was graded and what deduction the buyer took when the *taohan* turns over the receipt (*pesada*) to Mother.

## User stories
1. As Mother / the logger, when the *taohan* turns over the buyer's receipt (*pesada*), I record how moisture was judged (`Visual` / `Meter` / `Unknown`), the `Deduction %`, and `Gross Weight Before Deduction (kg)`.
2. As the family, we compare average net ₱/kg for `Visual` vs `Meter` sales on the `Summary` sheet and across buyers.

## Acceptance criteria
- AC1: The Sales sheet has columns `M:O`: `Moisture Method` (dropdown from `Lists!$D$2:$D$4`: `Visual`, `Meter`, `Unknown`), `Deduction %`, `Gross Weight Before Deduction (kg)`. ✅ *(Built in v0.1)*
- AC2: Existing formulas (spec 001 AC1–AC3) still give the same results. Regression test: ₱10,700 net, ₱42.80/kg, P1 profit ₱9,700, ₱4,850/ha. ✅ *(Tested in v0.1)*
- AC3: Summary (`H11:I12`) shows weighted average net ₱/kg by moisture method (`Visual` vs `Meter`). ✅ *(Built in v0.1 using Excel-2007 `SUMIFS`)*
- AC4: The fields are optional, so a sale can still be logged in under 2 minutes. ✅

## Non-goals
Buying a moisture meter. That is a decision for after 3 months of data: if the visual-grading gap shows up locally, consider a shared meter for the S2 association pilot.

## Open question
- Does our Baleno buyer write the pre-deduction weight and *resiko* % on the *pesada* (receipt) handed to the *taohan*, or only tell the *taohan* verbally? Brother and Mother to check on the next sale (`G2`).
