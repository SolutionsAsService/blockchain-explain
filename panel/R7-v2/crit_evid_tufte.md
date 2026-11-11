| Critic | Anchor used | Observed in the work | Verdict PASS/OBJECT | Requested change |
|---|---|---|---|---|
| Critic: Evidence (Tufte) | The Visual Display of Quantitative Information (Edward Tufte): data-ink, graphical integrity, labels placed on the data, no claim without evidence | Re-checked all 8 figures and the sidebar map live at 1280, 375 and 320, light and dark, with getBBox. All 10 R6 fixes are in and correct: the chain label fits, faulty validators are hollow, the keys and rollup wording is true to the text, contracts has four separate arrowheads and a "before" state, the bridge link is attached, ▶ marks the current page, and labels are 15 px (14.3 px at 375, 12 px at 320). Nothing is clipped. The two new figures have defects. In fork_fig the heading "A CHEATER'S REWRITE" (x 8–197) runs into the Block 3′ box (x 184) and is cut to "REWRIT" at every width. The figure also shows the rewrite level with the honest chain while the text says it must outpace it. risks_fig's caption makes a frequency and scale claim that neither the figure nor the page supports. | OBJECT | The 5 fixes below, all in `_src/figures.py`. |

1. **fork_fig, heading collides with a box.** On `:179`, the "a cheater's rewrite" heading at x=8, y=155 is 189 units wide (8–197). The dashed Block 3′ box starts at x=184 and covers the end of the word ("REWRIT" in the screenshots, light and dark). `measure.cjs` checks only for labels clipped by the viewBox, not labels that overlap a box, so it missed this. Split the heading over two lines left of the box: `'<text x="8" y="146" class="fg-s fg-h">a cheater’s</text><text x="8" y="166" class="fg-s fg-h">rewrite</text>'`.
2. **fork_fig, shows a tie, not a race.** The honest chain stops at Block 4 and the rewrite stops at Block 4′, so the two are the same length. The figure therefore does not show the claim in its own text ("must outpace everyone else"). Draw five honest blocks so the rewrite is visibly one behind:
   - `:174`: `xs = [8, 78, 148, 218, 288]`
   - `:176`: box width `80` → `64`
   - `:180`: `arrow(fid, 110, 76, 180, 126, dashed=True)`
   - `:181`: `xs[2:4]`
   - `:183`: `arrow(fid, 212, 150, 218, 150)`

   "Block 3′" (about 56 units) fits a 64-unit box.
3. **fork_fig, the note breaks in the wrong place.** Lines `:184-186` leave "(proof of stake)" alone on its own line, away from its clause. Make the two methods parallel lines:
   - `:184`: `"to win, the rewrite must overtake the chain:"`
   - `:185`: `"proof of work: out-mine everyone else"`
   - `:186`: `"proof of stake: put a deposit at risk"`
4. **risks_fig, caption claims what nothing shows.** The caption on `:204` says "Most losses happen at the top … deeper levels fail more rarely, but at a larger scale". That is a frequency and size claim, but the figure encodes neither, and the page gives no data or source for it. Either show the numbers with a source, or say only what is drawn: `"Each part of the stack fails in its own way; the sections below say how."`
5. **risks_fig, marks with no meaning.** The arrows on `:200` link a level to its risk, but an arrow elsewhere in the guide means "becomes" or "is sent to". Here the boxes already sit side by side, so delete `:200`. Also, on `:195`, "energy use" is a cost, not a way to lose funds. Change it to `("majority attacks,", "halts and reorgs")`, which matches the page text.

Checked and passing: chain, keys, validator grid, contracts, rollup, bridges, and the sidebar map on every page in both themes. On the keys page the active "Keys & wallets" slab keeps the inactive fill, but the ▶ and the bold label make clear where you are.
