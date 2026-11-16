# Spec 002 — Mobile Entry

**Status:** draft — do not build until the S0 gate passes · **Stage:** S1 · **Owner:** Cowboy

## Problem (hypothesis)
Logging in a spreadsheet on a phone is slow. If the logger skips entries, the data is useless. A phone-first entry form with local-language labels should raise the logging rate.
*To be confirmed by S0 data: are entries missing because the sheet is hard to use on a phone?*

## Users
The on-site logger first. Later, neighbor farmers (S2).

## User stories (draft)
1. As the logger, I log a sale in ≤5 taps plus the numbers, in Tagalog or Masbateño.
2. As the logger, I can log without signal and it syncs later. *(Required: see round 2, B5.)*
3. As the family, everything still ends up in the same data model as spec 001.

## Acceptance criteria (draft)
- AC1: Median time to log a sale is ≤60 seconds (timed with the real logger).
- AC2: Zero lost entries after 1 month, including entries made offline.
- AC3: The logging rate is at least as high as in S0.

## Direction after research round 2
Bicol data (Ligao, Albay, 2026): 34% of farmers have reliable internet, 80% have unstable connections, and 81–82% struggle to use digital tools (`docs/01-research/round2.md`, B5). So:
- **Offline-first is required.** Entry has to work with no signal and sync later.
- **Assisted entry is the default user model.** A logger or bookkeeper (brother or association bookkeeper) enters data for farmers. Don't plan on each farmer using it themselves.
- **Local language.** Labels in Masbateño/Minasbate + Tagalog; audio/icons where possible.

**Leading candidate:** AppSheet on top of the existing Google Sheet. It works offline, needs no backend, and keeps the spec-001 data model. Fallback: an offline-first PWA if AppSheet limits or cost block S2.
To confirm in plan.md: AppSheet free-tier limits and the offline sync behavior on low-end Android phones.

## Non-goals
Multiple farms, a price board, accounts and logins for outside users.
