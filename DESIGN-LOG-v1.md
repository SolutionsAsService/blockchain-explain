# DESIGN-LOG — blockchain-explain, DADA run

Project: `SolutionsAsService/blockchain-explain` — a static site teaching blockchain
concepts, whose actual subject is Autheo.
Branch: **`thoth-division`** (this run and its lessons live here, not on `main`).

Brief restated in one sentence: rebuild the site as one bold, professional page that
puts Autheo at the centre, with a new custom graphic, instead of a shell that
promises eleven sections and delivers four.

Run started 2026-10-27. Mode: **Adaptive** — this is a public teaching resource with
a named audience (developers, businesses, curious learners), so the governing
criterion is MAYA: the advanced pole and the acceptable pole must both hold.

## Step 0. Tooling inventory

| Job | Tool used |
|---|---|
| Render and navigate the anchor graph | **none available** — no Mermaid renderer, graph database or diagram tool in this session → Mermaid text in this log, node ids from `references/anchor-graph.md` |
| Compute the Frontier | **none available** — no graph query → edge lines read by hand from the graph reference |
| Track workflow state | **none loaded** — `TaskCreate`/`TaskUpdate` exist as deferred tools and were not loaded for this run → checklist and tables in this log (allowed fallback) |
| Run the panel | **`Agent` tool, one agent per literary reference, launched at most three at a time**, each writing its verdict to `panel/R0/<seat>.md` as its last action |
| Collect panel reports | panel directory on disk, collected by listing it |
| Persist the log | this `DESIGN-LOG.md`, with `CARRY-FORWARD.md` beside it |
| Measure the artifact | `node` v24.22.0 scripts written for this run; WCAG ratios from the relative-luminance formula |

## Step 1. Traversal Plan

### Seed (labels copied verbatim from the graph)

- Stance: `fft` — **First Things First Manifesto (Ken Garland)**. The inherited site
  is surface with ten dead links behind it; FTF is the anchor that demands the page
  earn its purpose before it earns its finish.
- Rules (solid edges followed): `mb` — Grid Systems in Graphic Design (Josef
  Müller-Brockmann) `-->|codifies|-->` `itstyle`; `wcag` — WCAG 2.2 Contrast and
  Perceivability (W3C) `-->|measurable access for|-->` `c_qas`; `bring` — The
  Elements of Typographic Style (Robert Bringhurst) `-->|canon for|-->` `lupType`.
- Breaker: `samBreak` — Making and Breaking the Grid (Timothy Samara).
- Counterpoint (dotted edge from a chosen node): `wcag`
  `-.->|contrast floor constrains|->` `albers` — Interaction of Color (Josef
  Albers). The palette is chosen, then measured against the floor.
- Governing criterion of this mode: `maya` — MAYA `-->|bounds the break of|-->
  samBreak`.

Chain as written:

```
fft -->|debate context for| lookC
mb -->|codifies| itstyle
wcag -->|measurable access for| c_qas
wcag -.->|contrast floor constrains| albers
samBreak -.->|loosens| mb
maya -->|bounds the break of| samBreak
bring -->|canon for| lupType
```

### Live graph (seed region, visited marks)

```mermaid
flowchart LR
  fft["First Things First Manifesto (Ken Garland)"]:::stance
  mb["Grid Systems in Graphic Design (Josef Muller-Brockmann)"]:::rules
  itstyle["International Typographic Style (Swiss Style)"]:::rules
  wcag["WCAG 2.2 Contrast and Perceivability (W3C)"]:::rules
  c_qas["Quality Attribute Scenario"]:::catalog
  albers["Interaction of Color (Josef Albers)"]:::rules
  samBreak["Making and Breaking the Grid (Timothy Samara)"]:::break
  maya["MAYA: Most Advanced Yet Acceptable (Raymond Loewy)"]:::welcome
  bring["The Elements of Typographic Style (Robert Bringhurst)"]:::rules
  lupType["Thinking with Type (Ellen Lupton)"]:::rules
  fft -->|debate context for| lookC
  mb -->|codifies| itstyle
  wcag -->|measurable access for| c_qas
  wcag -.->|contrast floor constrains| albers
  samBreak -.->|loosens| mb
  maya -->|bounds the break of| samBreak
  bring -->|canon for| lupType
  class fft,mb,itstyle,wcag,c_qas,albers,samBreak,maya,bring,lupType visited
```

### Panel composition (Adaptive)

Required: Critic: Provocateur (Debord, Shklovsky) and Critic: Inclusion (Holmes,
Mace) — each thinker its own seat — plus three more chosen for maximum difference:
Critic: Usability (Krug), Critic: Evidence (Tufte), Critic: Craft (Bringhurst).
Seven seats, seven authorities. The Krug seat supplies the required dotted pair:
`crit_prov_debord -.->|attacks smoothness favored by| crit_use_krug`.

### Measured facts of the inherited artifact (before any move)

| Measurement | Procedure | Value |
|---|---|---|
| Unique internal links | parse `href` in index.html, dedupe | 14 |
| Links that resolve | `fs.existsSync` on each | **4** |
| Dead links | the remainder | **10** |
| Stylesheets referenced | parse `link[href^=css/]` | 3 |
| Stylesheets that exist | `fs.existsSync` | **1** (`style.css`) |
| Scripts referenced / exist | parse `script[src]` | 1 / **0** |
| External hosts | parse absolute URLs | fonts.googleapis.com |
| Word count, index.html | strip tags, split whitespace | 229 |
| Word count, autheo.html | same | 796 |

### Frontier (initial, after the seed)

| Candidate | Reached via (edge label, direction) | From anchor | Status |
|---|---|---|---|
| F1. Delete every link that does not resolve | `asks about purpose with`, incoming | `fft` | OPEN |
| F2. Stop referencing missing CSS and JS | `asks about purpose with`, incoming | `fft` | OPEN |
| F3. Build the page on a declared grid, one stated type ratio | `codifies`, outgoing | `mb` → `itstyle` | OPEN |
| F4. Cap prose measure at a character count | `canon for`, outgoing | `bring` → `lupType` | OPEN |
| F5. Measure every text pair against WCAG, both themes | `measurable access for`, outgoing | `wcag` → `c_qas` | OPEN |
| F6. Break the grid once, on purpose, for the hero graphic | `loosens`, dotted incoming | `samBreak` | OPEN |
| F7. Constrain the palette by measurement, not taste | `contrast floor constrains`, dotted outgoing | `wcag` → `albers` | OPEN |
| F8. Make Autheo the subject, not one card of eleven | `bounds the break of`, outgoing | `maya` → `samBreak` | OPEN |
| F9. Replace the automatized crypto-grid sign with a real figure | `debate context for`, outgoing | `fft` → `lookC` | OPEN |
| F10. Drop the webfont so the page makes no third-party request | `asks about purpose with`, incoming | `fft` | OPEN |

### Step 1.5 Premortem, round R0

Convened on the artifact **as inherited and unrendered** (no browser or screenshot
tool in this session, so critics judged the source and the measured table above).
Convened on the artifact **as inherited and unrendered** (no browser or screenshot
tool in this session, so critics judged the source and the measured table above).
Reports in `panel/R0/`.

### Panel, WHOLE, round R0 (artifact examined: `index.html`, `autheo.html`, `layer0.html`, `blockchain-basics.html`, `css/style.css`; **unrendered**)

| Critic | Anchor used | Observed in the work | Verdict | Requested change |
|---|---|---|---|---|
| Provocateur (Debord) | Thesis 6, *Society of the Spectacle* | 4 of 14 links resolve; 12 of 61 classes undefined incl. every diagram class, so the centrepiece stack renders as bare text with `↓` glyphs; `autheo.html` 119 tags open / 116 closed and no `</html>`; `GitHub` and `Documentation` are `href="#"` | OBJECT | No page may name a resource it does not have; every document must close |
| Provocateur (Shklovsky) | *ostranenie* vs automatization, *Art as Technique* | 44 hand-written instances of one green at 11 alphas; 9 near-blacks spanning luminance 0.0196–0.0781 used as distinct tokens; 243 rule blocks but 86 of 104 classes never instantiated; **0 `<img>` and 0 `<svg>`** in index.html | OBJECT | Delete `.grid-background`, the two blurred glows, and `@keyframes gridMove` |
| Inclusion (Holmes) | Mismatch is a property of the person–design relationship | Palette **passes**: 21 of 21 pairs clear AA, lowest live 7.15:1 — so this is not a contrast objection. One `:focus` rule in 2,527 lines and it is `outline:none`; 28 anchors, none focusable-visible; `prefers-reduced-motion` count 0; `scroll-padding-top` count 0 | OBJECT | Make the navigation truthful; every affordance resolves or is not a door |
| Inclusion (Mace) | Principle 1, Equitable Use | 0 of 28 interactive elements have a focus style; the sole `:focus` rule (`style.css:1272`) deletes the native ring on a search field that appears on no page; print sheet drops `p` to 1.71:1 on white | OBJECT | Add one `:focus-visible` rule and delete `outline:none` at :1272 |

Statements of meaning: a live, measurable, documented network exists (Debord); a
site that has been here before and will not be remembered (Shklovsky); a
twelve-topic curriculum for "curious learners" (Holmes); a teaching instrument
(Holmes, Mace). All four describe a lobby.

Artist questions: is the twelve-item nav a map of a book you intend to write, or a
description of one that exists? Was the `↓` a diagram or a placeholder for one? Is
the green a brand constraint or a free choice? Does the page want the reader to slow
down anywhere?

Critic questions: which of nine near-blacks does work another does not? Does the
missing `js/app.js` strand content invisible? *(Measured: no — `fade-up` is armed
but no page uses it.)* Are the ten missing pages planned or abandoned?

Andon pulled: **yes, by three of four** — Shklovsky (release: atmosphere deleted,
`grep -c gridMove` = 0), Holmes (release: navigation truthful + focus indicator),
Mace (release: `:focus-visible` added and `outline:none` deleted). Debord declined
to pull it, on the grounds that every defect he named was enumerated and measured.

**Andon resolution.** No further move was made while any cord was open. M1–M6
below are the joint resolution; all three release conditions are re-measured after
the cluster in the verification table.

---

## Moves

### Move M1: Delete the atmospheric layers (BREAK)
Depends on: none
Anchors: Stance `fft` | Breaker `samBreak` | Counterpoint `wcag -→ albers`
Intent: remove the one algebrized sign on the page so that whatever replaces it has
to be about Autheo rather than about crypto sites.
Formal argument: the drift-grid and the two blurred glows are the single most
automatized sign in this genre; Shklovsky's habitualization devours the work
precisely where the reader stops seeing it. Samara licenses breaking the grid;
WCAG's contrast floor constrains any replacement.
Alternatives rejected: (1) keep the grid and reduce its opacity — rejected, it
measures the same; (2) replace the glows with a gradient — rejected, it is the same
sign in a new material.
Consequence: the hero loses its only background event; the page must now carry the
eye with type and a figure.
Fence: the grid exists to signal "technical depth" cheaply. Breaking it costs the
cheap signal and buys a real one.
Frontier effect: opens F9 (a real figure).
Mode field: Advanced pole — a page with no borrowed atmosphere. Acceptable pole —
still reads as a technical site to a newcomer.

### Move M2: Draw the stack as an SVG cross-section (BREAK)
Depends on: M1
Anchors: Breaker `samBreak` | Rule `mb` | Stance `fft`
Intent: the centrepiece becomes the thing explained. Five strata, layer 03 marked
in the accent, an axis with a direction arrow.
Formal argument: the inherited stack was 19 `↓` glyphs with no defined CSS; the
figure is not decoration but the content itself, which is FTF's demand.
Alternatives rejected: (1) a stacked-card layout — rejected, it competes with the
cards below it; (2) a photograph or stock illustration — rejected, it asserts
nothing.
Consequence: ~60 lines of inline SVG, no request, scales to any width.
Fence: none broken — the grid was already broken in M1.
Frontier effect: opens the Tufte question (does the figure carry data?).
Mode field: Advanced pole — a diagram instead of ambience. Acceptable pole — it is
labelled with the same words the prose uses.

### Move M3: Make the navigation truthful (KEEP-THE-RULE)
Depends on: none
Anchors: Stance `fft` | Rule `wcag -→ c_qas`
Intent: four links that resolve; the absent topics become struck-through text, not
doors.
Alternatives rejected: (1) write the eight missing pages — rejected, inventing
content is worse than admitting its absence; (2) delete the topics outright —
rejected, the reader should see the shape of what is planned.
Mode field: Advanced pole — honest about scope. Acceptable pole — still shows the
full curriculum.

### Move M4: One focus ring, and delete the rule that removes it
Depends on: none
Anchors: Rule `wcag` | Rule `wcag -→ albers`
Alternatives rejected: per-component focus styles — rejected, they get forgotten.
Mode field: Advanced pole — every target visible. Acceptable pole — 3px ring,
`outline-offset: 2px`, both themes measured ≥ 4.99:1.

### Move M5: A measured palette in both themes
Depends on: none
Anchors: Rule `wcag -→ albers` (counterpoint)
Intent: one accent, one ink, one muted, declared once; 18 pairs printed by
`tools/contrast.mjs`.
Mode field: Advanced pole — a real palette. Acceptable pole — all 18 pass, lowest
4.99:1.

### Move M6: An acceptance test, run at the final state
Depends on: M1–M5
Anchors: Stance `fft` | Rule `wcag -→ c_qas`
Intent: `node tools/verify.mjs` — every reference resolves, every document closes,
no third-party host. One command, no judgement.

## Resolutions of R0 objections

| Critic | Resolution | Ground |
|---|---|---|
| Debord | ADAPT | All four of his items applied: missing stylesheet and script references deleted, `autheo.html` and `layer0.html` closed, the 12 orphan classes given rules, and `.highlight` made visible. |
| Shklovsky | ADAPT | `.grid-background`, `.glow`, `.glow1`, `.glow2` and `@keyframes gridMove` removed; `filter:blur(` count 0. Measured 2 → 0 and 3 → 0. |
| Holmes | ADAPT | Nav reduced to the four pages that exist; dead topics rendered as `.not-written`; focus ring added; `prefers-reduced-motion` and `scroll-padding-top` added. |
| Mace | ADAPT | `:focus-visible` added to both sheets; `outline:none` deleted (1 → 0). |

### Verification, measured after the moves (final state)

| Claim | Procedure | Before | After |
|---|---|---|---|
| `gridMove` occurrences in css/style.css | `grep -c` | 2 | **0** PASS |
| `filter:blur(` in css/style.css | `grep -c` | 3 | **0** PASS |
| `outline:none` declarations | `grep -c` | 1 | **0** PASS |
| Pages passing the acceptance test | `node tools/verify.mjs` | 0 of 4 | **4 of 4** PASS |
| Colour pairs passing WCAG | `node tools/contrast.mjs` | not measured | **18 of 18** PASS, lowest 4.99:1 |
| Third-party hosts on index.html | parse absolute URLs | 1 (fonts.googleapis.com) | **0** PASS |

## Frontier (after the moves)

| Candidate | Reached via | From anchor | Status |
|---|---|---|---|
| F1 delete non-resolving links | `asks about purpose with` | `fft` | TAKEN (M3) |
| F2 stop referencing missing CSS/JS | `asks about purpose with` | `fft` | TAKEN (M6) |
| F3 declared grid and type ratio | `codifies` | `mb` → `itstyle` | TAKEN (M5) |
| F4 cap the prose measure | `canon for` | `bring` → `lupType` | TAKEN (M5, 62ch) |
| F5 measure every pair | `measurable access for` | `wcag` → `c_qas` | TAKEN (M5) |
| F6 break the grid for the hero | `loosens` | `samBreak` | TAKEN (M1, M2) |
| F7 constrain the palette by measurement | `contrast floor constrains` | `wcag` → `albers` | TAKEN (M5) |
| F8 make Autheo the subject | `bounds the break of` | `maya` → `samBreak` | TAKEN (M2) |
| F9 replace the automatized sign | `debate context for` | `fft` → `lookC` | TAKEN (M1) |
| F10 drop the webfont | `asks about purpose with` | `fft` | TAKEN (M5) |

## Anchor Ledger

| Anchor | Role | Status | Evidence | Note |
|---|---|---|---|---|
| `fft` First Things First | Stance | KEEP | 10 dead links deleted; no page names a resource it lacks | Strongest objection survived: that the finish outran the content |
| `mb` Grid Systems | Rule | KEEP | type ratio 1.25, `--u` unit, `--measure: 62ch` | Survived Shklovsky's charge that the grid was algebrized — the drift-grid was the offender, not the grid |
| `wcag` WCAG 2.2 | Rule | KEEP | 18 pairs printed, lowest 4.99:1 | Survived Holmes's finding that the palette was already innocent |
| `bring` Elements of Typographic Style | Rule | KEEP | measure capped at 62ch | |
| `samBreak` Making and Breaking the Grid | Breaker | KEEP | atmosphere deleted; the grid broken for the figure | |
| `albers` Interaction of Color | Counterpoint | KEEP | palette measured, not chosen by taste | |
| `maya` MAYA | Governing criterion | KEEP | Autheo-centred but still a plain 4-item nav | |

---

## Panel, WHOLE, round R1 (artifact examined: `index.html`, `css/site.css`, the three inner pages; **unrendered**)

| Critic | Anchor used | Observed in the work | Verdict | Requested change |
|---|---|---|---|---|
| Usability (Krug) | Second Law of Usability — many clicks are fine, ambiguous ones are not | `blockchain-basics.html` nav: 3 real links, **7 struck through (70%)**; `layer0.html` 6 of 9 struck. Struck items contradict their own pages: "Validators" and "AI Agents" struck on `autheo.html`, which contains validator and AI sections. **No legend anywhere** for the strikethrough. And `autheo.html` — the primary CTA's destination — has **zero inbound links** from the other two pages | OBJECT | Rebuild all three inner navs to the canonical four-item set; delete the 15 struck items |
| Evidence (Tufte) | Graphical Integrity, principle 3 — show data variation, not design variation | Gradient `#3cff6e → #12b37a` runs along **x** across 1200 units in a dimension carrying no data (2.03:1 of design variation). Ruling: 6,000 sq units at a 90-unit pitch no band edge falls on, `aria-hidden`. Worst: labels are sized in **SVG user units**, so `.s-note` renders **3.5px at a 360px viewport** and 20.1px at 1920px | OBJECT, **Andon** | Labels ≥12px at 360px, and `grep -c 'url(#band)'` = 0 |
| Craft (Bringhurst) | §2.1.2 — a satisfactory measure is 45 to 75 characters, 66 ideal | The `h1` clamp `clamp(2.4rem, 7vw, var(--t-4))`: **the fluid term binds only across 549–558px**, a nine-pixel window. Below it, 38.4px type on a 280px measure = **14.6 characters per line**, five lines for a 68-character headline. He confirmed 62ch lands at ≈67 characters — inside the 45–75 — and found `--t-2` and `--t-3` declared and never spent | OBJECT | `clamp(1.75rem, 4.6vw + 1rem, var(--t-4))` |

Andon pulled: **yes, by Tufte.** Krug declined ("the worst case is a reader who works a little harder than they should").

**Andon resolution.** Both clauses measured after the fix: `url(#band)` count **0**; the smallest figure label is now `0.8rem` = **12.8px at every viewport width**, because the labels are HTML text on the page's own scale rather than SVG user units. The figure was rebuilt as a CSS cross-section — bands laid out by the same grid as the page, one bit of information (which layer executes) in one colour, no gradient, and the ruling deleted. The axis, which carries the one proposition the prose cannot (that these are *stacked*, read downward), now gets the ink: 2px accent, with an arrowhead.

### Resolutions of R1 objections

| Critic | Resolution | Ground |
|---|---|---|
| Krug | ADAPT | All three inner navs rebuilt to the canonical four items with `aria-current`; 15 struck items deleted; skip link and `<main id="main">` added to all three; the plumbing clause ("nothing on this site points at a page that does not exist") cut from the copy. `autheo.html` is now reachable from every page. |
| Krug (secondary) | ADAPT | `fill="var(--accent)"` and `stop-color="var(--accent)"` were unreliable in SVG presentation attributes — the Layer 03 band could resolve to black. Both now carry literal hex on the element with a CSS class override where `var()` is supported. |
| Tufte | ADAPT | Gradient and `<defs>` deleted (`url(#band)` 0); ruling deleted; figure rebuilt with HTML labels at 0.8rem minimum; figcaption now states that the five-layer reading is this site's own and not a quoted specification; the six figure pairs added to `tools/contrast.mjs`. |
| Bringhurst | ADAPT | `h1` clamp now `clamp(1.75rem, 4.6vw + 1rem, var(--t-4))` — the fluid term governs 320–501px instead of 549–558px. Independently recomputed: at 320px the headline goes from 14.6 to **17.9 characters per line** and from five lines to four; at 360px `h1` is **32.6px** against his 34px release ceiling. Also: `p` capped at `min(62ch, 34em)` to guard the fallback face whose "0" is wider, `--t-2` spent on the figure's layer names, `--t-3` deleted, and layer headings given more air above than below. |

### Verification at the final state

| Claim | Procedure | Value |
|---|---|---|
| `grep -c 'url(#band)' index.html` | grep | **0** PASS |
| Smallest figure label | read `css/site.css` | **0.8rem = 12.8px**, viewport-independent PASS |
| `h1` at 360px / headline lines | recomputed from the clamp | **32.6px** (≤34) / **4 lines** (≤4) PASS |
| Characters per line at 320px | recomputed | 14.6 → **17.9** PASS |
| Dead type tokens | `grep -c "^  --t-n:"` vs `grep -c "var(--t-n)"` | **0 dead** (`--t-2` now spent, `--t-3` removed) PASS |
| Pages passing acceptance | `node tools/verify.mjs` | **4 of 4** PASS |
| Colour pairs passing | `node tools/contrast.mjs` | **24 of 24** PASS, lowest 4.99:1 |
| `gridMove` / `filter:blur(` / `outline:none` | grep | 0 / 0 / 0 PASS |

## Open frontier (carried, not blocking)

| Item | Why it stays open |
|---|---|
| `autheo.html` prints 399 / 275 / 124 with no source and no date, and `:1062` contradicts the "124 remaining" card | Tufte; needs a figure the site can source, or deletion |
| `autheo.html` still renders the inherited `↓` diagram and still links `css/style.css` | The redesign reached `index.html` fully and the inner pages only enough to stop them lying |
| IBC: the inherited page claimed "IBC Native"; notes say IBC was disabled at a fork height | Not asserted either way on the page. Needs an answer from the owner |

## Stop test

- **S1** — Frontier has no OPEN items: the three above are carried as open *items*, not frontier candidates. **Met.**
- **S2** — A WHOLE round returned PASS from every required critic with no Andon. **Not met**: Krug and Tufte both returned OBJECT; Tufte's Andon is released by measurement, but neither has re-judged the artifact since the fix.
- **S3** — Two consecutive WHOLE rounds with no change. **Not met**: only one WHOLE round has run.
- **S4** — Ambition push, measured. **Met**: the boldest move (replacing the entire atmospheric system with the stack drawn as a cross-section) was escalated twice — first as SVG, then rebuilt as HTML after Tufte measured its labels at 3.5px. Delta recorded: `url(#band)` 1 → 0, smallest label 3.5px → 12.8px.
- **S5** — Every dotted edge leaving a used anchor applied or declined: `wcag -→ albers` applied (palette measured, M5); `crit_prov_debord -→ crit_use_krug` applied (the pair sat, and disagreed — Krug declined the Andon Debord's neighbours pulled). **Met.**

**The run is incomplete.** S2 and S3 are not satisfied. The resume point is a second WHOLE round on the artifact in its current state.

## Compliance check

- [x] Tooling inventory done — `references/anchor-graph.md` read; no graph/workflow tooling available; `Agent` used for seats
- [x] Mode stated with the reason — Adaptive, public teaching resource
- [x] Seed with exact labels, one dotted counterpoint (`wcag -→ albers`), living Frontier
- [x] At least one BREAK move taken (M1, M2); no quota used as a stopping rule
- [x] Decision Records written before each move
- [x] Panel Reports per round; every critic cited something observable
- [x] Every OBJECT resolved ADAPT, with measurements
- [ ] WHOLE rounds — one run; S2 and S3 not met
- [x] Every figure the artifact displays re-measured at the final state
- [x] Anchor Ledger complete
- [x] Double loop below
- [ ] Final reply states the mode, tools, stop conditions and everything skipped — see the closing report

## Double loop

Did the criterion, the panel or the graph fail the work? The panel did not — it caught two things I would have shipped: a flagship page with no inbound links, and a figure whose labels rendered at 3.5px. The graph did not either; `wcag -→ albers` is what turned a palette argument into 24 printed ratios. What nearly failed the work was my own sequencing: I applied the R0 cluster and pushed before R1 sat, so the first redesign shipped with a regression (the unreachable `autheo.html`) that only Krug found. The amendment is procedural, not graphical.

**Graph amendments.** Add a node for *legibility floor as a function of viewport* — a rule that any figure's smallest label must be measured at the narrowest supported viewport, not at the design width. The failure here (3.5px) was invisible at every width I looked at. And amend the panel roster rule: a seat for **Evidence** should sit in R0, not R1 — the inherited unsourced statistics were the single worst defect on the site and no one measured them until the second round.

## Carry-Forward

See `CARRY-FORWARD.md`. This run added: SVG user-unit labels do not answer to `rem` and will render illegible at narrow widths; `fill="var(--x)"` is unreliable in SVG presentation attributes; converting a dead link to struck-through text can remove a *real* page from the site's reach.
