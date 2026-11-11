# DESIGN-LOG: blockchain-explain 2.0, a total makeover

DADA run, 2026-11-11. The earlier run's log is `DESIGN-LOG-v1.md`.

## 1. Traversal Plan

**Brief:** "full site redesign, very basic, total makeover". Keep the logo (saved as `brand/logo-v1.svg`) and make a version 2.0. Then add the site to the portfolio and the coding roadmap.

**Mode: Adaptive.** A public teaching site. **Run type: Full** ("full site redesign", "total makeover"). R0 is required because an artifact exists.

**Reading of "very basic":** plain, light and calm. One idea per page, few colours, short pages. Not a bare page: the landing still leads with one bold graphic that summarizes the site.

### Tooling (Step 0)
Agent tool, one seat per reference, at most three at a time, each filing to `panel/`; `pick_panel.py`; Playwright measuring scripts that enumerate every page; a Python build that computes every hash; the dada-changes ledger for the record.

### Seed (labels copied from the graph)
- Stance: **First Things First Manifesto (Ken Garland)**: the page earns its purpose before its finish (R0 found a site of invented numbers and vendor copy).
- Rules: **Grid Systems in Graphic Design (Josef Müller-Brockmann)** --codifies--> **International Typographic Style (Swiss Style)**; **WCAG 2.2 Contrast and Perceivability (W3C)**
- Breaker: **Making and Breaking the Grid (Timothy Samara)**
- Counterpoint (dotted): **Interaction of Color (Josef Albers)**, via `wcag -.->|contrast floor constrains| albers`. The slab colours are chosen by value, then measured.
- Field note 67 applied: the subject's own image (blocks stacked into layers, chains bridged) is a Frontier candidate. The v1 logo already holds it.

### Panel
From `pick_panel.py --mode adaptive --run-type full --project blockchain-explain --data-graphic`: Debord, Shklovsky, Holmes, Mace, Cairo, Tufte, Krug, and Greenberg (rotation). **Override, with a reason:** Critic: Brand (Sharp) is added for logo 2.0 and for subject character (field note 67). Dotted pairs: Debord and Krug; Shklovsky and Krug.

### Panel, WHOLE, round R0 (the inherited site; evidence in panel/R0-v2/EVIDENCE.md)
| Critic | Anchor used | Observed in the work | Verdict PASS/OBJECT | Requested change |
|---|---|---|---|---|
| Critic: Evidence (Cairo) | How Charts Lie (Alberto Cairo) | every hash and count typed by hand (no script on any page); the block, hash and Merkle sections printed twice; CometBFT drawn under "Cosmos SDK Layer 0" on one page and the reverse on another; "a minority" for the fault bound; "unique" hashes; the Merkle tree described as a storage trick | OBJECT | compute every value from editable input; one consistent stack; the exact bound (< 1/3); "collision-resistant" |
| Critic: Usability (Krug) | Don't Make Me Think (Steve Krug) | five-second test passes at 1280; the first action is below the fold at 390; two site names and two headers; the current page is not visible; a duplicate section; a skip link always visible; a 26,405 px page with no index | OBJECT | one header; mark the current page; split long pages; hide the skip link until focused |
| Critic: Provocateur (Debord) | The Society of the Spectacle (Guy Debord) | autheo.html is vendor copy ("Mainnet", "live", "production", "Migration Advantage"); validator figures 399/275/124 with no source or date; "Autheo is a decentralized operating system" stated as fact | OBJECT | only "Autheo describes itself as…"; cut the unsourced figures; general topics cited to their own documentation |

#### Resolutions, round R0
| Finding | Resolution |
|---|---|
| Cairo + Debord: "invented hashes and block values" | ADAPT (M1): every hash, root and link on the site is computed. The build computes the default values with SHA-256, and the same algorithm runs in the page (Web Crypto) so the reader can edit the input and watch the values change |
| Cairo + Krug: "sections printed twice / 26,405 px page" | ADAPT (M4): one topic per page, each section once |
| Cairo: "the stack contradicts itself" | ADAPT (M2): one stack, drawn and described the same everywhere: CometBFT (consensus) at the bottom, Cosmos SDK (the application framework, over ABCI) above it, the EVM (execution) above that, applications on top. IBC links chains sideways, and that is what "Layer 0" means on this site |
| Cairo: "'a minority' / 'unique' / Merkle as storage" | ADAPT (M1): "fewer than one third of the voting power", with the arithmetic computed for 4, 7, 10 and 100 validators; "collision-resistant"; Merkle trees prove inclusion |
| Debord: "vendor copy; unsourced figures" | ADAPT (M4): the site becomes a general explainer of the stack. Autheo keeps one short case-study page in Autheo's own terms ("Autheo describes itself as…"), with no mainnet, "live", validator or tooling claims |
| Krug: "two sites in one / current page invisible / skip link" | ADAPT (M3): one header and one name, the logo linking home, the current page underlined, the skip link hidden until focused |

### Panel, WHOLE, round R1 (the built 2.0 site; evidence in panel/R1-v2/)
| Critic | Anchor used | Observed in the work | Verdict PASS/OBJECT | Requested change |
|---|---|---|---|---|
| Critic: Evidence (Cairo) | How Charts Lie (Alberto Cairo): a graphic is a claim, so its numbers, its legibility and its words must all be true. | Every hash and BFT number is true. Both heroes fit the first screen, and focus rings on the SVG links are visible. Three measured defects: (a) white text on the consensus green `--s-cons` #1f8a52 measures **4.36:1**, below the 4.5:1 AA minimum for normal-size text. This affects the "CometBFT" slab labels (17px/700 is below the 18.66px bold large-text size), the active layer strip (16px/700), and the "1" in the layer list, in both themes. On the same fill, `.lstrip .on small` (#e6f4ec, 13px) measures **3.85:1**. (b) The Autheo page says post-quantum "signature schemes … ML-KEM, ML-DSA and SLH-DSA", but ML-KEM (FIPS 203) is a key-encapsulation mechanism, not a signature scheme. (c) The Basics page says the Bitcoin paper is "where hash chains and Merkle trees first met". That is overstated: Haber–Stornetta and Bayer–Haber–Stornetta (1991–92) combined them first, and the Bitcoin paper cites them. | OBJECT | (a) In both themes, change `--s-cons` from #1f8a52 to **#1a7d47**: white measures 5.16:1 on it and #e6f4ec 4.55:1. Keep `-l`/`-r` darker than the new top face. (b) Change it to "cryptography meant to resist quantum computers: NIST standardized ML-KEM (key exchange) and ML-DSA and SLH-DSA (signatures) in 2024". (c) Change it to "the Bitcoin paper, which put hash-linked timestamping (Haber and Stornetta, 1991) and Merkle trees to work in a currency". Optional: make "Every validator sees transactions arrive in a different order" read "may see". |
| Critic: Usability (Krug) | Don't Make Me Think (Steve Krug): five-second test, "street signs and breadcrumbs" (always know where you are and where to go next), self-evident over self-explanatory | Desktop home passes the five-second test and the hero marks can be traced. On a phone, though, the hero drops the "a transaction travels down" label and the Chain B column, so the dotted line has no name and the IBC arrow ends at the screen edge with nothing there. No page has a "Next topic" link at the bottom. On mobile the header is `position: static`, so after reading Basics the visitor reaches the footer (About and Source) and has to scroll all the way back up to use Menu. "Re-link the chain" repairs every block in one click and does not show which hashes it rewrote. That contradicts the copy above the demo ("the break moves down the chain"), so a first-time visitor sees everything turn green again and learns "tampering is easy to fix". | OBJECT | (1) Add a prev/next pager at the end of every topic page's `main`, in the nav order Home, Basics, Consensus, Cosmos SDK, EVM, Layer 0, Autheo, Glossary (for example "Next: Consensus →"). (2) In the phone hero, keep the "a transaction travels down" label on the dotted line and end the IBC arrow at a labelled "Chain B" stub (or a sliver of the second stack) instead of empty space. (3) Make the re-link demo show its own lesson: either put a "Re-link this block" button on the broken block so the break visibly moves to the next block, or after the full re-link mark each block whose hash changed as "rewritten" and give a count ("3 blocks rewritten to hide 1 edit"). |
| Critic: Brand Strategy (Sharp) | How Brands Grow (Byron Sharp): distinctive brand assets must stay consistent so people recognise them, stay visible at the sizes where the brand is actually seen, and appear wherever the brand shows up | Logo 2.0 keeps v1's assets: the rounded frame, three stacked layers, green on the bottom. It also carries the site's subject: isometric slabs with a dotted transaction path. The 34px header mark (inline, solid CSS-var fills) reads clearly in light and dark. It uses the same slab geometry, colour ramp and dotted path as the home hero, so the logo and the site read as one asset. "Blockchain, explained" appears identically in all 10 `<title>` tags, every `og:title` and the header wordmark. **Defects:** (1) `site/favicon.svg` (= `brand/logo-v2.svg`) at 16px, 1x: the top two slabs are pale fills at .45 and .75 opacity on the near-white ground, so they nearly disappear. The 1.1px dotted path smears. The tab shows one green blob, not a stack, and is less legible than v1's three crisp bars. (2) Every page's `og:image` points to `/og.png`, which is not in `site/` or in the build, so a shared link shows no brand image. | OBJECT | (1) Build a 16px favicon from the inline header mark, not from `logo-v2.svg`: solid fills (no opacity), the three slabs with a 1px gap and clear value steps, no dotted path at this size, and a dark ground with the bright #3cff6e base taken from `logo-v2-dark.svg`. The dark ground carries v1's most recognisable trait and holds up in both tab themes. Bring `brand/logo-v2.svg` into line with the inline mark's solid fills, so there is one master. (2) Generate `site/og.png` (1200x630: the hero stack with the logo and the name "Blockchain, explained"), or remove the `og:image` tag from `build.py` line 166. |

#### Resolutions, round R1
| Finding | Resolution |
|---|---|
| Cairo: "white on the consensus green is 4.36:1" | ADOPT: `--s-cons` is #1a7d47 in both themes (5.16:1; the small strip text 4.55:1) |
| Cairo: "ML-KEM is not a signature scheme" | ADOPT: ML-KEM for key exchange; ML-DSA and SLH-DSA for signatures |
| Cairo: "the Bitcoin paper did not first combine hash chains and Merkle trees" | ADOPT: credited with putting them to work in a currency, citing Haber and Stornetta (1991) |
| Krug: "no way on from the bottom of a page" | ADOPT: a previous/next pager on every page but home, in nav order |
| Krug: "the phone hero loses its labels; the IBC arrow points at nothing" | ADOPT: "Chain A" and "a transaction travels down" kept at 375; the arrow ends on a dashed "Chain B" stub |
| Krug: "Re-link repairs everything at once and hides the lesson" | ADOPT: the button re-links one broken block at a time and reports, in a live status line, that the break moved and how many blocks were rewritten |
| Krug (note): "Layer 1 of 4" over a strip of 3 | ADOPT: the strip shows all four layers |
| Krug (note): "computed as you read" is jargon | ADOPT: "Every hash on the site is real, and you can change the input yourself." |
| Sharp: "the favicon is a green blob at 16 px" | ADOPT: the favicon is written by the build with solid fills on the dark ground, bigger slabs and no path; `brand/logo-v2*.svg` are written by the same function with solid fills, so there is one master |
| Sharp: "og:image points at a missing og.png" | ADOPT: `_src/og.cjs` captures the 1200x630 first screen to `site/og.png`, and the build fails if it is missing; `og:site_name` added and the name is in the footer |

Step 2g re-measure after R1: every page at 1280x800, 375x812 and 390x844, light and dark: no overflow, smallest text 13 px, no target under 44 px, demo self-check ok, hero bottom 571 / 807 / 829.

## Frontier
| Candidate | Reached via | From anchor | Status |
|---|---|---|---|
| R0 objections | premortem | n/a | TAKEN (M1–M4) |
| Every value computed (purpose before finish) | First Things First Manifesto (Ken Garland) | stance | TAKEN (M1) |
| One stack, one grid | codifies | Grid Systems in Graphic Design (Josef Müller-Brockmann) | TAKEN (M2, M3) |
| Two stacks bridged across the grid | (Breaker) | Making and Breaking the Grid (Timothy Samara) | TAKEN (M2) |
| Slab colours stepped by value, measured | contrast floor constrains (dotted) | Interaction of Color (Josef Albers) | TAKEN (M3) |
| Logo 2.0 | owner's brief | n/a | TAKEN (M3) |

## Move M1: Every value computed (KEEP-THE-RULE)
Depends on: none. Anchors: Stance First Things First Manifesto (Ken Garland) | Rule WCAG 2.2 Contrast and Perceivability (W3C)
Intent: the hashing, block, chain and Merkle examples are real SHA-256, from text the reader can change. The build writes the defaults; the page recomputes them live.
Alternatives rejected: "illustrative" labels on fake values (honest, but they teach nothing); a full blockchain in JavaScript (too heavy for "very basic").
Mode field: Advanced pole: the reader breaks a chain and watches it fail. Acceptable pole: a text box and a hash, the simplest demo there is.

## Move M2: Two stacks and a bridge (BREAK)
Depends on: M1. Anchors: Breaker Making and Breaking the Grid (Timothy Samara) | Rule Grid Systems in Graphic Design (Josef Müller-Brockmann)
Intent: the landing graphic is logo 2.0 grown into a diagram: two isometric stacks, Chain A and Chain B, each made of the four layers (consensus, framework, execution, applications), standing on one bedrock (the basics). An IBC bridge crosses the gap between them at the framework layer, and a dotted transaction path runs down Chain A. Every slab, the bridge and the bedrock link to their pages.
Fence: the page grid is broken only by the bridge, which crosses the gutter between the two stacks; the break means "chains that talk".
Alternatives rejected: one stack (it cannot show Layer 0); a flat list of layers (not a form).
Mode field: Advanced pole: the site as a drawing of its subject. Acceptable pole: every part is labelled in words and is a link.

## Move M3: Light, plain, one system (KEEP-THE-RULE)
Depends on: none. Anchors: Rule International Typographic Style (Swiss Style) | Counterpoint Interaction of Color (Josef Albers)
Intent: stone-white paper, near-black ink, the logo's green deepened for text contrast, and slabs stepped from light (applications) to the green base (consensus), so each layer differs in value as well as hue. Archivo for type and IBM Plex Mono for hashes. One header, one name: "Blockchain, explained". Logo 2.0 in the header.

## Move M4: One topic per page (KEEP-THE-RULE)
Depends on: M2. Pages: home; Basics (blocks, hashes, the chain, Merkle trees: the bedrock); Consensus (CometBFT); Cosmos SDK; EVM; Layer 0 (IBC); Autheo (case study, attributed); Glossary; About; 404. The old URLs `blockchain-basics.html`, `layer0.html` and `autheo.html` are kept.
