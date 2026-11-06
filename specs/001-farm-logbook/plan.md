# Plan 001 — Farm Logbook (Design)

## Approach
A single spreadsheet workbook: `tools/baleno-farm-logbook-v0.xlsx`. Shared through Google Sheets so it costs nothing, works on any phone or laptop, and lets the family edit together.

## Data model
| Sheet | Grain (one row =) | Key fields |
|---|---|---|
| Parcels | one parcel | Parcel ID (PK), name/location, area (ha), current use, main crop |
| Lists | lookup values | crops, cost categories (chart of accounts), buyers |
| Sales | one sale | date, Parcel ID (FK), crop, kg, ₱/kg, *gross*, buyer, transport, *net*, *net ₱/kg* |
| Costs | one expense | date, Parcel ID (FK), crop, category, item, qty, unit, amount, paid to |
| Summary | computed | profit per parcel (SUMIFS), copra price tracker (COUNTIFS/SUMIFS/MINIFS/MAXIFS) |

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
