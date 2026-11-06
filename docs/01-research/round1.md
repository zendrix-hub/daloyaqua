# Research Round 1 — Problem Discovery (2026-11-04)

Method: deep-research workflow covering 5 angles and 22 sources. Each claim got 3 adversarial votes and needed 2 of 3 to survive. 25 claims verified: 13 confirmed, 12 rejected.

## Confirmed findings (ranked)
1. **Copra price volatility. Confidence: high.** PCA national average farmgate price was ₱58.10/kg on 31 Mar 2025, up from ₱27.69 a year earlier. In mid-2023 it was ₱21–24, with about 500k farmers affected. In Eastern Visayas it fell from ₱36.44 (2017) to ₱12.17 (Feb 2019). Around ₱44.5 in Jul 2026. Price falls with distance from an oil mill.
   - https://context.ph/2025/04/08/surge-in-copra-prices-bedevil-coconut-industry/
   - https://philstar.com/headlines/2023/06/27/2276809/pca-confirms-copra-price-slump-500000-farmers-affected
   - https://ptvnews.ph/copra-price-drop-hurts-region-8-coco-dependent-families/
2. **High input costs are the top constraint farmers report. Confidence: medium.** The source is a survey in Cawayan, Masbate (Velza et al. 2023). Soil fertility and water supply are the main natural-resource problems. DA-SAAD confirms these for Masbate.
   - https://doaj.org/article/4a2c3db1039140958b696a2c1619b33d
   - https://saad.da.gov.ph/phase-2/masbate/
3. **Risk comes from low coping capacity, not from hazards. Confidence: high.** Masbate ranks 6th of 84 for vulnerability and 68th of 84 for coping capacity, but 4th of 84 for typhoon-wind risk. Baleno poverty: 33.05% (2018), 19.54% (2023).
   - https://dev.pdc.org/wp-content/uploads/2024/07/Masbate.pdf
   - https://en.wikipedia.org/wiki/Baleno,_Masbate (PSA small-area estimates)
4. **PCIC crop insurance raised net income and access to credit for small farms. Confidence: medium.** Based on one 2016 study in Western Visayas.
   - https://pids.gov.ph/publication/discussion-papers/evaluation-of-the-impact-of-the-agricultural-insurance-program-of-pcic-on-rice-producers-in-region-vi
5. **Adoption warning. Confidence: medium.** PhilRice AgriDoc had 1,061 users. 74% were college graduates, and users found it tedious and English-only.
   - https://pidswebs.pids.gov.ph/CDN/document/pidsdps2329.pdf
6. **Future users. Confidence: high.** Three DA-SAAD associations in Baleno, 25 members each: poultry in Madangcalan, corn/cassava in Obongon Diot, vegetables in Polot. There is also a BFAR fisherfolk group in Polot.
   - https://saad.da.gov.ph/phase-2/masbate/

## Rejected or unverified (open, not disproven)
Fishpond economics (the SEAFDEC model figures), rural connectivity statistics, PCIC paperwork burden, trader-vs-mill price gap, Masbate priority commodities. Round 2 follows up on these.

## Decision
First atomic problem: *"We don't know what we earn per parcel and per copra sale."* We built it as → `specs/001-farm-logbook`.
