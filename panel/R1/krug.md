# R1 — WHOLE artifact — Krug seat (Adaptive mode)

**Authority:** Steve Krug, *Don't Make Me Think*. Self-evident. Obvious. Forgiving.
**Anchor used:** Krug's **Second Law of Usability** — *"It doesn't matter how many times I have to click, as long as each click is a mindless, unambiguous choice."*

---

## What I actually looked at

- Read `index.html` (218 lines) and `css/site.css` (507 lines) in full.
- Ran `node tools/verify.mjs` → `PASS autheo.html / blockchain-basics.html / index.html / layer0.html`, "all pages pass".
- Ran `node tools/contrast.mjs` → 18 pairs, all pass; lowest text pair **4.99:1** (light accent on paper), focus ring 14.69:1 dark / 4.99:1 light.
- Grepped the three inner pages for `stylesheet`, `<main>`, `skip`, `aria-current`, `not-written`, `<script`, and for every `href`.
- Counted visible words in `index.html` with the SVG stripped: **279**.

---

## 1. Statements of meaning

What the artifact is doing, as I read it off the files.

**The home page is doing the job.** `index.html` is 279 visible words. One accent (`--accent: #3cff6e`, `site.css:32`), one type scale (`site.css:13-19`), no `js/`, no `<script>`, no `@import`, no third-party host — the only outbound URL is `index.html:212`. It has a skip link (`:13`), `<main id="main">` (`:39`), `aria-current="page"` on Overview (`:31`), and a real `:focus-visible { outline: 3px solid var(--accent) }` at `site.css:86-89`. The strata SVG (`:67-125`) is drawn in the document, numbered 05 down to 01, with Layer 03 filled by the accent band and a caption that says what it means. The eyebrow says "read from the ground up" (`:43`) and the layer cards below read 01→05. That is coherent, and it is self-evident.

**The three inner pages are a different artifact.** They link `css/style.css` (autheo.html:19, blockchain-basics.html:16, layer0.html:14) — the inherited 33,499-byte sheet, not `site.css`. Each opens with `<div class="grid-background">` and two `<div class="glow glowN">` (autheo.html:27-31, blockchain-basics.html:23-26, layer0.html:21-25) for which `css/style.css` contains **no `.glow` rule** — only `.glow-border` at `style.css:1299`. Dead markup, though harmless.

**The nav is where the artifact stops being obvious.** Item counts, counted from the files:

| page | real links | `<span class="not-written">` | struck share |
|---|---|---|---|
| `index.html:30-35` | 4 | 0 | 0% |
| `autheo.html:50-78` | 4 | 2 (`:72`, `:75`) | 33% |
| `blockchain-basics.html:44-66` | 3 | 7 (`:52-64`) | 70% |
| `layer0.html:44-64` | 3 | 6 (`:52-62`) | 67% |

**The struck items contradict the pages they sit on.** `autheo.html:72,75` strikes "Validators" and "AI Agents"; `autheo.html` contains the headings *Validator Network Security*, *Autheo Validator Consensus Flow*, *AI Agents & Services*, *The AI Agent Coordination Layer*. `layer0.html:52,54` strikes "Layer 1" and "Cosmos SDK"; `layer0.html` contains *Layer 1 Blockchain* and *Cosmos SDK: Building Custom Blockchains*. `index.html`'s own centrepiece is "EVM-compatible Layer 1" (`:98`, `:151`), while "EVM" is struck on two inner navs.

**There is no legend.** Zero occurrences of "not written", "struck", "coming soon", "pending-as-text", or any visible gloss in any page. The meaning of the strikethrough exists only in a CSS comment (`site.css:500`, `style.css:2497`).

**Wayfinding is inconsistent across pages.**
- Order: `index.html` is Overview, Autheo, Blockchain, Layer 0 (`:31-34`). `autheo.html` is Home, Blockchain, Layer 0, Autheo (`:52-67`). Autheo is item 2 on the home page and item 4 on its own page.
- Label: the same destination is "Overview" on `index.html:31` and "Home" on the three inner pages; "Blockchain" in `blockchain-basics.html:48` and "Blockchain Basics" at `:184`.
- **`autheo.html` has zero inbound links from `blockchain-basics.html` and `layer0.html`.** Neither nav lists it, and grep finds no `href="autheo.html"` in either file. The flagship page — the one `index.html:59` makes the primary button — cannot be reached from two of the four pages.
- `aria-current` appears exactly once in the artifact, at `index.html:31`. Three of four pages have no you-are-here marker.
- Skip link appears exactly once, at `index.html:13`. Three of four pages have none; `blockchain-basics.html` runs 3,300+ lines.

**One sentence talks about the plumbing.** `index.html:180-183`: *"Three long-form pages exist today. Each one is linked below; nothing on this site points at a page that does not exist."* The second clause is the author reporting on the site's link hygiene to a reader who came to learn what Autheo is.

---

## 2. Artist questions

- When you struck "Validators" on `autheo.html:72`, did you mean "there is no separate *page* named Validators", or "there is no *content* about validators"? The page you put it on has a validator section. Which of those did you want the reader to understand?
- Why does `blockchain-basics.html:44-66` show the reader seven topics it refuses to open? What did you want the reader to do with "EVM" crossed out — remember it, or stop looking for it?
- Why does `index.html:59` push "Read the architecture" as the primary action when `blockchain-basics.html` and `layer0.html` give the reader no way to reach that page?

---

## 3. Neutral questions

- Is `fill="var(--accent)"` (`index.html:20`) and `stop-color="var(--accent)"` (`index.html:72-73`) resolving in every browser you intend to support? These two attributes are the only source of colour for the brand mark's base bar and for the entire `#band` gradient that marks Layer 03. If `var()` substitution in an SVG presentation attribute fails anywhere, `#band` resolves to black and `.s-name-on { fill: var(--on-accent) }` (`site.css:339-341`, `#04120a`) sits on black — the one layer the caption calls out becomes invisible. I could not render the page in this session, so I am asking, not asserting.
- Should the inner-page navs be identical to `index.html:30-35`? They are currently not, in membership, order and label.
- Is `css/style.css` meant to survive, or is `site.css` the intended single sheet? All three inner pages still load the former.

---

## 4. Opinions

`index.html` passes my authority cleanly. It is self-evident: the graphic, the eyebrow, the caption and the card list all point the same way, and nothing on the page asks the reader to figure out the site before they figure out the stack. That is the redesign working.

The three inner pages do not pass, and the reason is the nav. Striking through a dead link removed the broken affordance and left an ambiguous one in its place. A link that goes nowhere makes the reader think once — "that didn't work." A link drawn with a line through it makes the reader think every time, and think the wrong thing: on `blockchain-basics.html` and `layer0.html`, two out of every three things in the site's primary wayfinding element are crossed out, and several of them are crossed out while the content sits a few hundred lines further down the same page. That is the opposite of a mindless, unambiguous choice. Krug's Second Law permits many clicks; it does not permit a click you have to decode first.

And the repair introduced a hole it did not have before. Before, `autheo.html` was one of ten dead links. Now `autheo.html` is a live page with no inbound link from two of the four pages in the site, because converting the nav entries to struck-through text took them out of circulation rather than pointing them at the page that exists. The fix for a missing door is not to paint the door shut; it is to open the one next to it.

I would also cut `index.html:180-183`'s second clause. The reader does not need to be told the site's links resolve; that is the author talking about the author's problem.

**Andon: no.** Nothing here is broken — every link resolves, nothing misleads a reader into an unrecoverable error, the worst case is a reader who works a little harder than they should, and `index.html` itself is sound. I am not stopping the line over a thinking tax. If the panel overrules me and keeps the struck-through nav items, then the condition for release becomes: a visible one-line legend must sit immediately under each inner-page nav stating what the strikethrough means, and `autheo.html` must gain an inbound link from `blockchain-basics.html` and `layer0.html`.

---

## Requested change (one)

**Rebuild the three inner-page `<nav>` elements (`autheo.html:50-78`, `blockchain-basics.html:44-66`, `layer0.html:44-64`) to the canonical four-item set used at `index.html:30-35` — Overview/Home, Autheo, Blockchain, Layer 0 — with `aria-current="page"` on the item for the page being viewed, and delete the fifteen `<span class="not-written">` items from those navs** (`autheo.html:72,75`; `blockchain-basics.html:52,54,56,58,60,62,64`; `layer0.html:52,54,56,58,60,62`). Every nav item then becomes a door that opens, the four pages stop disagreeing about order and label, `autheo.html` becomes reachable from all four pages, and the reader never has to decode a strikethrough.

Non-blocking, in this order if the round continues:
1. Delete the plumbing clause at `index.html:180-183`.
2. Add the skip link and `<main id="main">` to the three inner pages.
3. Give `index.html:20` and `index.html:72-73` literal hex fallbacks so the Layer 03 band cannot render black.

---

**Verdict: OBJECT**
