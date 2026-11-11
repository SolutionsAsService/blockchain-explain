# R7-v2 critique: Critic: Formalist (Greenberg)

| Critic | Anchor used | Observed in the work | Verdict PASS/OBJECT | Requested change |
|---|---|---|---|---|
| Critic: Formalist (Greenberg) | Modernist Painting (Clement Greenberg): the medium earns its authority by being exactly itself, so the flat plane, the grid and the type have to be exact. | Most of my R6 items are fixed and hold up on the live build. There is one content edge (x=80) on every page. Nav links no longer move between pages. The guide-card titles share one line (670 px). Hashes split 32/32. Figures are 360 px with 15 px labels. The Basics label is whole, the Contracts arrowheads are separate, and the sidebar has one active style. The Risks figure and the glossary template are done. However, the new Consensus opening figure brings back exactly the defect class R6 was about: "A CHEATER'S REWRIT" is cut off where it runs into the Block 3′ box, at 1280 and at 375. `measure.cjs` misses it because it checks the label against the SVG edge, not against other shapes. Smaller leftovers: two left edges in the sign demo, a mini-map connector that stops short of the Bridges box, cramped figure boxes, and an unchanged phone hero. | OBJECT | Fix item 1 (one line in `fork_fig`). Extend `measure.cjs` to flag any `<text>` that overlaps a `<rect>` it is not inside. Then items 2-8. After that this seat expects to PASS. |

## R6 items re-checked

| R6 # | Status |
|---|---|
| 1 Basics label clipped | Fixed ("is the next “previous”") |
| 2 Contracts arrowheads merged | Fixed |
| 3 Two left edges | Fixed: header, hero, sections and footer all at x=80 |
| 4 Card titles staggered, badge borders | Fixed: titles all at 670 px, one badge border |
| 5 Sidebar map active styles, label collision, floating bridge box | Mostly fixed. The inactive connector still looks unattached (item 3 below) |
| 6 Nav moves between pages | Fixed |
| 7 Hash orphans, label sizes | Fixed |
| 8 Figure type scale | Fixed: 15 px at 1280, at least 12 px at 320 |
| 9 Template gaps | Risks and glossary fixed. Chains (the table is the figure) and Autheo/About deferred; the reason is accepted, but Autheo and About still have no pager |
| 10 Sign demo edges, button family | Buttons fixed (dimmed ink). Edges only partly fixed (item 2) |
| 11 Awkward breaks | Mostly fixed. The Chains lede still breaks "well-/known" at 1280 (item 6) |
| 12 Residue | Glossary letters and the Chains table font sizes fixed. Copy wording unified |

## Remaining defects, most visible first

1. **Consensus, opening figure: "A CHEATER'S REWRITE" is cut off by the Block 3′ box** (1280 and 375). The text starts at x=8, runs about 180 units wide in 15px uppercase, and the box starts at x=184. The chain arrows are also too short: `arrow(x-8 → x-2)` is 6 units long and carries a 7-unit marker, so every arrowhead touches both boxes ("Block 1▶Block 2"). Fix in `_src/figures.py`, `fork_fig` (line 179): set the label on two lines, `<tspan x="8" y="146">a cheater’s</tspan><tspan x="8" y="166">rewrite</tspan>`. Then set `xs = [8, 98, 188, 278]` with box width 74 so the gap is 16, and draw the arrows `arrow(fid, x - 14, 54, x - 2, 54)` (and the same for the rewrite row). Also add a text-against-rect overlap test to `measure.cjs`.
2. **Keys, sign demo: still two left edges.** The "1." and "2." markers, the buttons, the hints ("Make a key pair first.") and the Public key/Signature rows sit at x=401. The step labels and both inputs sit at x=419, because of `.steps li>label{display:inline-block;width:calc(100% - 2em)}` (site.css line 348). Fix: `.steps li>label{display:block;width:auto}` and make the number part of the label (`<span class="num">1.</span> Transaction`), so the input sits at 401 under the number like everything else.
3. **Sidebar mini-map, every page except Bridges: the connector looks unattached.** The inactive path `M160,yb+6 L206,yb+6 L206,yb-4` (figures.py line 160) has a 10-unit vertical leg. With `stroke-dasharray:4 3` (site.css line 246) that leg draws as one short tick, so the line appears to stop before the Bridges box. Fix: give the vertical leg its own solid segment, or set `.mn-br{stroke-dasharray:none;stroke-width:1.5}` and keep the dash only on the horizontal run.
4. **Bridges figure: text touches box edges.** "signers" has 2.9 px clearance in its 56-unit warning box, and "checks the proof" nearly fills the 124-unit Light client box. Fix (figures.py lines 124-133): narrow the arrows to 12 units and widen the boxes, for example `box(4, 62, 128, …)`, `box(148, 62, 64, …)` for signers, `box(228, 62, 128, …)`; do the same for the Light client box.
5. **Risks figure: the four level boxes use mismatched styles, and one label is cramped.** Keys has a grey fill and no border, Contracts and Consensus have green fills, and Bridges is white with a 2px ink outline, so Bridges reads as "selected". "Smart contracts" in 15px bold has about 4 px clearance in its 130-unit box. Fix in `risks_fig` (line 195): give `.s-bridge` a fill (for example `var(--s-exec)` with a green stroke, matching the mini-map's active Bridges box) and widen the level box to 140 (move the risk box to x=172, width 180).
6. **Chains lede: "well-/known" still breaks across the line at 1280.** Fix: use a non-breaking hyphen, `well‑known` (U+2011), in `content.py`, as was already done for "Re‑link".
7. **Home, phone hero (375): unchanged since R6.** Chain B is still a squashed dashed tab with rotated text at the right edge. The pill says "Bridge" on the phone and "Bridges" on desktop. The bedrock says "hashes and blocks" on the phone and "blocks, hashes and Merkle trees" on desktop, and "→ Basics" wraps alone onto its second line. Fix (the `.hero-narrow` SVG in build.py): use the same wording at both widths ("Bridges", "Bedrock: blocks and hashes → Basics" on one line), and either draw Chain B as a second small stack or drop it and end the bridge arrow at a labelled "Chain B" box the same height as the pill.
8. **Small residue.**
   - (a) Glossary sidebar: the letters are centred in 44 px links, so they sit about 12 px right of the 80 px sidebar edge that "LETTERS" and the "ON THIS PAGE" numbers use. Fix: `justify-content:flex-start`.
   - (b) Contracts figure: the third line, "was Ada 100 · Ben 100", is set in Archivo while the line above is Plex Mono. Use `"m"` for both (figures.py, `contract_fig`).
   - (c) Autheo and About are still the only inner pages without a pager. A Previous/Next pair (Chains ↔ Autheo, Glossary ↔ About) would finish the template.
