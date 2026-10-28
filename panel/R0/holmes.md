# R0 Premortem — Holmes Seat

**Authority:** Kat Holmes, *Mismatch: How Inclusion Shapes Design* — exclusion is produced by the
relationship between a person and a design, not by the person.
**Round:** R0, premortem. Judged exactly as inherited, before any redesign move.
**Artifact:** `H:\blockchain-explain`
**Files read:** `index.html` (311 lines), `css/style.css` (2,527 lines, 32,202 bytes — read in full).

---

## 1. Statements of meaning

What I see, before I judge it.

The artifact is a four-page static site that presents itself as a **twelve-topic curriculum**.
`index.html` carries a twelve-item `<nav>` (lines 42–64) and a ten-card grid (lines 154–272),
each card naming a distinct blockchain topic. The page states its own audience at line 88:

> "This companion guide is designed to make advanced blockchain concepts approachable for
> developers, businesses, and curious learners."

The site renders as a dark near-black field (`body { background:#050505 }`, style.css:27) with a
single saturated green accent (`--primary:#3CFF6E`, style.css:58) used for the logo dot, the badge,
the primary button, section rules, card top-lines, timeline dots, table headers, and every hover
state. The visual language is finished and confident: sticky blurred header, radial glows, a moving
60px grid, hover lifts, ripples, float and pulse keyframes.

What the filesystem says is different. `H:\blockchain-explain` contains four HTML files —
`index.html`, `autheo.html`, `blockchain-basics.html`, `layer0.html` — and `css/` contains one file.

So the meaning the page declares (twelve topics, approachable) and the meaning the files carry
(four topics, one stylesheet) do not agree. I describe that gap before I evaluate it.

---

## 2. What I measured

### 2a. Contrast — the palette passes, and I will not pretend otherwise

I computed WCAG 2.x relative luminance and contrast for every text/background pair I could find in
`style.css`. **All twenty-one pass AA for normal text.** The lowest live pair is 7.15:1.

| Pair | fg | bg | ratio | source |
|---|---|---|---|---|
| body `p` / `--muted` | `#c6c6c6` | `#050505` | **11.93** | :160 / :27 |
| `nav a` | `#d8d8d8` | `#050505` | 14.30 | :363 |
| `footer a` | `#bdbdbd` | `#070707` | 10.72 | :1338 |
| `footer p` | `#c6c6c6` | `#070707` | 11.79 | :160 |
| `.gray` | `#bcbcbc` | `#050505` | 10.73 | :1392 |
| `.toc a` | `#bbbbbb` | `#0d0d0d` | 10.12 | :1567 |
| `.docs-sidebar a` | `#c8c8c8` | `#0d0d0d` | 11.62 | :1507 |
| `.breadcrumb` | `#999999` | `#050505` | **7.15** ← lowest live | :1629 |
| `.breadcrumb a` | `#aaaaaa` | `#050505` | 8.77 | :1635 |
| `.faq-answer` | `#bdbdbd` | `#111111` | 10.05 | :1204 |
| `.stat-card p` | `#bdbdbd` | `#101010` | 10.13 | :984 |
| `.hero-card li` | `#d5d5d5` | `#121212` | 12.76 | :597 |
| `code` in `pre` | `#82ffab` | `#0b0b0b` | 15.78 | :1092 / :1076 |
| `th` | `#3cff6e` | `#111111` | 14.14 | :1048 |
| `--primary` on body | `#3cff6e` | `#050505` | 15.26 | :58 |
| `.btn-primary` label | `#000000` | `#3cff6e` | 15.72 | :504 |
| `.btn-secondary` label | `#ffffff` | `#050505` | 20.38 | :536 |
| `.badge` | `#3cff6e` | `#09190d` (composited) | 13.59 | :473 |

`--gray:#888888` (style.css:68) computes to 5.75:1 — still a pass, and it is **declared but never
referenced** anywhere in the CSS.

I report this because a critic who needs the palette to be guilty will not find it here. Whoever
chose these grays chose well. The exclusion in this artifact is not in the color values.

### 2b. Where color is the *only* signal — and carries no luminance at all

The accent green and the primary text gray are **isoluminant**:

```
L(#3cff6e) = 0.7361      L(#d8d8d8) = 0.6867      ratio = 1.072
WCAG contrast between them = 1.07 : 1
```

The green is the same *brightness* as the gray it replaces. Every place the design uses green to
signal **state** or **emphasis** over gray text, the change is pure hue with a luminance signal of
essentially zero. Viénot (1999) simulation:

| vision | rest `#d8d8d8` | hover `#3cff6e` | contrast |
|---|---|---|---|
| normal | `#d8d8d8` | `#3cff6e` | 1.07:1 |
| protanopia | `#00d8d8` | `#00f26f` | 1.18:1 |
| deuteranopia | `#d8d8d8` | `#ecd97a` | **1.00:1** |
| tritanopia | `#d8d8d8` | `#65f572` | 1.01:1 |

Footer links (`#bdbdbd` → `#3cff6e`, style.css:1338 → :1345) measure 1.41:1 normal, 1.32:1 deutan.

I will be exact about how far this goes. Most of these hovers carry a **non-color** cue as well, and
I will not inflate the finding past that:

- `nav a:hover` (:371) changes color **and** grows a 2px underline via `nav a::after` (:377–401) — a real second cue.
- `footer a:hover` (:1344) changes color **and** shifts `padding-left:8px`.
- `.feature-card:hover` / `.arch-card:hover` (:770, :918) translate and glow.
- `.btn-secondary:hover` (:542) changes background and border.

**One selector has no second cue and is live on three pages:** `.toc a:hover` (style.css:1573–1577)
sets `color` and nothing else. `.toc` is present in `autheo.html`, `blockchain-basics.html`, and
`layer0.html`. There, the hover state is carried entirely by a hue shift that measures 1.00:1 in
luminance. That is a WCAG 1.4.1 (Use of Color) failure, localized and real.

### 2c. The navigation is 71% nonexistent

| measure | count |
|---|---|
| unique internal links, all pages | 14 |
| resolving | 4 |
| dead | **10 (71.4%)** |
| `index.html` nav items (lines 42–64) | 12 |
| resolving | 4 (`index`, `blockchain-basics`, `autheo`, `layer0`) |
| dead | **8 (66.7%)** — `layer1`, `cosmos-sdk`, `evm`, `ibc`, `validators`, `did`, `pqcnet`, `ai-agents` |
| `index.html` feature cards (lines 154–272) | 10 |
| resolving | 3 |
| dead | **7 (70%)** |
| `<a>` elements in `index.html` | 28 |

Dead files confirmed absent from the directory: `layer1.html`, `cosmos-sdk.html`, `evm.html`,
`ibc.html`, `validators.html`, `did.html`, `ai-agents.html`, `pqcnet.html`, `faq.html`,
`glossary.html`.

Two footer links are `href="#"` (index.html:298 GitHub, :299 Documentation) — affordances that
promise a destination and deliver a scroll to top.

### 2d. Focus: one rule in 2,527 lines

```
grep -n ':focus'  css/style.css  →  1276:.search-box input:focus{
grep -n 'outline' css/style.css  →  1272:    outline:none;
```

One `:focus` rule exists in the entire stylesheet, and it is the rule that **removes** the native
focus ring from the search input (`:1272`), replacing it with a 1px border-color change (`:1276`).
`.toc`, `.docs-sidebar`, `nav a`, `.feature-card`, `footer a`, `.btn-primary`, `.btn-secondary`,
`.tab-button`, `.accordion-header`, `.faq-question` — none has any focus indicator.

`index.html` contains 28 anchors. A person who navigates by keyboard, switch, sip-and-puff, or
voice cannot see which one is selected.

Compounding it: `.feature-card { overflow:hidden }` (style.css:735) will **clip** an outline if one
is added naively later. The fix has to account for that.

### 2e. Motion: no opt-out exists

```
grep -c 'prefers-reduced-motion' css/style.css  →  0
```

Four infinite animations, none gated:

| animation | source | period | used? |
|---|---|---|---|
| `.grid-background` → `gridMove` | :2279, :2283 | 30s linear infinite | **yes**, every page |
| `.float` → `float` | :2215, :2219 | 6s infinite | not in HTML |
| `.pulse` → `pulseGlow` | :2247, :2251 | 2.5s infinite | **yes** — `autheo.html:175`, `blockchain-basics.html:133`, `layer0.html:137` |
| `.loading::before` → `loading` | :2465, :2469 | 2s infinite | not in HTML |

Plus `html { scroll-behavior:smooth }` (:22), which forces animated motion on **every** in-page
anchor jump, including the "Explore Architecture" button (index.html:100).

A `.grid-background` drifting behind all content at 30s linear infinite, and a hero card pulsing
glow at 2.5s, are exactly the class of continuous, non-optional motion that a person with a
vestibular disorder, or migraine, or simply a tired afternoon, needs to be able to switch off. There
is no switch.

### 2f. The sticky header occludes its own jump target

- `header { position:sticky; top:0 }` — style.css:283
- `html { scroll-behavior:smooth }` — style.css:22
- `href="#overview"` on "Explore Architecture" — index.html:100
- `grep -c 'scroll-padding\|scroll-margin' css/style.css` → **0**

There is no offset. Clicking "Explore Architecture" smooth-scrolls `<section id="overview">`
(index.html:144) so that its title, `<h2 class="section-title">` (index.html:146), lands **underneath**
the sticky header. The button navigates you to a heading it then hides.

### 2g. Structure and semantics

- `grep -ci '<main\|aria-\|alt=\|skip' index.html` → **0**. No `<main>`, no `aria-label`, no
  `role`, no skip link. All four pages together return 3 hits (one each on the inner pages).
- `<nav>` (index.html:40) is unnamed — no `aria-label`, so it does not distinguish itself as a landmark.
- `<section id="overview">` (index.html:144) has no accessible name, so it is not exposed as a landmark.
- Heading order in `index.html`, measured:

  ```
  36:h2  Understanding Autheo     (the logo)
  80:h1  Understanding Modern Blockchain Infrastructure
 116:h3  Mainnet Features          ← skips h2
 146:h2  Explore the Platform
 156-264:h3 ×10
 282:h3  Understanding Autheo      (footer)
  ```

  The first heading a screen-reader user reaches is an `<h2>`; the `<h1>` arrives second; the third
  heading skips a level. Heading navigation is scrambled at the top of the document.

- The badge at index.html:76 opens with a literal `●` (U+25CF) in markup, not a styled pseudo-element —
  unhidden decorative glyph, announced before the label.

### 2h. Files the page calls that are not there

- `index.html:14` → `css/animations.css` — absent. `css/` holds only `style.css`.
- `index.html:15` → `css/responsive.css` — absent. (The responsive work that *does* exist is
  inlined in `style.css`, lines 1936–2149.)
- `index.html:306` → `js/app.js` — no `js/` directory exists.

I checked whether this strands content invisible: `.fade-up` sets `opacity:0` (style.css:2157) and
depends on JS to add `.visible`. **No HTML file uses `fade-up`, `fade-left`, or `fade-right`** —
so nothing is permanently invisible. That is the one thing the missing JS does not break. It does
mean `.reading-progress` (:1649, `width:0`) can never advance.

- `index.html:19` loads Inter from `fonts.googleapis.com`. Fallback is bare `sans-serif`
  (style.css:31), so a blocked, filtered, metered, or offline connection degrades the typography.

---

## 3. Artist questions

Questions for whoever made this, asked before I give my opinion, because the answer could change it.

1. Is the twelve-topic nav a **map of a curriculum you intend to write**, or a menu of pages you
   believed already existed? The difference matters: the first is a roadmap drawn in the wrong
   medium, the second is a broken product.
2. You wrote responsive breakpoints into `style.css` (lines 1936–2149) *and* linked
   `css/responsive.css`. Which did you think was doing the work?
3. `js/app.js` is linked but absent. What was it meant to do — the fade-in reveals, the reading
   progress bar, both, something else? Knowing the intent tells me whether to rebuild it or delete
   the reference.
4. `backdrop-filter:blur(16px)` on the header (style.css:299) and the moving `.grid-background` are
   the two most expensive things to render here. Were they chosen for legibility, or for
   atmosphere? If atmosphere, they are the cheap things to trade away.
5. The green `#3cff6e` does a lot of work — logo, badge, button, rules, hovers, table headers,
   timeline. Is there a reason it must carry all of it, or did it simply become the default?

---

## 4. Neutral questions

Factual questions about the work itself, answerable from the files.

1. Of the 28 anchors in `index.html`, how many can be reached and activated without a pointing
   device? (Measured: none has a focus indicator.)
2. When `#overview` is the scroll target, what is the vertical distance between the header's bottom
   edge and the `<h2>`'s top edge — and is it positive or negative? (Measured: no offset declared,
   so the heading sits under the header.)
3. Is `--gray` (style.css:68) referenced by any rule? (Measured: no. It is dead code.)
4. Do the ten missing pages exist anywhere — another branch, another directory, a CMS? Or is the gap
   total?
5. Which of the four infinite animations are actually reachable by a real visitor?
   (Measured: `gridMove` on all pages, `pulseGlow` on three.)
6. Does any page carry a `<main>` element? (Measured: no, on any of the four.)

---

## 5. Opinions

*Last, as they should be.*

**The literary anchor I argue from.** Holmes's example in *Mismatch* of the typewriter — built, she
recounts, so that a blind countess could write letters someone else could read — carries her
counter-intuitive instruction: **design for one, extend to many.** The dominant habit is the
reverse — design for the middle, then accommodate outward — and Holmes's point is that the
accommodations bolted on at the edge are always weaker than the thing built for one person at the
margin and then widened. The blind countess did not get a typewriter adapted for her. The typewriter
is what writing became.

**Opinion one: the palette is innocent, and saying so is the point.** Every contrast pair passes,
comfortably. If exclusion required bad contrast, this artifact would be inclusive. It is not. That
is Holmes's premise stated in numbers: exclusion is not sitting inside the color values waiting to
be found. It is produced in the *relationship*. I measured the palette first precisely so the
finding that follows is not mistaken for a contrast complaint.

**Opinion two: the deepest mismatch here is between what the page promises and what the directory
contains.** This is not a styling defect; it is the design's central claim being false. Twelve
topics offered, four delivered, and the page's own line 88 names "curious learners" as its audience.
Consider who a 404 actually breaks. A developer who hits `layer1.html` and gets a 404 can guess that
the page is unwritten and move on; they have a model of how sites are built. A curious learner with
no mental model of blockchain — the person the page says it exists for — has no basis to tell a
missing page from a topic that does not exist. They conclude they have reached the end of what there
is to know, or that they navigated wrongly, and they leave. **The design's failure is severest
exactly where its stated ambition is highest.** That is the mismatch, and it is not fixable by
tuning a color.

**Opinion three: the site is built on the assumption of a hovering pointer.** One focus rule in
2,527 lines, and that rule deletes a focus ring. Twenty-eight anchors on the home page, and a
keyboard user cannot see any of them. Every hover state in the file is `:hover`-only. The design was
made for a hand on a mouse; for a hand on a switch, or a keyboard, or a voice command, the same file
withholds the one piece of information — *where am I* — that makes navigation possible. Nothing
about that user is deficient. The relationship is.

**Opinion four: the motion has no off switch, and the pulsing hero card is the one that stings.**
`prefers-reduced-motion` appears zero times. `gridMove` runs forever behind every page; `pulseGlow`
runs on the hero card of three. I am not going to argue that a drifting grid is harmful in the
abstract — it is atmosphere, and atmosphere is legitimate. I am arguing that atmosphere a person
cannot decline is no longer atmosphere; it is a condition of entry. Holmes's test is not "does this
bother most people" but "who does this relationship exclude, and could one change let them in."
Here one media query lets them in, and it is not there.

**Opinion five: the smallest honest fix is also the largest.** Making the eleven `.toc` hover states
non-color-only is a two-line change. Making the nav truthful is a content decision. I judge the
content decision the more important, because 71% dead affordances is not a bug at the margin — it is
the product's core promise failing for every person, sighted or not, mouse or keyboard. Holmes
designs for one and extends to many; here the one I would design for is the curious learner at
`index.html:88`, standing in front of a ten-card grid where seven cards are doors into a wall.

**What I am not claiming.** Not that the site is inaccessible by WCAG audit alone — the contrast
passes, and I will not pretend otherwise. Not that the missing pages are a moral failing; unwritten
content is a schedule, not a sin. Not that the green is wrong; it is beautiful and it measures fine.
What I claim is narrower and, I think, harder to dismiss: **the artifact declares a relationship with
a beginner that its own files do not honor, and the beginner is the one who pays.**

---

## Verdict

**OBJECT**

The palette passes — 21 of 21 measured pairs clear AA, lowest live pair 7.15:1 — so this is not a
contrast objection. It is an objection to a design whose primary affordance is a map to territory
that does not exist (10 of 14 internal links dead; 8 of 12 nav items and 7 of 10 feature cards on
`index.html` resolve to nothing), which withholds the focus indicator from all 28 of its anchors
(one `:focus` rule in 2,527 lines, and it sets `outline:none`), offers no opt-out from four infinite
animations (`prefers-reduced-motion` count: 0), and scrolls its own jump target underneath its own
sticky header (`scroll-padding-top` / `scroll-margin-top` count: 0).

**One requested change:**

> In `index.html`, make the navigation truthful. Reduce the `<nav>` (lines 42–64) and the
> `.card-grid` (lines 154–272) to the four pages that exist — `index.html`,
> `blockchain-basics.html`, `autheo.html`, `layer0.html` — and render the remaining eight topics as
> non-link items (`<span class="coming-soon">`, not `<a href>`), with the two `href="#"` footer
> links (lines 298–299) either pointed at real destinations or removed. Every affordance the page
> shows must lead somewhere, or must not look like a door.

Secondary, logged as open items rather than gates (they do not block delivery): add
`:focus-visible` for every interactive element, accounting for `.feature-card { overflow:hidden }`
at style.css:735 which will clip an outline; add a `@media (prefers-reduced-motion: reduce)` block
covering `gridMove`, `pulseGlow`, `float`, `loading`, and `scroll-behavior`; add
`scroll-padding-top` to `html`; fix the heading order so `index.html:36` is not an `<h2>` preceding
the `<h1>`; give `<nav>` an `aria-label` and add a `<main>`.

---

## Andon

**Yes — I pull the Andon.**

Bounded, per the standing rule that a gate never blocks delivery: the line stops only until the
navigation is truthful (every visible affordance resolves) and until every interactive element has a
visible focus indicator. Two changes. Once those land, the line restarts and the remaining items run
as open items against a moving line — measured, logged, not blocking.

I pull it because a site that teaches beginners by offering them twelve doors, eight of which are
walls, is not a site with accessibility defects to be triaged later. It is the product's core promise
misfiring, and it misfires hardest on the person it names for itself. That is Holmes's mismatch in
its plainest form, and it is worth stopping for.
