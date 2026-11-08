# Research Round 5 — Ground-Level Realities for "Now": Copra Weighing, Farm Labor, Baleno Groups & CDA Accounts (2026-11-08)

Method: targeted deep-research pass focused strictly on **what we need to know right now (Phase 0 / Stage S0)** before deploying the family logbook or designing any software. Covers 5 angles: (A) copra weighing, moisture deductions, and buyer *pesada* mechanics; (B) coconut farm labor payment structures; (C) named target associations and copra trade routes in Baleno/Masbate; (D) CDA `MC 2022-24` Standard Chart of Accounts & federation software landscape; and (E) PH agritech failure modes (`AgriDoc`, `Cropital`). Every claim was checked against primary sources and the `HANDOFF.md` 🚫 refuted list.

---

## A. How Copra Is Actually Weighed and Discounted (*Resecada*, *Corriente*, *Pasa*, *Resiko*)

1. **Official PCA moisture rules: 6% base (*Resecada*), 6.1–13.9% sliding deduction, ≥14% rejected. *(high)***
   Under **PCA Administrative Order No. 01 (s. 1991)** and **PCA Administrative Order No. 02 (s. 2003)** (*Implementing Rules and Regulations of the Revised Price Adjustment Scale for Moisture Content in Copra*, issued to meet EU Directive 2002/32/EC on Aflatoxin B1), **6.0% moisture content** (*resecada* / *bodega*) is the equilibrium base price with **0% deduction**. Copra graded between **6.1% and 13.9% moisture** takes an incremental weight deduction from the official PCA moisture table. Copra at **≥14.0% moisture** is legally classified as non-merchantable and subject to rejection.
   - https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/41935
   - https://jur.ph/apis/ai/summary/philcoa-administrative-order-no-02-s-2003

2. **How the village buyer's weighing slip (*pesada*) works in practice: *Bawas Sako* + *Resiko* / *Pasa*. *(medium)***
   Smallholders rarely dry copra down to 6% laboratory *resecada*; copra coming off a smoke kiln (*tapahan*) or sun-drying is traded as *corriente* (typically 14–22% moisture, per Rivera & Lantican 2010 in `round2.md`). At a local buying station (*komprahan*), the payout calculation follows a 4-step deduction flow on the *pesada* (weighing slip):
   $$\text{Gross Scale Weight (kg)} - \text{Sack Weight (\textit{Bawas Sako / Tara})} = \text{Clean Weight (kg)}$$
   $$\text{Clean Weight (kg)} - \text{Moisture/Quality Deduction (\textit{Resiko / Pasa} \%)} = \text{Net Billable Weight (kg)}$$
   $$\text{Net Billable Weight (kg)} \times \text{Quoted Base Price (₱/kg)} = \text{Gross Payout (₱)}$$
   - https://journal.coconutcommunity.org/index.php/journalicc/article/download/133/120
   - https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/41935

3. **Immediate implication for `Spec 001` and `Spec 003` (before logging row 1):**
   - In `tools/baleno-farm-logbook-v0.xlsx`, `Sales!D` (`Qty (kg)`) multiplies directly by `Sales!E` (`Price (₱/kg)`) to compute `Gross (₱)`.
   - Therefore, **the logger must enter `Net Billable Weight (kg)` (after *bawas sako* and *resiko* weight cuts) into `Qty (kg)`**, and the actual price applied on the receipt into `Price (₱/kg)`. If the logger enters raw scale weight before weight deductions, `Gross (₱)` in the logbook will not match cash in hand.
   - In `Spec 003` (`specs/003-copra-sale-quality/spec.md`), `Gross weight before deduction (kg)` captures the raw scale weight (after sack tare) so the spreadsheet can compute the exact empirical *resiko* deduction % on every Baleno sale.

---

## B. Coconut Farm Labor & Cost Structure (*Pakyawan* vs. *Tersya*)

4. **Physical conversion benchmark: ~4.5 to 5 mature nuts = 1 kg of dry copra. *(medium)***
   Across Philippine smallholder coconut budgets, producing 1 kg of dry copra requires roughly 4.5–5 mature whole nuts, and a skilled dehusker using a traditional plowshare spike (*kabayo* / *tapasan*) processes ~1,000 nuts per day.
   - https://www.unido.org/ (UNIDO traditional vs. mechanized coconut dehusking productivity benchmarks)

5. **Two labor payment systems exist — and *Tersya* (share-splitting) can silently break farm bookkeeping if not handled. *(medium)***
   Philippine coconut farms pay for harvesting and copra processing in two ways:
   - **Piece-rate / per-stage cash wages (*pakyawan* or *arawan*):** paid per tree or per 1,000 nuts across 5 distinct stages: (1) harvesting/climbing (`pagkawit`), (2) piling/hauling (`pagpulot`/`paghakot`), (3) dehusking (`pagbunot`), (4) splitting & meat scooping (`pagbiyak`/`paglukad`), and (5) kiln firing/drying (`pagtapahan`).
   - **Crop-share / labor-sharing (*tersya* or *hatian*):** to avoid paying cash upfront before copra is sold, many farm owners let the harvesting/copra crew take a direct percentage split of the sale proceeds — traditionally **1/3 (*tersya*) to the labor crew and 2/3 to the landowner** (or 50/50 for full tenants), often deducted right at the buyer's counter alongside any cash advances (*bali*).
   - **Verified Baleno Family Farm Workflow (from Cowboy, 2026-11-08):** On our family farm in Baleno, the ***taohan*** (farm worker/caretaker) cooks the copra (*tapahan*), transports it, and bargains with the buyer. After the sale, the *taohan* turns over the receipt (*pesada*) and cash to **Mother**, who calculates and reviews the sale and allocates the proceeds between **our family's share ("ours")** and **the *taohan*'s share ("the ones who did the work")**.
   - **Design update implemented (`v0.1` of `tools/baleno-farm-logbook-v0.xlsx`):** Instead of forcing Mother or Brother to log a sale in `Sales` and then switch to `Costs` to log the *taohan* share, `Sales` now serves directly as **Mother's Turnover Calculator**: `Transport Cost (₱)` (`H`) → `Net (₱)` (`I`) → `Taohan Share (₱)` (`K`, yellow input) → `Our Family Share (₱)` (`L = I - K`, auto-calculated), and `Summary` automatically sums `Sales!K` + standalone `Costs!H` per parcel.

---

## C. Named Target Groups & Copra Trade Routes in Baleno & Masbate

6. **The 3 DA-SAAD Phase 2 associations in Baleno are now identified by name. *(high)***
   Official DA-SAAD Bicol records confirm the exact names, barangays, and commodities of the three 25-member associations in Baleno, Masbate (`round1.md` finding 6):
   - **Maluy-a Proper Farmers Association** — Brgy. Obongan Diot, Baleno (25 members; **corn and cassava**). Founded ~2019; highlighted by DA-SAAD in 2025 for conducting member profit-sharing, market expansion, and Marketing Assistance and Enterprise Development (MAED) record-keeping training.
   - **Madancalan Farmers Association** — Brgy. Madangcalan, Baleno (25 members; **poultry production**).
   - **Maan Farmers and Fisherfolks Association** — Brgy. Polot, Baleno (25 members; **vegetable production**).
   - https://saad.da.gov.ph/masbate-fas-reflect-on-2025-success-holds-profit-sharing-and-market-expansion/
   - https://saad.da.gov.ph/masbate/
   - https://saad.da.gov.ph/phase-2/masbate/

7. **How DA-SAAD associations register and transition to CDA co-ops (answers part of `F9`). *(medium)***
   Under DA-SAAD Phase 2, beneficiary groups start as **Farmers' Associations (FAs)** — typically registered first with **DOLE** (as rural workers' associations) or **SEC** (as non-stock associations) to gain legal personality and Civil Society Organization (CSO) accreditation — and are then coached by SAAD's MAED unit on financial record-keeping to **transition into full CDA-registered cooperatives**.
   - **Implication for `G3` (sister's interview):** If the sister interviews **Maluy-a Proper FA** (Obongan Diot), she should expect them to be a DOLE/SEC-registered association currently learning enterprise bookkeeping under DA-SAAD MAED (preparing for cooperative transition), whereas an already-registered coconut co-op under PCA-CDA **CocoFarmCoop** faces immediate CDA `MC 2025-02` COC filing. Both need bookkeeping, but the compliance trigger differs (`F9`).

8. **Masbate copra trade routes and CFIDP activity on the island. *(medium–high)***
   - **CFIDP in Masbate:** ATI Bicol (DA-ATI RTC V) hosted the first leg of the **CFIDP Techno Forum 2025** in Masbate City on April 14, 2025 (focusing on value-added coconut products, VCO, coco sugar/vinegar, and market linkage), and President Marcos signed **Memorandum Circular No. 84** approving the **Revised CFIDP 2024–2028**.
     - https://ati2.da.gov.ph/ati-5/
   - **Where Masbate copra goes:** Local traders/consolidators in Baleno and Masbate ports ship raw copra across the gulf primarily to **Legaspi Oil Company Inc. (CIIF Oil Mills Group)** in Legazpi City, Albay (the primary Bicol industrial oil mill), as well as inter-island buyers in **Lucena City, Quezon** and **Cebu/Mandaue**. Because Baleno copra must be trucked to a Masbate port and barged across the sea to Legazpi, Lucena, or Cebu, transport and double-handling widen the gap between the PCA millgate price and the Baleno farmgate price (`round1.md` finding 1).

---

## D. CDA `MC 2022-24` Chart of Accounts & Federation Software Landscape

9. **CDA `MC 2022-24` coding structure for the sister's chart of accounts. *(high)***
   **CDA Memorandum Circular No. 2022-24** (*Revised Standard Chart of Accounts for Cooperatives*, Sept 5, 2022) prescribes a mandatory 5-digit account code structure across all Philippine cooperatives:
   - `10000` **Assets** (Current & Non-Current, including e-wallet/cash accounts and biological/agricultural assets)
   - `20000` **Liabilities**
   - `30000` **Equity** (Share Capital + mandatory Cooperative Statutory Funds: Reserve Fund, Cooperative Education & Training Fund [CETF], Community Development Fund, Optional Fund)
   - `40000` **Revenues / Income** (segregated by business line: e.g., Marketing Operations, Production Operations, Service Operations)
   - `50000` **Cost of Goods Sold / Cost of Services** (`51000` Cost of Goods Sold; `51110` Purchases, plus freight-in and processing costs deducted from gross sales to compute Gross Margin per activity)
   - `60000` **Operating / Administrative Expenses**
   - https://cda.gov.ph/issuances/mc-2022-24-revised-standard-chart-of-accounts-for-cooperatives-amendment/
   - https://cda.gov.ph/wp-content/uploads/2022/10/MC-2022-24.pdf

   **Crosswalk from `Spec 001` (`Lists!B2:B12`) to CDA `MC 2022-24` (ready for the sister):**
   | `Spec 001` Logbook Cost Category | Farm Level Role | Co-op Level Mapping (`MC 2022-24`) |
   |---|---|---|
   | Seeds / planting materials | Direct crop input (Parcel COGS) | `50000` Cost of Production / Farm Inputs |
   | Fertilizer | Direct crop input (Parcel COGS) | `50000` Cost of Production / Farm Inputs |
   | Pesticide / herbicide | Direct crop input (Parcel COGS) | `50000` Cost of Production / Farm Inputs |
   | Hired labor (*pakyawan* / *tersya*) | Direct harvest/crop labor | `50000` Direct Labor / Processing Cost |
   | Land preparation / machinery | Direct crop input / equipment hire | `50000` Cost of Production — Equipment Rental |
   | Copra drying / processing | Post-harvest direct cost (*tapahan*) | `50000` Cost of Goods Sold — Post-Harvest Processing |
   | Transport / hauling | Selling / delivery expense | `50000` Freight-In (buying) or `60000` Freight-Out / Selling Expense |
   | Feed | Direct livestock/aquaculture input | `50000` Cost of Production — Feeds |
   | Irrigation / water | Direct farm utility | `50000` Cost of Production — Utilities/Water |
   | Repairs & tools | Farm maintenance overhead | `60000` Repairs and Maintenance |
   | Other | Unclassified | `60000` Miscellaneous Operating Expenses |

10. **Other federation software in the Philippines (`Pinoy Coop Core`, `CoopBase`) also target credit co-ops, confirming the agricultural co-op gap. *(medium)***
    Expanding `round4.md` finding 8 (which verified NATCCO's `eKoopBanker`), two other major cooperative federations offer CDA-compliant accounting software:
    - **MASS-SPECC (`Pinoy Coop Core 3.0`):** Web-based core banking, general ledger, CISA credit reporting, and SMS blast, built by Mindanao's largest co-op federation — https://pinoycoop.com
    - **PFCCO (`CoopBase`):** Cooperative banking, loan/time-deposit monitoring, and CDA-compliant general ledger used by credit cooperatives in Visayas/Luzon — https://www.pfccovisayas.coop
    - **Takeaway:** All three verified federation systems (`eKoopBanker`, `Pinoy Coop Core`, `CoopBase`) are **core-banking systems built for savings and credit cooperatives**. None of them is designed for **smallholder crop/copra buying, moisture deduction tracking, or assisted offline field logging** in a 25-member rural farmers' association.

---

## E. Why PH Agritech & Record Tools Fail — Guardrails for "Now"

11. **Why farmers drop record-keeping apps (`AgriDoc`) and why retail crowdfarming collapsed (`Cropital`). *(medium)***
    - **PhilRice `AgriDoc` (`PIDS DP 2023-29`):** Even with offline capability, Google Maps lot plotting, and expense categories, `AgriDoc` stalled at ~1,061 users (74% college-educated) because daily data entry was tedious and **disconnected from an immediate economic transaction or requirement**.
      - https://pidswebs.pids.gov.ph/CDN/document/pidsdps2329.pdf
    - **`Cropital`:** Connected retail crowdfunding lenders with smallholder farmers, but went silent in late 2022 amid typhoon/pest shocks and unresolved investor payouts.
      - https://cropital.com
    - **Design guardrails for DaloyAqua right now:**
      1. **Log only at cash events (sales and actual expenses), never daily agronomic diaries.** That keeps the 2-minute rule realistic.
      2. **Never touch retail crowdfunding or unhedged farmer lending.** Stay strictly in bookkeeping, price transparency, and co-op compliance/pooled selling.
      3. **Verify on our own family farm first (S0)** before asking any neighbor or Baleno association to adopt a workflow.

---

## Rejected or Flagged During Round 5 Verification
- **🚫 Re-confirmed rejected (from Round 4):** Secondary blogs/Scribd summaries still claim `MC 2025-02` lets micro co-ops file via Google Forms. Primary `MC-2025-02-with-annexes.pdf` requires **CAIS online + hard copies**. Keep on the 🚫 list.
- **⚠️ Still open for field verification (`F8`):** Whether `MC 2019-04`'s Audit Committee sign-off for micro co-ops (≤₱3M assets) is still accepted by CDA Region V under `MC 2025-02`. Must be asked directly in `G5` Question 3a.
