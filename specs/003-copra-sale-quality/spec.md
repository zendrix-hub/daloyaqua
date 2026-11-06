# Spec 003 — Copra Sale Quality Fields

**Status:** draft — awaiting review by brother (agronomy) and sister (accounting) · **Stage:** S0 (v0.1 of the logbook) · **Owner:** Cowboy

## Problem
Round 2 found that copra graded for moisture by eye sold for about 7.7% less than metered copra, and most sales took a 14–22% moisture deduction (`docs/01-research/round2.md`, A1). Our logbook records the price but not *why* it was low.

## User stories
1. As the logger, I record how moisture was judged (visual / meter / unknown) and the deduction % the buyer applied.
2. As the family, we compare net ₱/kg for visual vs metered sales and across buyers.

## Acceptance criteria
- AC1: The Sales sheet has new columns: `Moisture Method` (dropdown: Visual, Meter, Unknown), `Deduction %`, `Gross weight before deduction (kg)`.
- AC2: Existing formulas (spec 001 AC1–AC3) still give the same results. Regression test: ₱10,700 net, ₱42.80/kg, P1 profit ₱9,700.
- AC3: Summary shows average net ₱/kg by moisture method.
- AC4: The fields are optional, so a sale can still be logged in under 2 minutes.

## Non-goals
Buying a moisture meter. That is a decision for after 3 months of data: if the visual-grading gap shows up locally, consider a shared meter for the S2 association pilot.

## Open question
Does the buyer report weight before or after the deduction? The brother should ask on the next sale.
