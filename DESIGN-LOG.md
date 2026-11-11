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
