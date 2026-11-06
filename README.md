# DaloyAqua 🌊

> *Daloy* — flow. DaloyAqua helps Baleno farm families see and steer the flows of their farm: **water, data, cash and knowledge.**

An agritech startup in the making, for Baleno, Masbate, Philippines. It is built one small step at a time by three siblings: IT, agriculture and accounting.

## Current phase: **Research** (SDLC Phase 0) · Stage: **S0**, before deployment
> Continuing this work (human or AI)? **Read [HANDOFF.md](HANDOFF.md) first.**

The family farm logbook is our first **research instrument**: it collects real Baleno price and cost data to test what desk research found.

| Spec | Name | Status |
|---|---|---|
| [001](specs/001-farm-logbook/spec.md) | Family farm logbook (spreadsheet) | built, awaiting deployment |
| [002](specs/002-mobile-entry/spec.md) | Mobile entry (offline-first, assisted) | draft (waits for S0 gate) |
| [003](specs/003-copra-sale-quality/spec.md) | Copra moisture & deduction fields | draft (awaiting review) |

## Strategy in one line
Association first, not app first: bookkeeping and pooled selling for Baleno farmer groups, built after it's proven on our own farm. See [lean canvas](docs/02-strategy/lean-canvas.md).

## Repo map
| Path | What |
|---|---|
| `docs/00-brand.md` | Name, meaning, principles |
| `docs/01-research/` | Cited research rounds 1–4 (problem discovery; value chain, users, Japan; who pays and funding; co-op bookkeeping landscape) |
| `docs/02-strategy/` | Lean canvas, team roles, funding roadmap |
| `docs/03-sdlc.md` | How we build: SDLC + spec-driven development, stage gates |
| `docs/05-fieldwork/` | Interview guides (G1–G6) and interview notes |
| `docs/04-innovation.md` | Innovation log: idea → experiment → spec or parked |
| `HANDOFF.md` | Progress, decisions, next actions, rules for AI agents |
| `specs/` | One folder per feature: `spec.md` → `plan.md` → `tasks.md` |
| `tools/` | Working tools (v0 logbook workbook) |

## How we work
1. Every feature starts from a verified problem (`docs/01-research`).
2. No build without a spec (`docs/03-sdlc.md`).
3. Ideas go to the innovation log first. Experiments come before specs.
4. Small, constant flow over big, rare effort.
