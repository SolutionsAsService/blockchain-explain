# DADA Panel — Seat: Guy Debord, *The Society of the Spectacle*
**Round:** R0 — premortem (artifact judged exactly as inherited, before any redesign move)
**Artifact:** `H:\blockchain-explain` (static site: teaches blockchain, promotes Autheo)
**Mode:** Adaptive
**Date:** 2026-10-27

---

## 0. Literary anchor (one)

> **"The spectacle, grasped in its totality, is both the result and the project of the existing mode of production. It is not a supplement to the real world, an additional decoration. It is the heartbeat of the unrealism of real society."**
> — Guy Debord, *The Society of the Spectacle*, Thesis 6

I judge this artifact against Thesis 6 and nothing else. Thesis 6 is chosen because it refuses the defence I expect to hear — "these are only cosmetic problems, the content is fine." Debord's sentence forecloses that defence in advance: the decoration is not supplementary. And it names the second thing precisely: *unrealism*. This site is not merely thin. It is **unreal** — it declares resources that do not exist, documents that do not close, and a network whose status it cannot evidence.

---

## 1. Statements of meaning — what the work seems to say

Read naively, as a visitor would read it:

- **It says: a live network exists.** `index.html:76` opens with the badge `● MAINNET EDUCATION PLATFORM`. `autheo.html:111` opens with `● AUTHEO MAINNET ARCHITECTURE`. `autheo.html:467` labels a panel `LIVE NETWORK FEATURES`. `autheo.html:475` calls it `A Production Blockchain Environment`. The claim is made four times before any substance is offered.
- **It says: the system is legible and layered.** `autheo.html:290–433` draws a five-tier stack — Web Applications → AI Agents → EVM Layer 1 → CometBFT → Cosmos SDK Layer 0 — joined by four `↓` arrows. There are 19 `↓` glyphs in this one file. The page's governing gesture is *the arrow*: it proposes that everything flows downward into a foundation, and that the foundation is Autheo.
- **It says: it is capacious and measurable.** `autheo.html:999` `399` slots available; `:1019` `275` subscribed; `:1040` `124` remaining. The arithmetic is correct (399 − 275 = 124). It is presented in three large-type `stat-card`s.
- **It says: it is wide.** `index.html:42–64` offers twelve navigation destinations. `index.html:154–272` offers eleven feature cards. The front page is a map of a territory.
- **It says: it is modern and in motion.** `index.html:13–15` loads three stylesheets, two named `animations.css` and `responsive.css`. `index.html:306` loads `js/app.js`. `autheo.html:175` puts `pulse` on the hero card. The site declares animation, responsiveness, and behaviour.
- **It says: it is open and verifiable.** `index.html:298–299` links to `GitHub` and `Documentation`.

Taken together, the page's single meaning is: **this is a finished, live, measurable, documented, open system.** That is the proposition. Everything below tests it.

---

## 2. Artist questions (put to the maker, not answered by me)

1. When you wrote `<div class="status"></div>` at `index.html:114` — an empty element that `css/style.css` renders as a 14px `#3cff6e` circle with a glow — did you intend it to indicate a state, or to indicate *the idea* of a state? Is the dot a measurement, or a costume?
2. `autheo.html` ends at line 1761 with `</section>` and whitespace. There is no `</main>` for the `<main>` opened at line 97, no `</body>`, no `</html>`, no footer, no return path. Did you stop writing, or did you believe you had finished?
3. You gave `index.html:298–299` the labels `GitHub` and `Documentation` and pointed both at `href="#"`. What were you asking the reader to believe those words meant?
4. The "Mainnet Features" list at `index.html:118–135` and the "Autheo Network" list at `autheo.html:189–220` are near-identical eight-token sets. In a 796-word page, "Autheo" appears 23 times and "AI" 17 times. Is the repetition pedagogy, or incantation?
5. `autheo.html:1067` says remaining validator capacity "is reserved according to network participation requirements and enterprise partnerships" — directly beneath a card that calls 124 slots `Remaining Capacity`. Is that number available to the reader, or is it already spoken for? Who is the stat-card for?
6. Why does the site that most wants to be believed — `autheo.html`, the product page — carry the unfinished document?

---

## 3. Neutral questions (from me as critic — factual, answerable, not yet opinion)

1. Of the 14 unique internal link targets on `index.html`, how many resolve? *(Measured: 4. Dead: layer1, cosmos-sdk, evm, ibc, validators, did, pqcnet, ai-agents, faq, glossary — 71% of the promised territory is absent.)*
2. Do `css/animations.css` and `css/responsive.css` exist? *(Measured: `css/` contains one file, `style.css`, 32,202 bytes. Both named sheets are absent, and are referenced by all four pages.)*
3. Does `js/app.js` exist? *(Measured: there is no `js/` directory. `index.html:306` and `blockchain-basics.html` still request it.)*
4. Are the class names used in the HTML actually styled? *(Measured: 61 distinct classes used; **12 have no rule anywhere in `css/style.css`** — `architecture-stack`, `stack-layer`, `stack-arrow`, `highlight`, `application`, `network-map`, `network-node`, `connected`, `center-node`, `block-visual`, `block-header`, `block-row`. These are exactly the diagram classes, and exactly the classes the two missing stylesheets were meant to carry.)*
5. Do the two long documents close? *(Measured: `autheo.html` 119 structural tags opened / 116 closed, last line 1761, no `</html>`. `layer0.html` 108 / 105, no `</html>`. `index.html` 21/21 and `blockchain-basics.html` 259/259 both close.)*
6. What fraction of the four existing pages clears 800 words? *(Measured: one of four. `index.html` 229 visible words, `layer0.html` 706, `autheo.html` 796, `blockchain-basics.html` 1793.)*

**The decisive neutral finding:** the element the author marks for attention is the element with no definition. `.highlight` is undefined in `css/style.css`. It is applied at `autheo.html:352` (EVM Layer 1), `:412` (Cosmos SDK Layer 0), `:1674` (Autheo Identity & Coordination Layer) and `:1714` (AI Agents) — the four things the page most wants seen. As shipped, **the highlight is invisible.** The emphatic gesture is performed and has no effect. The stack it sits in (`architecture-stack`, `stack-layer`, `stack-arrow`) is likewise undefined, so `autheo.html:290–433` — the centrepiece diagram, "How Autheo Is Built" — renders as bare text with `↓` characters.

---

## 4. Opinions (last, and mine alone)

**The decoration is not a supplement; it is the whole.** Debord's Thesis 6 says the spectacle "is not a supplement to the real world, an additional decoration." This site is the proof of the negative case: strip the decoration and there is almost nothing left. `index.html` is 229 visible words — a lobby. Its first three body elements are `<div class="grid-background">`, `<div class="glow glow1">`, `<div class="glow glow2">` (lines 25–28): three empty divs whose entire function is ambience. Five empty `<div>`s in `index.html`, five in `autheo.html`, eight in `layer0.html`. The page is propped up by containers that contain nothing. Debord is right that the ornament is not additional — here the ornament *is* the content, and when the ornament's own stylesheet is missing, the content disappears with it.

**The motion is non-living.** The site declares autonomous movement — `animations.css`, `responsive.css`, `js/app.js`, `.pulse` — and not one of those declarations resolves. `js/` does not exist as a directory. This is a site that advertises animation and cannot animate; that loads a script that was never written. The declared dynamism is a property of the *markup*, not of the page. What moves is the promise; the artefact is still.

**The sign has separated from the state it names.** `index.html:114` is a green dot with a glow, styled to mean *operational*, wrapped in a badge reading `MAINNET EDUCATION PLATFORM`. It is attached to nothing: no block height, no uptime, no as-of date, no source. Likewise `399 / 275 / 124` (`autheo.html:999, 1019, 1040`) — internally consistent, externally unsourced and undated, and then quietly disavowed eleven lines later at `:1067` by "reserved according to … enterprise partnerships." The number is not false. It is worse than false: it is *unattached*. It is a measurement with no measured thing. Debord's spectacle is precisely this — the representation continuing to circulate once its referent has been withdrawn.

**The exits are sealed.** `index.html:298–299` — `GitHub`, `Documentation` — both `href="#"`. Of all the links on the front page, the only two that would lead *out* of the closed system lead back to the top of the same page. The two words that promise an external, checkable record are the two links that cannot leave. A system that offers twelve internal destinations and zero external ones, where ten of the twelve internal ones do not exist, is a closed loop: the reader's only possible movement is within a representation that has no outside.

**And the ground is unreal.** `autheo.html` — the product page, the one that sells — does not close. 119 tags opened, 116 closed, ending mid-air at line 1761 with no `</main>`, `</body>`, `</html>`, no footer, no way back. `layer0.html` is the same (108/105). Debord's phrase for this condition is exact and I can improve on it: this is *the heartbeat of the unrealism of real society*, and here the unrealism is literal. The browser does not render what the author wrote; it renders an error-corrected guess. So every judgment the panel makes about `autheo.html`'s visual result — including mine — is a judgment about a document that does not exist as authored. **That is why this is a premortem and not a review: there is, as yet, no stable object to review.**

I do not object because the site is promotional. I object because it is **unreal in a way that is measurable**, and because that unreality is not incidental but structural: phantom stylesheets, phantom script, twelve undefined classes, ten dead links, two unclosed documents, a status light with no status, and two exits that lead nowhere.

---

## Evidence index (every line below was measured on this artifact today)

| # | Observable | Location | Value |
|---|---|---|---|
| 1 | Internal link targets that resolve | `index.html` | 4 of 14 (10 dead: layer1, cosmos-sdk, evm, ibc, validators, did, pqcnet, ai-agents, faq, glossary) |
| 2 | `css/animations.css`, `css/responsive.css` | `index.html:14–15`, `autheo.html:21–22`, all 4 pages | absent; `css/` holds only `style.css` (32,202 B) |
| 3 | `js/app.js` | `index.html:306` | no `js/` directory exists |
| 4 | Classes used but undefined in `css/style.css` | across 4 pages | 12 of 61 — incl. `architecture-stack`, `stack-layer`, `stack-arrow`, `highlight`, `block-visual`, `network-map`, `center-node` |
| 5 | `.highlight` applications | `autheo.html:352, 412, 1674, 1714` | 4; rule defined in `style.css`: **false** |
| 6 | Tag balance | `autheo.html` | 119 open / 116 closed; ends line 1761, no `</html>` |
| 7 | Tag balance | `layer0.html` | 108 / 105; no `</html>` |
| 8 | Tag balance | `index.html` / `blockchain-basics.html` | 21/21 and 259/259 — both close |
| 9 | Empty `<div>`s | index 5, autheo 5, layer0 8, basics 6 | 24 |
| 10 | `<div class="status"></div>` (empty) | `index.html:114` | styled in `style.css` as 14px `#3cff6e` circle + glow |
| 11 | `href="#"` on `GitHub` / `Documentation` | `index.html:298–299` | 2 |
| 12 | Visible word counts | 4 pages | index 229, autheo 796, layer0 706, basics 1793 — 3 of 4 under 800 |
| 13 | Term frequency, `autheo.html` (796 words) | — | Autheo ×23, AI ×17, Layer ×13, identity/Identity ×15, EVM ×8 |
| 14 | `↓` glyphs | `autheo.html` | 19 |
| 15 | Validator stats | `autheo.html:999 / 1019 / 1040` | 399 / 275 / 124 — arithmetic holds; no source, no date; disavowed at `:1067` |
| 16 | Webfont | `index.html:19` | `fonts.googleapis.com`, 9 weights (300–900) of Inter |

---

## Verdict

**OBJECT.**

## Andon: **No.**

I do not pull the Andon, for three reasons, in order of weight:

1. **There is no unknown here.** Every defect I name is enumerated, located by file and line, and measured. Andon is for the unmapped and the unknowable; this is a bill of quantities.
2. **The fixes do not require a design decision.** They require a deletion, a closing tag, and a stylesheet block. Nothing about them is contested, and nothing about them needs the panel's ambition.
3. **A premortem that freezes before move one defeats its own purpose.** My operating rule is explicit: a gate, an unmapped fact or a styling disagreement never blocks delivery — it is logged and work continues. And the panel's own stopping rule applies: once critics begin to repeat one another, ship the strongest variant. This report is written so the panel can *move*, not so it can wait.

## Requested change (one)

**Bring declaration into correspondence with existence: no page may name a resource, a destination, or a document it does not have — and every document must close.**

Concretely, in one pass:

1. Delete `<link rel="stylesheet" href="css/animations.css">` and `<link rel="stylesheet" href="css/responsive.css">` from `index.html:14–15`, `autheo.html:21–22`, `layer0.html`, `blockchain-basics.html` — **or** write those two files. Do not leave the reference standing.
2. Delete `<script src="js/app.js"></script>` from `index.html:306` and `blockchain-basics.html` — **or** create `js/` and the file.
3. Close `autheo.html` (append `</main>`, a footer, `</body>`, `</html>`; resolve the 119/116 imbalance at line 1761) and close `layer0.html` (108/105).
4. Give the 12 orphan classes — at minimum `architecture-stack`, `stack-layer`, `stack-arrow`, and `highlight` — real rules in `css/style.css`, so that `autheo.html:290–433` renders as a stack and the four `.highlight` layers are actually distinguishable.

**Acceptance test (one command, no judgement required):** for each of the four pages, every `href`/`src` in the document resolves to a file that exists in the repo, every `<link>` and `<script>` resolves, the file ends in `</html>`, and the count of opened structural tags equals the count of closed ones. Today, on this artifact, that test fails on all four counts.

Until it passes, the panel is not reviewing a website. It is reviewing a rendering engine's guess about one.

---

## Open items (logged, non-blocking — not the requested change)

- **O1** — `index.html:114` `.status` dot and the `MAINNET`/`LIVE NETWORK` badges (`index.html:76`, `autheo.html:111, 467, 475`) assert liveness with no evidence. Either attach a dated, sourced figure (block height, validator count as-of date) or delete the dot. *This is the deepest Debordian defect on the site; I list it second only because the document must first exist before its signs can be corrected.*
- **O2** — The 10 dead internal links. Either build the 10 pages or remove the 10 promises; a nav that is 71% absent is worse than a nav of four honest items.
- **O3** — `index.html:298–299` `href="#"`. Point `GitHub` at a real repository or drop the label.
- **O4** — `autheo.html:999–1048` stat-cards: add a source and an as-of date, or reduce to prose.
- **O5** — `autheo.html:1067` contradicts the `124 Remaining Capacity` card above it. Resolve the contradiction in text.
- **O6** — `index.html:19` webfont: 9 weights of Inter from `fonts.googleapis.com` for a 229-word page is an external dependency carrying no content of its own; consider a system stack.
- **O7** — Repetition: 23× "Autheo" in 796 words, and two near-identical eight-item feature lists (`index.html:118–135` / `autheo.html:189–220`). Deduplicate into one canonical capability statement.

---

*Seat: Guy Debord, Thesis 6. Round R0, premortem. Verdict OBJECT. Andon: no.*
