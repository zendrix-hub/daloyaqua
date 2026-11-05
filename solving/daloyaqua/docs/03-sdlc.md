# DaloyAqua Development Lifecycle — SDLC + Spec-Driven Development

## Principle
**No build without a spec.** Every feature lives in `specs/NNN-name/` and moves through the same SDLC phases. Specs are small, like atomic habits: one problem per spec.

## SDLC phases → artifacts
| # | Phase | Question | Artifact | Owner |
|---|---|---|---|---|
| 0 | **Research / Discover** ← *current* | What is the real problem? What's verified? What's still a guess? | `docs/01-research/roundN.md` (cited, vote-verified) + field-validation notes | Cowboy (desk), brother (field) |
| 1 | Plan | Which verified problem? Is it worth solving now? | Problem statement + evidence link in `spec.md` | Cowboy |
| 2 | Requirements | Who uses it, what must it do, how do we know it works? | `spec.md`: user stories, acceptance criteria, non-goals | Cowboy + domain owner |
| 3 | Design | How will it work? Data model, tools, trade-offs | `plan.md` (doubles as the Software Design Document) | Cowboy |
| 4 | Build | What are the smallest steps? | `tasks.md` (checklist, each ≤ 1 hour) | Cowboy |
| 5 | Test | Does it meet each acceptance criterion with real data? | Results recorded in `tasks.md` | Cowboy + user |
| 6 | Deploy | Who gets it and how? | Release note in `spec.md` → Status | Cowboy |
| 7 | Maintain / Review | Is it used? What did we learn? | Monthly review notes; a new spec if needed | All three |

### Phase 0 exit criteria (Research → Plan)
- [ ] Desk research rounds are cited, and rejected claims are listed *(done: rounds 1–3)*
- [ ] Top hypotheses checked in the field, in Baleno (see the field-validation checklist in `HANDOFF.md`)
- [ ] ≥30 days of real logbook data (spec 001 deployed)
- [ ] Riskiest assumption #2 (associations accept assisted bookkeeping) tested in ≥1 interview

### Spec status flow
`draft → approved → in-progress → built → shipped (deployed and in real use) → (retired)`
A spec moves to `approved` only after the domain owner (brother/sister) reviews it.

## Product stages and gates
| Stage | Scope | Gate to the next stage (all must hold) |
|---|---|---|
| **S0 Logbook** (now, before deployment) | Spreadsheet, family farm only — `specs/001-farm-logbook`, `specs/003-copra-sale-quality` | 90 days of use, ≥80% of transactions logged, profit per parcel known |
| **S1 Mobile entry** | Phone-friendly logging, local-language labels — `specs/002-mobile-entry` | Family logs from phones for ≥1 month; ≥3 neighbor farmers ask for it |
| **S2 Baleno pilot** | Association ledger with assisted entry + shared Baleno copra price and moisture board, with a DA-SAAD association or CFIDP coconut co-op | ≥25 active farmers for 3 months; farmers trust the price data |
| **S3 DaloyAqua platform** | Co-op financial statements (CDA COC-ready / lender-grade), pooled selling, two-way buyer matching (JA model), pond module | A paying customer or a secured grant; a business registered |

Gates exist to stop us building ahead of real use. AgriDoc had low adoption (see `docs/01-research/round1.md`), which shows what happens when tools are built ahead of users.

Ideas don't enter a spec directly. They start in `docs/04-innovation.md` as an idea, then an experiment, and only then become a spec.

## Spec template (copy for each new spec)
```
specs/NNN-short-name/
  spec.md   — Status, Problem (+evidence), Users, User stories, Acceptance criteria, Non-goals, Open questions
  plan.md   — Approach, Data model, Tools/stack, Alternatives considered, Risks
  tasks.md  — [ ] small steps, test results, release note
```

## Definition of Done (every spec)
- [ ] All acceptance criteria were checked against real farm data, not only example rows
- [ ] The domain owner signed off
- [ ] The README stage/status table is updated
