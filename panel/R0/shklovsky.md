# R0 Premortem — Shklovsky Seat

**Panel:** DADA, Adaptive mode · Round R0 (premortem)
**Artifact:** `H:\blockchain-explain`, judged exactly as inherited, before any redesign move
**Authority:** one only — Viktor Shklovsky, *"Art as Technique"* (1917): ostranenie (making strange) against automatization
**Files read:** `H:\blockchain-explain\index.html` (311 lines, in full) · `H:\blockchain-explain\css\style.css` (2527 lines, 32 KB, in full)

---

## The one literary anchor

Tolstoy's note on the sofa. A man cleaning a room dusts the sofa and, coming round a second time, cannot remember whether he has dusted it. Shklovsky: *"Habitualization devours works, clothes, furniture, one's wife, and the fear of war… if the whole complex lives of many people go on unconsciously, then such lives are as if they had never been."*

The sofa **was** dusted. The dusting **did not happen**. That is the defect I am hunting: work performed that leaves no trace in consciousness. Everything below is measured against that single sentence and nothing else.

---

## 1. Statements of meaning

(Description only. No evaluation yet.)

**The sheet is enormous; the page uses almost none of it.**
- `css/style.css` contains **243 rule blocks** and defines **104 class selectors**.
- `index.html` uses **18** of them: `badge, btn-primary, btn-secondary, card-grid, feature-card, glow, glow1, glow2, grid-background, hero, hero-buttons, hero-card, hero-left, hero-right, logo, logo-circle, section-title, status`.
- **86 defined classes are never instantiated** anywhere in `index.html` — including `.doc-panel`, `.info-box`, `.warning-box`, `.danger-box`, `.timeline`, `.stats`, `.flow`, `.tabs`, `.accordion`, `.text-gradient`, and the 16 `.w-100/.flex/.grid/.center/…` utilities at lines 2509–2524.

**The palette is one hue and a band of indistinguishable blacks.**
- `--primary:#3CFF6E` at `style.css:58`.
- **44 occurrences** of `rgba(60,255,110,α)` at **11 distinct alpha values**: `.10`×14, `.15`×8, `.08`×7, `.25`×3, `.18`×3, `.12`×3, `.05`×2, then one each of `.50`, `.45`, `.35`, `.30`.
- **30 distinct six-digit hex values. 11 have relative luminance below 0.12. Nine of those are neutral grey** (max channel − min channel ≤ 6): `#050505, #070707, #080808, #090909, #0b0b0b, #0d0d0d, #0e0e0e, #101010, #121212`. Their luminance spans **0.0196 → 0.0781** — a 0.059 range spread across nine named tokens.

**The atmosphere is painted, not built.**
- `index.html:25,27,28` — three empty `<div>`s: `.grid-background`, `.glow.glow1`, `.glow.glow2`.
- `style.css:200–216` — the grid: two `linear-gradient`s of `rgba(60,255,110,.05)` at `background-size:60px 60px`, `z-index:-20`, plus a `::after` radial vignette to `#050505`.
- `style.css:238–274` — the glows: 600×600 px circles, `filter:blur(140px)`, `opacity:.12`, `z-index:-10`, one `#00ff66` top-left, one `#2dff83` bottom-right.
- `style.css:2277–2297` — `@keyframes gridMove`, `animation:gridMove 30s linear infinite`, drifting the grid by exactly one 60 px tile.
- `style.css:103–115` — the scrollbar thumb is painted solid `#3cff6e` with `border-radius:50px`.
- Three `filter:blur(` declarations in total; **14** `box-shadow` declarations; **19** `:hover` rules; **7** repetitions of the literal `transition` duration `.35s`.

**There is no image and no drawing on the page.**
- `index.html` contains **0 `<img>` tags and 0 `<svg>` tags.** Every visual event on the landing page is a rectangle, a border, a text-glyph, or a blurred circle.

**The page is a set of doors, most of which do not open.**
- 12 `<a>` elements in `<nav>` (`index.html:42–64`); 10 `.feature-card` anchors (`index.html:152–274`).
- 10 of the 14 unique internal targets do not exist: `layer1, cosmos-sdk, evm, ibc, validators, did, pqcnet, ai-agents, faq, glossary`.
- `index.html:298–301` — `GitHub` and `Documentation` are `href="#"`.
- `index.html:14–15` link `css/animations.css` and `css/responsive.css`; `css/` contains only `style.css`. `index.html:306` loads `js/app.js`; there is no `js/` directory.
- `index.html:76` — the badge reads `● MAINNET EDUCATION PLATFORM`, the bullet being a literal U+25CF text glyph, not a drawn mark.

**Type.** `style.css:122–132` — `h1` at `4.4rem`, `font-weight:900`, `line-height:1.05`, `letter-spacing:-2px`. Body `line-height:1.7` (`style.css:35`); `p` colour `var(--muted) #c6c6c6` (`style.css:158–164`).

---

## 2. Artist questions

1. Which of the nine near-black tokens is doing work that another is not — and if none is, why are there nine?
2. You declared `--primary` once (`style.css:58`) and then wrote its RGB triple by hand 44 times at 11 opacities. Where did you intend the green to *mean* something, and where did you intend it merely to be? Can you point to the line where the difference is decided?
3. You wrote 86 classes for pages that are not here, and 10 nav links to pages that are not here. Was the sheet written first and the site promised afterwards?
4. Where on this page is the reader asked to slow down? Name the element. If the answer is "nowhere, the reader should move fast," say so plainly, because that is a different design.
5. `blockchain-basics.html` has 1793 words and `index.html` has 229. Did you consider that the landing page's job might be to be *difficult*, and chose instead that it be empty?
6. What was the sofa here — the thing you dusted and could not remember dusting?

---

## 3. Neutral questions

1. Is `css/animations.css` meant to exist in a later round, or is it a leftover from a template? `style.css:2155–2477` already contains `.fade-up`, `.fade-left`, `.fade-right`, `.float`, `.pulse`, `gridMove`, a button ripple and a loading shimmer — so what would `animations.css` add?
2. Does `js/app.js` have a defined purpose? The only candidates in the sheet that need script are `.reading-progress` (`style.css:1649`, `width:0`), `.tab-button.active`, `.accordion-header`, `.faq-question` and `.fade-up.visible`. None of those classes appears in `index.html`.
3. Are the ten dead pages planned content or abandoned content? The answer changes whether the nav is a promise or a ruin, and I cannot tell from the files.
4. Is `#3cff6e` a brand constraint inherited from Autheo, or a free choice? If it is a constraint, my objection about the *hue* dissolves and only the *count* stands.
5. Is there any diagram, chart or figure planned for the landing page, or is text-and-cards the intended medium for all 14 pages?
6. Was the Google Fonts request at `index.html:19` (`Inter`, nine weights 300–900) chosen, or inherited?

---

## 4. Opinions

**The inherited visual language is an automatized sign. It does not lengthen perception; it is the generic dark-grid-and-glow crypto site, and it is the sofa dusted twice.**

The evidence is not the mood — mood is taste, and taste is not my authority. The evidence is the count. **Forty-four hand-written instances of one green at eleven opacities.** When a colour appears forty-four times it has stopped being a colour and become a rule; Shklovsky's word for this is *algebrization* — the thing replaced by its own shorthand. The reader's eye stops at the second instance and never arrives at the fortieth. The glows are `opacity:.12` over a `#050505` field with a vignette already fading them to black (`style.css:218–236`); they are, by their own arithmetic, at the threshold of not being there. That is not atmosphere — it is atmosphere *algebrized*, the sign of depth painted where depth would have to be built.

The nine neutral greys are the same failure in a quieter key. `#050505` at luminance 0.0196 and `#121212` at 0.0781 are separated by less than six hundredths of a luminance unit, and they are used as *different* tokens on *different* elements (`--background`, `--panel`, `--background-secondary`, `.feature-card` at `rgba(15,15,15,.92)`, `.hero-card` at `rgba(18,18,18,.9)`). No eye holds that difference. The variety is legible in the source and nowhere else. It is work performed that leaves no trace — the sofa.

Shklovsky's own test is the stone: the device exists so that the stone becomes *stony*, so that the act of seeing is prolonged into an end in itself. Ask what on this page forces the eye to labour. Nothing. There are **zero images and zero SVGs**; every mark is a rectangle with a 1 px green border and a `translateY(-8px)` hover (`style.css:770–780`, one of 19 hover rules, seven of which share the identical `.35s` duration). The sweep on `.feature-card::before` (`style.css:741–768`) is a 4 px bar crossing in 0.7 s; the ripple (`2312–2338`) is a white sheen at 0.15 alpha crossing in 1 s. Both are motion applied *to* a surface, not motion *of* a meaning. They are the briskness of a site that has been here before. The reader has seen this page on thirty other chains and will not remember this one.

And then the automatization turns into something worse than invisibility. **The chrome is finished and the content is absent.** 243 rule blocks, a print stylesheet, a scrollbar styled in brand green, a shimmer for loading states — against 4 resolvable links out of 14, two missing stylesheets, and no `js/` directory. The finish of the surface is precisely what makes the emptiness unnoticeable. A reader meets twelve nav items, ten cards, a badge announcing `MAINNET EDUCATION PLATFORM`, and a hero card listing eight features; the *form* of an encyclopedia is fully present while the encyclopedia is not. This is habitualization devouring a work in real time: the sign of a documentation site has been built so competently that nobody checks whether there is a documentation site. Ten of the fourteen doors open onto nothing, and the green glow is what stops the reader from trying the handle.

This is why I object at R0 rather than waiting. If the panel now *adds* pages to this sheet — writes `layer1.html`, `evm.html`, `ibc.html` in the inherited language — the ten dead links become ten live pages, the automatization is ratified, and the site will be larger and no more seen. Premortem exists to name that before it happens. The page must be made strange *first*, or it will be finished while remaining invisible.

One thing I will not object to: the type. `h1` at 4.4rem/900/−2px (`style.css:122–132`) is loud, but loudness is not automatization, and `line-height:1.7` on body at `#c6c6c6` is a readable setting. The hero copy at `index.html:88` is 51 words listing eight abstractions with no image between them — but that is a writing problem, and it belongs to whoever writes `blockchain-basics.html`, not to my seat.

---

## Verdict

**OBJECT.**

**Requested change (one):** Delete the three atmospheric layers from the inherited sheet — `.grid-background` and its `::after` vignette (`css/style.css:200–236`), `.glow`, `.glow1`, `.glow2` (`css/style.css:238–274`) — along with `@keyframes gridMove` and the `animation:gridMove 30s linear infinite` declaration (`css/style.css:2277–2297`), and remove the three corresponding empty `<div>`s from `index.html:25,27,28`.

**Exit test:** `grep -c 'gridMove' css/style.css` returns `0`; `grep -c 'filter:blur(' css/style.css` returns `0`; `index.html` contains no element with class `grid-background`, `glow`, `glow1` or `glow2`.

**Why this one.** It is the smallest cut that removes an algebrized sign from the surface without touching structure, and it is the only cut that cannot be undone by adding pages later. Once the drift-grid and the two blurred circles are gone, whatever the redesign puts in their place has to be *about* Autheo rather than about crypto sites — and if the redesign can find nothing to put there, the empty page will say so honestly, which is more than the glow says now.

**Not requested (open items, logged, not gates):** collapsing the 44 green instances to two alpha levels; collapsing the nine neutral greys to three; resolving the ten dead links; creating or dropping `css/animations.css`, `css/responsive.css` and `js/app.js`; choosing whether `Inter` is inherited or chosen. I flag these and continue.

---

## Andon

**Yes — pulled**, on one defect and with a release condition stated in the same breath, because a cord without a release condition is a stall and I do not hold the panel.

**Defect:** the artifact as inherited cannot be read as a site. 10 of 14 unique internal targets do not exist; `css/animations.css` and `css/responsive.css` are linked and missing; `js/app.js` is loaded and there is no `js/` directory.

**Release condition:** the single requested change above is applied and its exit test passes. At that point I release the cord and the panel proceeds. The dead-link inventory and the missing stylesheets do **not** gate the panel — they are logged as open items and belong to the work queue, not to my verdict.

---

*Shklovsky, "Art as Technique": habitualization devours works… as if they had never been. This artifact has been dusted twice. The dusting does not count.*
