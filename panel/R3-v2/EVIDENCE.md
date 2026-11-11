# R3 evidence: Blockchain, explained 2.0 (built site)

- Site source: /home/user/blockchain-explain/site/ (10 pages). Live locally at http://localhost:8768/site/ (Playwright: require('playwright'), chromium.launch()).
- Generator: /home/user/blockchain-explain/_src/build.py, copy in _src/content.py, demos in site/js/demos.js, CSS site/css/site.css.
- Design intent and R0 objections: /home/user/blockchain-explain/DESIGN-LOG.md (moves M1–M4).
- Logos: brand/logo-v1.svg (kept, owner said "this logo is good"), brand/logo-v2.svg, brand/logo-v2-dark.svg; the header uses an inline variant.
- Screenshots in this folder: <page>-<width>-<scheme>.png (1280 and 375; index also dark).
- measure.json: re-measured after the R1 fixes: no overflow, smallest text 13px, no target under 44px except the off-screen skip link, demo self-check ok, hero bottom 571 (1280x800) / 807 (375x812) / 829 (390x844); 320x640 added, no overflow.
- Brief from owner: "full site redesign, very basic total makeover"; keep the logo, make a version 2.0.
- R1 and R2 objections and resolutions: DESIGN-LOG.md ('Resolutions, round R1' and 'round R2'). Verdict files in panel/R1-v2/ and panel/R2-v2/.
