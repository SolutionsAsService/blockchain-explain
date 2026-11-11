| Critic | Anchor used | Observed in the work | Verdict PASS/OBJECT | Requested change |
|---|---|---|---|---|
| Critic: Inclusion (Mace) | Universal Design principles (Ronald Mace): 2 Flexibility in use, 4 Perceptible information, 5 Tolerance for error | Focus, contrast, reduced motion, 640px reflow and all ten R1 fixes hold. Two measured defects remain. (a) At 320 CSS px (WCAG 1.4.10 reflow, 400% of a 1280 window) the header does not fit: `.brand` is `white-space:nowrap` at 240px wide, so the Menu button spans x 272–343 and the page scrolls sideways by 23px on all 10 pages. The only nav control on a narrow screen is cut off at the edge. (b) The demos' results are only partly announced (WCAG 4.1.3). On consensus.html, `.demo-out` ("Needed to finalize: 67 · faulty it can survive: 33") has no role or aria-live. In the chain demo, an edit changes a block's status to "broken: previous no longer matches block 1" in a plain `<p>`, so the lesson is silent. Only the Re-link line is `role="status"`. The four chain inputs are all named "Data", so a screen-reader user cannot tell the blocks apart. | OBJECT | (a) Let the header fit at 320: give `.brand` `min-width:0` and let it wrap or shrink, e.g. `@media (max-width:359px){.brand{white-space:normal;font-size:1rem;line-height:1.15}}`. Then check that `scrollWidth`=320 on every page. (b) Add `aria-live="polite"` to `.demo-out` on consensus.html. Add one polite live line to the chain demo, written on input, e.g. "Block 2 is now broken: its previous hash no longer matches block 1" (or make each `.blk-s` `role="status"`). Name each data input with its block, e.g. `aria-label="Block 1 data"`, or `aria-labelledby` pointing at the "Block n" heading. |

## Measurements (Playwright, Chromium, http://localhost:8768/site/, all 10 pages)

**1. Focus visibility and order** (Tab through the whole page until it wraps; read the computed outline of each focused element)
- 1280x800: 33 / 30 / 20 / 20 / 20 / 19 / 17 / 13 / 13 / 13 stops (index, basics, consensus, cosmos-sdk, evm, autheo, layer0, glossary, about, 404). Elements without a ring of at least 2px: **0** on every page. The ring is 3px solid `--focus` with 2px offset.
- 375x812: 21 / 23 / 13 / 13 / 13 / 12 / 10 / 6 / 6 / 6 stops, **0** without a ring. The closed menu's links are correctly out of the tab order.
- Hero SVG: 11 focusable links at 1280 (bedrock, Chain A ×4, Chain B ×4, bridge, Chain B stub). Each one changed 3,981–10,280 PNG bytes between the focused and blurred screenshot, and the screenshot shows a blue 3px rectangle. Order: bedrock, then Chain A from the bottom up, then Chain B, then the bridge. That is logical; the HTML layer list that follows runs top-down (4→0), a small inconsistency with no barrier.
- Mobile Menu (375): the summary takes focus with a ring, Enter opens it, and the next 8 Tabs go Home…Glossary, each with a 3px ring at 44px height. Notes, not objections: Escape does not close the native `<details>`. Once focus leaves the last link the panel stays open and partly covers the focused "EVM / Execution" strip card: the ring stays visible at the panel's right edge, so it is not fully obscured (2.4.11 AA is met; 2.4.12 AAA is not).
- Demo inputs and button (basics): hash input, 4 data inputs, Re-link, 4 transaction inputs, all ringed and in reading order. Pager: Previous, then Next, both ringed.
- Skip link: works (the next Tab lands on "1 · Hashes" inside main).

**2. Accessibility tree** (`locator.ariaSnapshot()` and DOM inspection)
- Hero SVG: a `group` named "Two blockchain stacks on one bedrock, joined by an IBC bridge". Every link has an aria-label that contains its visible text (e.g. "Chain A, Consensus: CometBFT. Validators agree…", visible "CometBFT"), so 2.5.3 Label in Name is met.
- Tables: consensus.html `table "Equal voting power"` with a caption and 3 `columnheader` cells (`th scope=col`). PASS.
- Live regions on basics: 1 (`p.relinked role=status`). Consensus: **0**. (Five `data-role="status"` attributes appear in the source but are not ARIA roles.)
- Chain inputs: `textbox "Data"` ×4 (duplicate names). Hash input: "Type anything". Merkle inputs: "Transaction 1–4". BFT input: "Validators". Leaving the 64-character hash outputs out of a live region is right; announcing them on every keystroke would be noise.

**3. Contrast** (a walk over every text node to its solid background, plus the token pairs)
- Text nodes measured: light 527, dark 527, across the 10 pages. Below AA: **0** in both schemes. Lowest: 4.55 (small strip label on the consensus green). Lowest link: 4.55, then 5.7.
- Light: body 16.59, muted 7.50 (on panel 8.06), link #17703f 5.70 (on panel 6.13), underlined. Slab labels: apps 15.27, exec 12.60, frame 7.57, consensus (white on #1a7d47) 5.16. Bedrock 8.34.
- Dark: body 16.13, muted 9.26 (on panel 8.49), link #5fd394 9.83 (on panel 9.02). Slab labels: apps 9.09, exec 8.53, frame 5.66, consensus 5.16. Bedrock 9.12.
- Focus ring against the page: light 6.20, dark 8.83 (3:1 needed for non-text).

**4. Motion and zoom**
- `reducedMotion:'reduce'`: 0 animations, 0 transitions, `getAnimations()`=0 on all 10 pages. With no preference there are also 0 animations, so the only motion is the hover transitions, which the reduce rule removes.
- 640x400 at DPR 2 (200%): `scrollWidth`=640 on all 10 pages, no clipped text, no inner scrollers. PASS.
- **320x640 at DPR 2 (1.4.10 reflow): `scrollWidth`=343 on all 10 pages.** Brand 16–256, Menu summary 272–343; the screenshot shows "Menu" cut at the edge. At 360 it fits (`scrollWidth`=360). FAIL, so objection (a).

**5. R1 resolutions (DESIGN-LOG "Resolutions, round R1"), all verified**
- `--s-cons` is #1a7d47 in both themes: white on it 5.16, strip text 4.55. ✔
- ML-KEM for key exchange, ML-DSA and SLH-DSA for signatures (autheo.html). ✔ Haber and Stornetta (1991) credited (basics). ✔
- Pager: prev/next in nav order on basics → consensus → cosmos-sdk → evm → layer0 → autheo → glossary (glossary has prev only). None on home, about or 404, which are outside nav order. ✔
- Hero at 375/320: "Chain A", "a transaction travels down" and a dashed "Chain B" stub that the IBC arrow ends on. ✔
- Re-link: an edit to block 1 breaks block 2. Press 1 gives "Block 2 rewritten (1 so far)… the break moved to block 3"; press 2 gives "Every link holds again, after rewriting 2 blocks", in `role=status`. ✔
- Strip shows all four layers (4 links) on consensus, cosmos-sdk and evm. ✔
- Hero copy reads "Every hash on the site is real, and you can change the input yourself." ✔ (og:description still says "computed as you read", a small leftover.)
- favicon.svg has 0 `<path>` elements. ✔ og.png is 1200x630 and present, and og:site_name is set. ✔
