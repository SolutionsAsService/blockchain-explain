/* Rewrites the graphic block of css/site.css: the figure's labels become real
   HTML text so they cannot scale below legibility. Run: node _src/apply-moves-4.mjs */
import { readFileSync, writeFileSync } from 'node:fs';

const R = 'H:/blockchain-explain';

const START = '/* ------------------------------------------------------------ the graphic */';
const END = '/* ------------------------------------------------------------------ prose */';

const BLOCK = `/* ------------------------------------------------------------ the graphic */

/* A cross-section built from elements rather than drawn in SVG. The reason is
   measured: an SVG scaled by its viewBox scales its labels too, so the note
   labels rendered at 3.5px on a 360px viewport and 20px at 1920px. Here the
   bands are laid out by the same grid as the rest of the page and the labels
   sit on the page's own type scale — smallest is 0.8rem, 12.8px, at every
   width. One bit of information (which layer executes) gets one colour. */

.strata-wrap {
  margin: 0 0 calc(var(--u) * 12);
  padding-inline: calc(var(--u) * 4);
}

@media (max-width: 40rem) {
  .strata-wrap {
    padding-inline: calc(var(--u) * 2.5);
  }
}

.strata {
  position: relative;
  border: 1px solid var(--rule);
  background: var(--panel);
  padding: calc(var(--u) * 3) calc(var(--u) * 3) calc(var(--u) * 3) calc(var(--u) * 8);
}

/* The axis carries the one proposition the prose cannot: that these five are
   stacked and read downward. It gets the ink. */
.strata-axis {
  position: absolute;
  left: calc(var(--u) * 4);
  top: calc(var(--u) * 4);
  bottom: calc(var(--u) * 4);
  width: 2px;
  background: var(--accent);
}

.strata-arrow {
  position: absolute;
  left: -4px;
  bottom: 0;
  width: 0;
  height: 0;
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 9px solid var(--accent);
}

.strata-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  gap: calc(var(--u) * 1.5);
}

.stratum {
  background: var(--raised);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: calc(var(--u) * 2.5) calc(var(--u) * 3);
  display: grid;
  grid-template-columns: 3rem 1fr;
  grid-template-areas: "num name" "num note";
  column-gap: calc(var(--u) * 2);
  align-items: baseline;
}

@media (max-width: 30rem) {
  .stratum {
    grid-template-columns: 2.5rem 1fr;
    padding: calc(var(--u) * 2);
  }
}

.stratum-marked {
  background: var(--accent);
  border-color: var(--accent);
}

.stratum-base {
  border-bottom-width: 3px;
}

.s-num {
  grid-area: num;
  font-family: var(--font-mono);
  font-size: var(--t--1);
  font-weight: 700;
  letter-spacing: 0.1em;
  color: var(--accent);
  margin: 0;
}

.stratum-marked .s-num {
  color: var(--on-accent);
}

.s-name {
  grid-area: name;
  font-family: var(--font-mono);
  font-size: clamp(1rem, 2.4vw, var(--t-1));
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  color: var(--ink);
  margin: 0 0 calc(var(--u) * 0.5);
}

.stratum-marked .s-name {
  color: var(--on-accent);
}

/* 0.8rem = 12.8px at every viewport width. This is the floor the SVG figure
   could not hold. */
.s-note {
  grid-area: note;
  font-family: var(--font-mono);
  font-size: var(--t--1);
  color: var(--muted);
  margin: 0;
  max-width: none;
}

.stratum-marked .s-note {
  color: var(--on-accent);
}

.strata-wrap figcaption {
  margin-top: calc(var(--u) * 2);
  font-size: var(--t--1);
  color: var(--muted);
  max-width: var(--measure);
}

`;

let css = readFileSync(`${R}/css/site.css`, 'utf8');
const a = css.indexOf(START);
const b = css.indexOf(END);
if (a === -1 || b === -1) throw new Error('markers not found');
css = css.slice(0, a) + BLOCK + css.slice(b);

// The gradient is gone with the SVG; keep the brand-mark overrides.
if (!css.includes('#band .stop-a')) {
  css += `
/* SVG shapes take their colour from CSS where var() is supported; the literal
   hex on the element is the fallback for where it is not. */
.brand-mark .bar-accent { fill: var(--accent); }
.brand-mark .bar-mid { fill: var(--ink); }
.brand-mark .bar-low { fill: var(--ink); }
`;
}
writeFileSync(`${R}/css/site.css`, css, 'utf8');
console.log('site.css: graphic block replaced with the HTML cross-section');
console.log(`  url(#band) still referenced: ${/url\(#band\)/.test(css)}`);
console.log(`  svg label classes removed  : ${!css.includes('.s-num-on')}`);
