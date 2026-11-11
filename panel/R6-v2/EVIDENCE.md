# R6 evidence: every page redone after the owner's B- ("only a B minus and needs all pages, very sloppy")

- Site: /home/user/blockchain-explain/site/ served at http://localhost:8768/site/ (Playwright: require('playwright')).
- Source: _src/build.py (page template `doc()`, home, demos), _src/figures.py (one figure per topic, sidebar map), _src/content.py (copy), site/css/site.css (the "2.1" section at the end is the new template), site/js/demos.js.
- What changed: one template for every inner page (sidebar map of the stack with "you are here" and the page's contents; kicker, title, lede; an "In one line" key idea; a drawn figure; numbered sections; "Try it" demo panels; read-further links; pager). Home: guide cards in reading order and three computed facts. Glossary by letter.
- Screenshots here: <page>-1280.png and <page>-375.png, full page, light.
- measure.json: 16 pages x 1280x800, 375x812, 390x844, 320x640, light and dark: no overflow, smallest text 12.6 px, no target under 44 px, demo self-checks ok.
