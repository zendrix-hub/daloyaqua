# Plan 001 — Farm Logbook (Design)

## Approach
A single spreadsheet workbook: `tools/baleno-farm-logbook-v0.xlsx`. Shared through Google Sheets so it costs nothing, works on any phone or laptop, and lets the family edit together.

## Data model
| Sheet | Grain (one row =) | Key fields |
|---|---|---|
| Parcels | one parcel | Parcel ID (PK), name/location, area (ha), current use, main crop |
| Lists | lookup values | crops, cost categories (chart of accounts aligned with CDA `MC 2022-24`), buyers, moisture methods (`Visual`, `Meter`, `Unknown`) |
| Sales | one sale turnover (*taohan* → Mother) | date, Parcel ID (FK), crop, net kg paid, ₱/kg, *gross*, buyer, transport, *net*, *net ₱/kg*, taohan share (₱), *our family share (₱)*, moisture method, deduction %, gross weight before deduction (kg), notes |
| Costs | one standalone expense (outside sale turnover) | date, Parcel ID (FK), crop, category, item, qty, unit, amount, paid to, notes |
| Summary | computed | profit per parcel (`Sales Net − [Taohan Share + Costs]`, SUMIFS), copra price & turnover tracker (COUNTIFS/SUMIFS/MINIFS/MAXIFS, Visual vs Meter avg net ₱/kg) |

*Italic* = formula columns. Yellow cells with blue text are for input. Black text is formulas.

This schema is meant to become the database tables in S1/S2 (`parcels`, `sales`, `costs`, `lookups`), with `farm_id` added for multi-farm use.

## Alternatives considered
- **Mobile app first:** rejected. AgriDoc's low adoption shows the risk of building before usage is proven.
- **Paper notebook:** fine as a fallback for the logger, but someone has to type it in weekly. There are no analytics without that step.

## Risks
| Risk | Mitigation |
|---|---|
| Logger forgets to log | 2-minute rule; Cowboy's weekly check notices gaps |
| Accidental formula edits | Formula cells kept visually distinct; consider sheet protection in Google Sheets |
| Prices recorded inconsistently (posted price vs. paid price) | Column note: "price actually paid to you" |
