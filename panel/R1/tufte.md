# R1 — Tufte seat (Adaptive mode)

**Authority:** Edward Tufte, *The Visual Display of Quantitative Information* (1983).
One anchor, used for every judgement below:

> **Chapter 2, "Graphical Integrity," principle 3 — "Show data variation, not design variation."**

**Artifact examined:** `index.html` (217 lines), `css/site.css` (507 lines), `tools/contrast.mjs`,
`DESIGN-LOG.md`; plus `autheo.html`, because `index.html:59` makes it the page's primary call to
action. Every claim below is either read from the source or computed, and the procedure is named
each time. Ratios are WCAG relative luminance, `node -e` with the formula in `tools/contrast.mjs`.

---

## 1. Statements of meaning

What the work says about itself, before I judge it:

- It says: Autheo has five layers and they are **stacked**. The order is the point, not the list.
  05 at the top, 01 at the bottom, and a vertical axis at x=28 with an arrowhead at y=492 saying
  read downward.
- It says: one of the five is not like the others. Layer 03 is painted in the accent; the other
  four are not. The figcaption names why: *"Layer 03 is where applications actually execute."*
- It says: this is a **cross-section** — the figcaption's own word. A cut through a solid, with
  strata.
- It says: the figure is the thing being explained, not an illustration beside the text. The
  source comment at `index.html:65-66` says so outright: *"The graphic is the thing being
  explained… It is drawn in the document, not loaded."*
- It says: this site is careful. `index.html:181-182` asserts *"nothing on this site points at a
  page that does not exist,"* and that is true of the four links it offers.
- It says, by `aria-hidden="true"` on `.strata-grid` (line 77) and `.strata-axis` (line 116): the
  ruling and the axis carry nothing for a reader who cannot see them.

## 2. Artist questions

- You wrote in the source that the graphic *is* the thing being explained. Then why does the page
  explain the same five things again, in prose cards, immediately below it — `index.html:130-175`,
  the same five numerals, the same five names, the same order, with the marked layer marked again
  by `.layer-marked { border-color: var(--accent) }`?
- The gradient runs left to right across a band whose width is a constant 1200 for all five
  strata. What does the left edge of layer 03 know that the right edge does not?
- The figcaption calls it a cross-section. Cross-section of what, cut at what scale? What is the
  unit on the axis at x=28?
- Is "five strata" Autheo's published architecture, or your reading of it? The page never says, and
  the footer's only pointer is to your own repository.
- You replaced the inherited `↓` stack because its classes were never defined. The page your
  primary CTA points to (`autheo.html:920-968`) still renders `<div class="arrow">↓</div>` three
  times. Was the replacement meant to reach only `index.html`?

## 3. Neutral questions — and the measurements that answer them

**Q: Does the geometry vary with anything?**
*Procedure: read every `rect` in the SVG.* All five: `x="0"`, `width="1200"`, `height="62"`;
y = 80, 170, 260, 350, 440 (pitch 90). No attribute of any rect is a function of a quantity.
Vertical position varies, and it encodes ordinal rank — which is *also printed*, as text, at x=56
(05, 04, 03, 02, 01). The positional dimension duplicates a printed one; one of the two is
redundant.

**Q: What is the figure's ink budget?**
*Procedure: area from the viewBox and the rect attributes.*

| Ink | Computation | Units | Carries |
|---|---|---|---|
| Strata fills | 5 × 1200 × 62 | 372,000 | 1 bit (marked vs not), on 74,400 of it |
| Grid ruling | 5 × 1200 × 1 | 6,000 | nothing (`aria-hidden="true"`) |
| Axis line + arrowhead | 422 × 1 + ~12 | ~434 | direction of reading |
| Labels | 10 `<text>` runs | — | all five names, notes, numerals |
| Figure, total | 1200 × 520 | 624,000 | |

**Q: Is the gradient data-ink or design-ink?**
This is the one that matters, and it splits. `<linearGradient id="band" x1="0" y1="0" x2="1" y2="0">`
runs `#3cff6e → #12b37a` along **x**. Measured: **2.03:1** between the two stops. The x-axis of that
rect carries nothing — every stratum is 1200 wide, and nothing is placed, ordered or measured along
x. So:

- the **hue** is data-ink: one bit, *this stratum is the execution layer* (12.92:1 against the
  adjacent band);
- the **ramp** is not: it depicts a continuous 2.03:1 variation across 1200 units in a dimension
  where the data has zero dimensions.

That is design variation drawn in the place where data variation belongs. One rect, half honest.

**Q: Do the strata read as strata?**
*Procedure: WCAG luminance ratio of the band fill against the SVG's own ground.*

| Pair | Tokens | Ratio |
|---|---|---|
| band fill vs svg ground | `--raised` #171c19 on `--panel` #121614 | **1.057:1** |
| grid ruling vs svg ground | `--rule` #232b26 on `--panel` #121614 | **1.256:1** |
| axis line vs svg ground | `--rule` on `--panel` | 1.256:1 |
| accent band vs adjacent band | `#3cff6e` on `#171c19` | **12.92:1** |

The bands are painted in `--raised` — the same 5/255-per-channel step this design system uses
between `--paper` and `--panel`, i.e. the *elevation* token, the material of a card. The cross-section
reads as stacked panels, and the page then draws the same five items again as panels at
`index.html:130-175`. Note where the ink went: the axis line carrying the one proposition the prose
does not carry (that these are *stacked*, read downward) is at 1.256:1, while the decorative ramp is
at 12.92:1. **The ink is allocated inversely to the information.**

**Q: What does the ruling measure?**
`<path d="M0 60h1200M0 150h1200M0 240h1200M0 330h1200M0 420h1200"/>`. Band edges are 80/142,
170/232, 260/322, 350/412, 440/502. No gridline falls on any band edge; each falls in the 28-unit
inter-band gap, 8 below the band above and 20 above the band below, and the first sits 20 above
band 05. So it is neither a boundary rule nor a scale — a 90-unit pitch that nothing is read
against. The author agrees: `aria-hidden="true"`, line 77.

**Q: Does the figure show anything at the size most readers will meet it?**
*Procedure: `.strata { width: 100%; height: auto }` with `viewBox="0 0 1200 520"` — uniform scale is
containerWidth/1200. Label sizes are hardcoded in user units (`.s-num` 15, `.s-name` 21, `.s-note`
13), so they scale with the viewport and not with the reader's root font size.*

| Viewport | SVG width | Scale | `.s-note` renders | `.s-num` renders |
|---|---|---|---|---|
| 360px | 320px | 0.267 | **3.5px** | 4.0px |
| 768px | 704px | 0.587 | **7.6px** | 8.8px |
| 1440px | 1376px | 1.147 | 14.9px | 17.2px |
| 1920px | 1856px | 1.547 | 20.1px | 23.2px |

At 1920px the note label is 20.1px — larger than the page's `--t-1` (20px), the size of an `h2`.
At 360px it is 3.5px. Neither end sits on the page's 1.25 modular scale, because user units do not
answer to `rem`. `DESIGN-LOG.md` M2 claims the figure "scales to any width." It does scale — into
illegibility.

**Q: Is any figure printed without a procedure to reach it?**
- On `index.html`: **no quantitative figure is printed at all.** 05–01 are ordinal labels, not
  measurements. `grep` for 399 / 275 / 124 over `index.html` returns nothing. The page makes no
  numeric claim. On the narrow question as asked: PASS.
- But the figure itself is undocumented. Nothing states whether "five strata" is Autheo's published
  architecture or this site's reading of it, and there is no as-of date. The one place the page
  relaxes its own standard — it is scrupulous enough elsewhere to assert, truly, that no link
  dangles — is the graphic.
- One click away, at the destination of the primary CTA (`index.html:59` → `autheo.html`), three
  figures are printed with no source and no date: `399` (`:988`), `275` (`:1010`), `124` (`:1031`),
  each in an `<h2>` inside a `.stat-card`. The arithmetic holds (399 − 275 = 124). `399` is printed
  twice (`:934`, inside the surviving `↓` diagram). And `:1062` says remaining capacity "is reserved
  according to network participation requirements and enterprise partnerships" — which is quoting
  the figure out of context. `autheo.html:19` still links `css/style.css`, the inherited sheet, so
  the redesign has reached `index.html` only, and the artifact the CTA delivers is the inherited one.

**Q: Is the graphic's own documentation honest?**
`css/site.css:9-10` claims: *"Every text/background pair used here is listed and measured in
tools/contrast.mjs."* That file lists 18 pairs. It does not list `--muted` on `--raised`
(#9ba8a0 on #171c19) — the pair used by `.s-num` and `.s-note`, i.e. 8 of the 10 text runs in the
figure. It does not list the values actually painted either: `.s-num-on` at `opacity: .75`,
`.s-note-on` at `opacity: .8`. I measured all four as-composited:

| Pair as painted | Ratio | Verdict |
|---|---|---|
| `.s-num` / `.s-note` — `--muted` on `--raised` | 6.99:1 | passes |
| `.s-name` — `--ink` on `--raised` | 14.57:1 | passes |
| `.s-num-on` @ 0.75 on gradient end | 4.72:1 | passes |
| `.s-note-on` @ 0.80 on gradient end | 5.22:1 | passes |

So this is a documentation defect, not an access defect: the graphic's colour work is sound and
unmeasured. An unmeasured figure is an undocumented figure. Six lines in `PAIRS` fixes it.

*(Latent, not reachable: `[data-theme="light"]` sets `--on-accent: #ffffff`; white on the gradient
end `#12b37a` is 2.71:1, and `.s-note-on` at 0.8 is 2.23:1. No page sets `data-theme`, so this is
dead CSS today. Not an objection — noted because it is one line of CSS away from being live.)*

## 4. Opinions

The figure is a labelled diagram, not a data graphic, and I will not pretend otherwise by quoting a
data-ink ratio for it. Tufte's own book is full of diagrams; a diagram is not a lesser thing. But
principle 3 applies to any surface that varies, and this surface varies in three places where the
data does not:

1. **The gradient.** A 2.03:1 ramp across 1200 units in a dimension with no data behind it. This is
   the clearest instance of design variation standing in for data variation on the page, and it is
   inside the one rect that otherwise does honest work.
2. **The ruling.** 6,000 square units of stroke at a 90-unit pitch that no band edge falls on,
   measuring nothing, at 1.256:1 against its ground — and declared `aria-hidden` by its own author.
3. **The redundancy.** The single bit the figure uniquely carries — 03 is the execution layer — is
   also carried by the numeral, by the figcaption sentence, and by `.layer-marked` on the card
   below. Meanwhile the proposition only the figure can carry (that the five are *stacked*) is
   drawn in the faintest ink in the box, and the four bands that would make "stacked" visible are
   filled at 1.057:1 in the site's card-elevation material.

Does it carry information, or decorate? Both, and the split is measurable: it carries one real
proposition (stacking) and one real distinction (03), and spends 372,000 square units of fill plus
6,000 of ruling to do it. Strip the fills and the ruling and every fact in the figure survives in
the ten `<text>` runs. That is the test, and the figure fails it.

Is any figure printed without a procedure? Not on this page — and I want to credit that, because
the inherited 399 / 275 / 124 are gone from `index.html` and the page now asserts no number at all.
But the page has swapped an unsourced statistic for an unsourced architecture, and the unsourced
statistic is still live one click away on `autheo.html`, unchanged, alongside the `↓` diagram this
run was convened to replace.

**Verdict: OBJECT**

**Requested change (one):** remove the horizontal gradient. Replace
`<rect x="0" y="260" width="1200" height="62" fill="url(#band)"/>` with `fill="var(--accent)"`, and
delete the `<defs><linearGradient id="band">…</linearGradient></defs>` block. One bit, one colour,
no ramp along a dimension that carries nothing.

If you also: (a) delete `<g class="strata-grid">`; (b) give the axis the ink the ruling has — the
axis carries the figure's only real proposition; (c) have the figcaption name the source and as-of
date for the five-stratum architecture, or state plainly that it is this site's reading; (d) add the
four missing pairs to `tools/contrast.mjs` so `css/site.css:9-10` is true.

**Andon: yes.**

*Release condition (one, two measurable clauses):* every label in the figure renders at **≥ 12px at
a 360px-wide viewport** — currently `.s-note` renders at 3.5px, measured as
`13 × (360 − 40) / 1200` — **and** `grep -c 'url(#band)' index.html` returns **0**.

The first clause is the one that holds the release: a graphic whose labels are 3.5px does not show
the data at the size its readers have. If the 1200-unit viewBox cannot meet that floor, the figure
needs a narrow-width redraw (a second inline SVG with a narrow viewBox, swapped by media query, or
the labels moved out of SVG into positioned HTML) — the mechanism is yours, the floor is not.
