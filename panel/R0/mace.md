# R0 Premortem — Seat: Ronald Mace, Principles of Universal Design

**Artifact:** `H:\blockchain-explain` (Autheo blockchain explainer, static site)
**Round:** R0 — premortem. Judged exactly as inherited, before any redesign move.
**Authority:** Ronald Mace and the seven Principles of Universal Design. No other doctrine cited.

---

## 0. What I judged, and a flag before anything else

I judged the **inherited** artifact: `index.html` at git `HEAD` (`0991d54`), 310 lines, and `css/style.css` (32,202 bytes, 2,527 lines), read in full.

**Flag for the panel:** while I was reading, `index.html` was rewritten under me. `git status` shows `M index.html`, mtime `2026-10-27 18:17:55`, `202 insertions(+), 295 deletions(-)` against HEAD. The working copy now has a `<main>`, a skip link, a `nav aria-label`, and a real `href` where `GitHub` was. That is a redesign move, not the inheritance. **My verdict is on the inherited file.** I note it because it matters: the fixes are landing in `index.html`, and the defect I am objecting to lives in `css/style.css`, which nobody has touched.

---

## 1. Statements of meaning — what the artifact says about who it is for

What I see the artifact doing, stated as neutrally as I can:

1. The site presents itself as a **teaching instrument**. Its own words: "This companion guide is designed to make advanced blockchain concepts approachable for developers, businesses, and curious learners" (`index.html:88`). It claims an audience of learners. A learner is precisely the person who cannot fall back on prior knowledge to reconstruct what the page fails to show them.

2. The site's navigation **promises eleven destinations and keeps four**. The `<nav>` at `index.html:40-66` offers Home, Blockchain, AUTHEO, Layer 0, Layer 1, Cosmos SDK, EVM, IBC, Validators, Identity, PQC, AI — twelve links, of which ten point at files that do not exist (`layer1.html`, `cosmos-sdk.html`, `evm.html`, `ibc.html`, `validators.html`, `did.html`, `pqcnet.html`, `ai-agents.html`, `faq.html`, `glossary.html`). The footer adds two more links — `GitHub` and `Documentation` at `index.html:298-299` — and both are `href="#"`.

3. The site **never tells a keyboard user where they are.** In 2,527 lines of CSS there is exactly one focus rule, and it is not on a link or a button — it is on a search field that appears on no page. I will show the measurement below.

4. The site **moves on its own and offers no way to ask it to stop.** `.grid-background` carries `animation:gridMove 30s linear infinite` (`style.css:2279`) and is instantiated on every page (`index.html:25`). `html{scroll-behavior:smooth}` (`style.css:22`) is unconditional. There is no `prefers-reduced-motion` query anywhere in the repository.

5. The site's **print form is unreadable.** `@media print` (`style.css:2483-2503`) flips `body` to `background:white;color:black` and stops there. Every rule that actually colours text is untouched. Measured below.

6. The site's **structural voice is missing.** Inherited `index.html` has `<header>`, `<nav>`, `<footer>` and bare `<section>` — no `<main>`, no skip link, no `aria-label` on the `<nav>`. Its heading order is `h2 → h1 → h3 → h2 → h3…`: the logo is an `<h2>` at `index.html:36` and it precedes the page's only `<h1>` at `index.html:80`.

---

## 2. Artist questions — questions to the maker

These are mine, asked of the person who built it, not answered by measurement:

- When you wrote `a{text-decoration:none}` at `style.css:166-172`, did you intend links in prose to carry no underline? What did you intend a reader to use instead?
- The twelve-item navigation bar reads as a map of a complete book. Was it written as a map of a book you intended to write, or as a description of a book that exists? I ask because the answer changes whether this is an unfinished site or a misleading one.
- `GitHub` and `Documentation` are both `href="#"`. Were they placeholders awaiting URLs, or were they never meant to resolve?
- The centrepiece "How Autheo Is Built" stack — the `architecture-stack` / `stack-layer` / `stack-arrow` / `highlight` classes have no rule in `style.css` and render as bare text with `↓` characters. Did you think of the `↓` as a diagram, or as a placeholder for one? A learner who cannot see the arrow glyph gets "Layer 3 ↓ Layer 2 ↓ Layer 1" as a run of words with a punctuation mark inside it.
- You loaded nine weights of Inter. Which one is the body weight? I could not find a rule that sets it.

---

## 3. Neutral questions — factual, answerable, and the answers I found

- **Does any `:focus` or `:focus-visible` rule exist in the CSS?**
  No `:focus-visible` anywhere in the repository — not in `style.css`, not in any HTML. Exactly one `:focus` rule exists: `style.css:1276`, `.search-box input:focus{border-color:var(--primary)}`. No HTML file contains the string `search-box`. So the only focus rule in the stylesheet targets an element that exists on zero pages.

- **Does the CSS remove a focus affordance anywhere?**
  Yes, once: `style.css:1272`, `outline:none` inside `.search-box input`. This is the significant one. The browser's native focus ring is the *only* focus affordance the site has on its 28 interactive elements, and the single place the stylesheet addresses focus is the single place it deletes that ring, substituting a 1px border-colour change from `rgba(60,255,110,.15)` to `#3CFF6E`.

- **How many interactive elements are there in inherited `index.html`?**
  28 `<a href>` elements: 12 in `<nav>`, 2 hero buttons, 10 `.feature-card` anchors, 4 in the footer. **Zero** have a focus style.

- **Is there a `prefers-reduced-motion` query?**
  No, in any file. Nor `prefers-contrast`, nor `forced-colors`.

- **Landmarks and heading order in inherited `index.html`?**
  `<main>`: absent. Skip link: absent. `nav aria-label`: absent. Heading order: `h2 → h1 → h3 → h2 → h3 ×11`. `href="#"` count: 2.

- **Images?** Zero `<img>` elements across all four pages, so no `alt` text question arises. Nothing is missing that should be there.

- **Is `lang` set?** Yes — `<html lang="en">`. Credited.

---

## 4. Measurements

### 4a. Contrast — computed with the WCAG relative-luminance formula

sRGB channel `c`: `c/255`, then `c ≤ 0.03928 ? c/12.92 : ((c+0.055)/1.055)^2.4`.
`L = 0.2126R + 0.7152G + 0.0722B`. Ratio `(L₁+0.05)/(L₂+0.05)`.
Alpha composites resolved against their stated backdrop.

**Text pairs — most pass, and I say so:**

| Ratio | Pair | Verdict |
|---|---|---|
| 20.38:1 | `h1` `#ffffff` on body `#050505` | pass |
| 15.72:1 | `.btn-primary` `#000` on `--primary` `#3CFF6E` | pass |
| 15.78:1 | `code` `#82ffab` on `pre` `#0b0b0b` | pass |
| 14.30:1 | `nav a` `#d8d8d8` on header over `#050505` | pass |
| 14.14:1 | `th` `#3CFF6E` on `#111` | pass |
| 13.59:1 | `.badge` `#3CFF6E` on its own tint | pass |
| 12.87:1 | `.hero-card li` `#d5d5d5` on card tint | pass |
| 11.93:1 | `p` `--muted` `#c6c6c6` on body | pass |
| 11.62:1 | `.docs-sidebar a` `#c8c8c8` on `#0d0d0d` | pass |
| 11.29:1 | `--warning` `#ffc107` on `#17140a` | pass |
| 10.72:1 | `footer a` `#bdbdbd` on `#070707` | pass |
| 5.84:1 | `--danger` `#ff5050` on `#1b0e0e` | pass |
| 5.75:1 | `--gray` `#888888` on `#050505` | pass (tight) |

The dark palette is genuinely well chosen for luminance. I am not objecting to the palette.

**The three text/background pairs that fail:**

| Ratio | Pair | Where | Needs |
|---|---|---|---|
| **1.71:1** | link `#ffffff` vs adjacent body text `#c6c6c6` | `style.css:166-172` + `158-164` | 3:1 (WCAG 1.4.1, colour alone) |
| **1.71:1** | `p` `#c6c6c6` on `white` | `@media print`, `style.css:2483-2503` | 4.5:1 |
| **1.34:1** | `.green` `#3CFF6E` on `white` | `@media print`, same block | 4.5:1 |

The first is the one I want the panel to hold. `a{text-decoration:none;color:white}` sits beside `p{color:var(--muted)}`. In a paragraph, a link is distinguished from its surrounding prose by **nothing but a 1.71:1 luminance difference** — no underline, no weight change, no icon. WCAG 1.4.1 requires 3:1 between link text and body text when colour is the only differentiator. This misses it by a wide margin, and for a reader with low vision or a degraded display the link simply merges into the sentence.

The second and third mean the print stylesheet is not an accessible alternative format — it is a broken one. Every paragraph prints at 1.71:1 on white. `code` prints at 1.25:1. `.gray` at 1.90:1. The document was given a print mode that makes it harder to read than the screen.

**Non-text / UI boundary contrast (WCAG 1.4.11, 3:1):**

| Ratio | Element | Source |
|---|---|---|
| **1.17:1** | `.feature-card` border `rgba(60,255,110,.10)` → `rgb(11,30,16)` on `#050505` | `style.css:725` |
| **1.82:1** | `.btn-secondary` border `rgba(60,255,110,.25)` → `rgb(19,68,31)` on `#050505` | `style.css:534` |
| **1.12:1** | `header` bottom border `rgba(60,255,110,.08)` → `rgb(9,25,13)` | `style.css:301` |
| **1.41:1** | `.step-number` `rgba(60,255,110,.15)` → `rgb(23,53,31)` on `#111` | `style.css:1767` |
| 2.14:1 | `.timeline` rail `rgba(60,255,110,.30)` | `style.css:1126` |

The green is beautiful at 15.26:1 as a solid and invisible at .10 alpha (1.17:1). `.btn-secondary` — one of the two primary calls to action on the home page ("Explore Architecture", `index.html:100-104`) — is bounded by a 1.82:1 line. Its label passes at 11.20:1 against the border's own colour, so the words are readable; the *control* is not locatable. And `.step-number` at 1.41:1 is a numeral carrying sequence information at 3rem/900 weight — large text, so 3:1 is the bar, and 1.41 misses it.

### 4b. The focus audit, in one line

**Zero of 28 interactive elements in inherited `index.html` have a focus style. The stylesheet contains no `:focus-visible` rule and, at line 1272, removes the browser's native outline on the one element it does style.**

### 4c. A latent trap I am logging, not objecting to

`.fade-up{opacity:0}` (`style.css:2155-2158`) is gated on a `.visible` class that only `js/app.js` can add. There is no `js/` directory. So any content marked `fade-up` is permanently invisible to everyone. I checked all four pages: **zero** use `fade-up`, `fade-left` or `fade-right`. The trap is armed but not stepped on. I log it as an open item because the next page someone authors with a `fade-up` class ships blank.

---

## 5. Opinions — last, and mine

**My literary anchor is Ronald Mace's Principle 1, Equitable Use, guideline 1a: "Provide the same means of use for all users: identical whenever possible; equivalent when not."**

That guideline is the whole objection, and it is why I am not satisfied by the palette passing. Equitable Use is not a demand that the colours be legible — the colours here are legible, generously. It is a demand that **the means of use be the same**.

Consider what the site gives two readers on the home page. The mouse user gets 28 reachable targets, hover states on every card, an underline animation under every nav item on hover (`style.css:397-401`), a lift, a glow, a ripple. The keyboard user gets 28 reachable targets and **no signal at any of them** — because the entire hover vocabulary of this design (colour shift, underline sweep, `translateY`, `box-shadow`) is bound to `:hover` and to nothing else. Same destinations, different means of use, and the difference is not equivalent — it is the difference between knowing where you are and not knowing.

And then the navigation itself. Ten of fourteen links are dead. For a mouse user that is a disappointment discovered one click at a time. For a screen-reader user who pulls the links list — the standard, efficient way to read a page's structure — it is **the site's primary interface arriving 83% broken**. There is no equivalent route. There is no search (the `.search-box` is CSS with no markup). There is no sitemap. The `<nav>` is unlabelled, so it does not even announce itself as navigation. Mace's 1a says identical when possible, equivalent when not; here the second-rate route was not built, and the first-rate route does not work.

I want to be precise about what I am *not* saying. I am not saying the design is ugly. The dark-green palette is disciplined and the contrast maths is, for screen text, genuinely good — better than most sites this panel will see. I am saying that the design has one complete sensory channel (sighted, pointer-driven, motion-tolerant) and a fragmentary one (everything else), and that the fragmentary one is the one a learner with a disability is handed. A teaching site that says "approachable for… curious learners" and then offers no focus ring, no reduced-motion path, no working navigation, no landmarks and a print stylesheet that renders body text at 1.71:1 has made an audience decision it did not announce.

Mace's own line — that universal design is not a special feature for a minority but a design that works for people of all abilities from the start — is the reason I am not willing to file this as polish. Focus rings and reduced-motion are not accommodations to be added later. They are the means of use, and here they are absent from the shared stylesheet, which means every page the panel authors from now on inherits the absence.

**Opinion, stated plainly:** this is the strongest candidate for an Andon I have seen in this panel's inherited material, because the defect is not in a page — it is in `css/style.css`, and it is therefore multiplied by every page yet to be written. Fixing `index.html` while `style.css` goes untouched fixes one file and leaves the factory running.

---

## Concrete requested change (one)

Add, at the end of `css/style.css`, one universal focus rule — and delete the line that suppresses the native one:

```css
/* Universal Design — Principle 1, Equitable Use: identical means of use for
   pointer users and keyboard users. Hover vocabulary must have a focus twin. */
:focus-visible{
    outline:3px solid #82ffab;      /* --primary-light; 16.35:1 on #050505 */
    outline-offset:3px;
    border-radius:6px;
}
```

and at `style.css:1272` **delete `outline:none;`**, changing `.search-box input:focus` (line 1276) to `.search-box input:focus-visible` so the field keeps a real ring rather than a 1px border tint.

One rule. It covers all 28 elements in `index.html` and every interactive element in every page the panel writes next, and the ring measures **16.35:1** against `#050505` — more than five times the 3:1 that WCAG 1.4.11 asks for.

**Logged as open items, not blocking:** the 10 dead internal links; the 2 `href="#"` footer links; the missing `<main>` / skip link / `nav aria-label`; the `h2`-before-`h1` heading order; the 1.71:1 link-vs-prose contrast; the print stylesheet; the missing `prefers-reduced-motion` query; the 12 orphan CSS classes including the four diagram classes; the unclosed-tag imbalance in `autheo.html` and `layer0.html`; the armed-but-unused `.fade-up` invisibility trap.

---

## Andon

**Yes — I pull the Andon.**

Scoped narrowly, and it is a stop on **authoring new pages**, not on the panel: no further page should be written against `css/style.css` until a `:focus-visible` rule exists in it and `outline:none` at line 1272 is gone. Every page authored before that lands inherits a design with 28 invisible targets. The change is eight lines, the measurement is already done (16.35:1), and once it is in, the Andon clears and the panel proceeds unblocked.

---

## Verdict

**Verdict: OBJECT**

**Requested change:** add a single `:focus-visible` rule to `css/style.css` and remove `outline:none` at `style.css:1272`.

**Andon: yes.**
