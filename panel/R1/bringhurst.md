# R1 — Bringhurst seat (Adaptive)

**Artifact:** `H:\blockchain-explain` (`index.html`, `css/site.css`), branch `thoth-division`
**Round:** R1, whole
**Authority:** Robert Bringhurst, *The Elements of Typographic Style* — measure, rhythm, the 45–75 character line. Nothing else is borrowed here.

**The one anchor I am arguing from:**

> "Anything from 45 to 75 characters is widely regarded as a satisfactory length of line for a single-column page set in a serifed text face in a text size. The 66-character line (counting both letters and spaces) is widely regarded as ideal."
> — Bringhurst, *The Elements of Typographic Style* (4th ed.), §2.1.2, "Choose a comfortable measure".

---

## 1. Statements of meaning

What I take this artifact to be doing, as observable declarations:

- It is a **reading room**, not a brochure. `p` is capped (`css/site.css:136`), the wrap is capped at 68rem (`site.css:113`), and the longest prose on `index.html` is six sentences spread over five cards. It asks to be read in a column.
- It declares **one modular scale** and means it. `--t--1` … `--t-4` at `site.css:14–19`. I checked the arithmetic: 1.25⁻¹ = 0.8, 1.25¹ = 1.25, 1.25² = 1.5625 → 1.563, 1.25³ = 1.953125 → 1.953, 1.25⁴ = 2.44140625 → 2.441. Every step is exact to the declared ratio. Six steps, one ratio, no drift. Declared claim **verified**.
- It declares `--u: 0.5rem` (8px) at `site.css:36` and then spends it consistently — every margin, padding and gap in the sheet is `calc(var(--u) * n)`. I counted roughly thirty spend sites; I found none that steps outside it. Declared claim **verified**.
- It applies `--measure: 62ch` to `p` (`site.css:21`, `:136`). Declared claim **verified**.
- `h1` is `clamp(2.4rem, 7vw, var(--t-4))` with `letter-spacing: -0.03em` (`site.css:231, 233`) and `max-width: 22ch` (`:234`). Declared claim **verified**.
- Body `line-height: 1.6` (`site.css:74`). Declared claim **verified**.
- System font stack (`site.css:23–24`), no `@font-face` anywhere in `site.css`, and `<head>` in `index.html:1–9` carries exactly one `<link>`, to `css/site.css`. No webfont. Declared claim **verified**.

All six declarations are true as written. I did not have to take them on trust.

### The `ch` question, answered

`ch` resolves to the advance of "0". In this stack — Segoe UI, Roboto, Helvetica, Arial — the digit advance is 0.556em. So:

- `62ch` = 62 × 0.556em = **34.47em** = **551.6px** at 16px.
- The average character of English prose, counting spaces, runs ≈ 0.50–0.52em = **8.0–8.3px** at 16px.
- 551.6 ÷ 8.15 ≈ **67 characters**. The range across that average is 66–69.

**So 62ch does not land past 75. It lands at about 67 — within two characters of Bringhurst's stated ideal of 66.** The cap is not naive; it is close to exact.

Two things follow, and both are worth recording:

- **`ch` is the right unit here, and it is better than `em` would be.** Because `ch` is font-size-relative, `62ch` holds ≈67 characters at 16px body *and* at the 12.8px figcaption (`site.css:422`) *and* anywhere else it is inherited. A cap in `em` would hold a constant width and a drifting character count. That is a real virtue, and it is why `.strata-wrap figcaption` at `--t--1` is correctly measured rather than merely narrow.
- **It is face-dependent, and the sheet has one unguarded exit.** The stack ends in the bare `sans-serif` (`site.css:23`). On a Linux box where that resolves to DejaVu Sans (digit 0.636em), `62ch` = 630px = **77 characters** — just past the ceiling. Not a failure on any face this stack names first; a hole at the last fallback. Logged below, not objected.

The `.lede` overrides to `46ch` at `--t-1` (`site.css:244–246`): 46 × 0.556 × 20px = 511px ÷ 10px = **≈51 characters**, with leading 1.6 × 20 = 32px. Larger type, shorter measure, wider leading. That is a correct lede, not a violated one.

---

## 2. Artist questions

- Did you choose `7vw` in the `h1` clamp (`site.css:231`) intending it to be the working term, or only as a guard? I ask because I want to know whether the narrow window I measured below is intent or accident.
- When you wrote `max-width: none` at `site.css:411, 476, 517, 538`, were you releasing those four small-text contexts from the measure deliberately — because each is currently a short string — or did the cap get in the way of a layout and get switched off?
- Is `--u: 0.5rem` (`site.css:36`) meant to be a *baseline* unit or only a *box* unit? Every margin spends it; no line box lands on it. I cannot tell which you meant.
- `--t-2` and `--t-3` are declared (`site.css:17–18`) and referenced nowhere in the sheet. Are they held for the sub-pages, or are they aspirational?
- `line-height` went 1.7 → 1.6 against the inherited sheet. What did you want the page to feel more of?

---

## 3. Neutral questions

- What is the intended floor viewport? The smallest breakpoint in the sheet is `max-width: 30rem` (`site.css:358`); below `40rem` the wrap padding drops to `calc(var(--u) * 2.5)` (`:118–122`), so a 320px viewport yields a 280px content measure.
- Does `tools/contrast.mjs` assert anything about measure or leading, or only about luminance pairs? I am holding the reversed-setting question (below) pending that.
- Are `.s-note`, `.cards p` and `.layer p:last-child` ever populated from longer source strings on `autheo.html`, `blockchain-basics.html` or `layer0.html`? The three files exist in the repo root.

---

## 4. Opinions

**The measure is the strongest thing on this page, and I would not touch it.** 62ch ≈ 67 characters, computed, at every size in the same face. Against an inherited sheet that set `p` in a `width: 80%` container with no `ch` cap at all, this is the single largest typographic gain in the redesign. It is also, I note, a *sans-serif* 67: Bringhurst frames 45–75 for a serifed text face, and sans generally wants the shorter half of that band. 67 sits high-ish in the band for a sans; it is inside it, not outside it.

**Opinion 1 — the `h1` clamp is inert, and on a phone it sets a 15-character line.** This is my objection. `clamp(2.4rem, 7vw, var(--t-4))` (`site.css:231`): 7vw = 2.4rem at a 548.6px viewport, and 7vw = 2.441rem at a 558px viewport. So the fluid term binds **only between 549px and 558px — a nine-pixel window.** Everywhere below, `h1` is pinned at its floor, 38.4px; everywhere above, at its ceiling, 39.06px. The clamp is arithmetic that almost never fires.

The consequence is on the device most readers will use. At a 320px viewport the wrap gives 280px of measure; `h1` sets at 38.4px, average character 19.2px → **14.6 characters per line.** The headline at `index.html:45–49` is 68 characters, so it sets in **five lines** at 42.2px leading — a 211px slab of 900-weight type tracking -0.03em, on a 15-character measure. At 375px: 17.4 characters per line, four lines. Desktop is fine: `max-width: 22ch` (`:234`) gives ≈24 characters per line, three lines. It is only the small end that is broken, and it is broken because the size is fixed while the measure is not. A display size that does not fall as the column falls is a measure error, and measure is the thing I am here for.

**Opinion 2 — the unit and the leading are incommensurable.** `--u` = 8px governs every margin, padding and gap in the sheet. But no line box in the document is a whole number of `--u`:

| setting | computed leading | in `--u` |
|---|---|---|
| body, 16px × 1.6 (`site.css:74`) | 25.6px | 3.2u |
| small, 12.8px × 1.6 (inherited) | 20.48px | 2.56u |
| `.prose h2`, 20px × 1.1 (`:132, 433`) | 22px | 2.75u |
| `.layer h3`, 16px × 1.1 (`:132, 468`) | 17.6px | 2.2u |
| `h1`, 39.06px × 1.1 (`:132`) | 42.97px | 5.37u |

So the page has a block rhythm but no baseline rhythm; the two systems meet and never coincide. Partial credit where it is due, because it is not nothing: 20.48 × 1.25 = 25.6 **exactly**, so body and small text do reconcile — every 4 body lines = 5 small lines = 102.4px = 12.8u. The type ratio itself supplies a long-period reconciliation. But 12.8u is a long cycle, and the 1.1 headings (ratio 1.1/1.6 = 0.6875) are on no such relation at all.

**Opinion 3 — inside the cards, a heading gets less air than a paragraph.** `.layer-num` → `h3` is `var(--u)` = 8px (`:464`); `h3` → `p` is `var(--u)` = 8px (`:469`). Two structurally different breaks, one interval. Meanwhile two paragraphs of the *same* body text are separated by `calc(var(--u) * 3)` = 24px (`:137`). The paragraph break gets three times the air of the heading break. `.prose h2` gets this right — `calc(var(--u) * 4)` = 32px plus a rule (`:437–439`). The card headings do not. Vertical space is a scale of relationships; here three levels read as one.

**Opinion 4 — the four `max-width: none` releases are latent, not actual.** At `site.css:411` (`.s-note`, mono, 12.8px) the available column at a 1920px viewport is roughly 1700px; in a monospace face at 12.8px that is a **241-character** capacity. Nothing in `index.html` is long enough to reach it today — the longest `.s-note` is 39 characters (`index.html:89`). So this is not a defect in the artifact as it stands; it is a cap removed from four contexts where a longer string would run past 75 with nothing to stop it. I am logging it, not objecting to it.

**Opinion 5 — on the inherited 1.7 → 1.6.** Dropping body leading from 27.2px to 25.6px while holding a 67-character measure bought tightness and gave up air. On a reversed setting — `--ink #e8ede9` on `--paper #0a0c0b` (`site.css:26, 29`) — light type on near-black reads as if it spreads, and the long end of the measure is where it shows first. 1.6 is defensible; it is not an improvement on 1.7, and if any change is made to leading here it should go up, not down. Against the inherited sheet's nine near-black greys, the reduction to two text greys (`--ink`, `--muted`) does give the column an even typographic colour, which is the point. Luminance itself belongs to the contrast seat, and I leave it there.

---

## Verdict: **OBJECT**

One concrete change requested:

**`css/site.css:231` — replace the inert clamp with one whose floor actually tracks the measure:**

```css
/* was: font-size: clamp(2.4rem, 7vw, var(--t-4));  — fluid term binds only 549–558px */
font-size: clamp(1.75rem, 4.6vw + 1rem, var(--t-4));
```

Numbers, so this can be checked rather than argued: at 320px this resolves to 30.7px → 280px measure ÷ 15.35px ≈ **18 characters per line**, four lines at 33.8px leading. At 360px: 32.6px → **19.6 characters per line**. It reaches the `--t-4` ceiling (39.06px) at a 501px viewport and holds there upward, so the desktop headline is unchanged. The fluid term now governs 320–501px instead of 549–558px. The `1.75rem` floor is a safety net that should never bind; `max-width: 22ch` at `:234` needs no change — it already yields ≈24 characters per line on desktop, which this brings the small end into line with.

**Andon: no.** This is one declaration on one line; it does not reach the layout, the scale, the figure or the measure token, and everything else on the page can proceed to R2 while it lands. I will pull the cord next round if R2 returns with `h1` still pinned at a fixed 2.4rem floor below 549px — release condition: computed `h1` font-size at a 360×640 viewport ≤ 34px, and the headline setting in no more than four lines.

**Open items, non-blocking, for the log:**

1. `site.css:23` — the stack's bare `sans-serif` fallback can resolve to a face whose digit is 0.636em, taking `62ch` to ≈77 characters. Guard it with `max-width: min(62ch, 34em)` on `p` (`:136`) if the exact band matters on Linux.
2. `site.css:411, 476, 517, 538` — four `max-width: none` releases. Latent only; re-raise if those contexts get long strings.
3. `site.css:17–18` — `--t-2` (1.563rem) and `--t-3` (1.953rem) are declared and never referenced. They are exactly the two steps between the largest text in use (`--t-1`, 20px) and `h1` (39.06px), so the display-to-text jump is two steps at once. Use them or drop them, but a six-step scale that uses four is a claim not yet made.
4. `site.css:74` vs `:36` — no line box is a whole multiple of `--u`. Worth deciding whether `--u` is a baseline unit or only a box unit; if the former, derive leading from it.
5. `site.css:464, 469` vs `:137` — 8px heading intervals against a 24px paragraph interval.
