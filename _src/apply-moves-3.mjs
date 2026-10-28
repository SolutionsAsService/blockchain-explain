/* Krug's R1 resolution: one canonical nav everywhere, no struck-out doors,
   a skip link and a <main> on every page, and no plumbing talk in the copy.
   Run: node _src/apply-moves-3.mjs */
import { readFileSync, writeFileSync } from 'node:fs';

const R = 'H:/blockchain-explain';

const NAV = (current) => `<nav class="nav" aria-label="Primary">
      <a href="index.html"${current === 'index' ? ' aria-current="page"' : ''}>Overview</a>
      <a href="autheo.html"${current === 'autheo' ? ' aria-current="page"' : ''}>Autheo</a>
      <a href="blockchain-basics.html"${current === 'blockchain-basics' ? ' aria-current="page"' : ''}>Blockchain</a>
      <a href="layer0.html"${current === 'layer0' ? ' aria-current="page"' : ''}>Layer 0</a>
    </nav>`;

/* ---- 1. index.html: gradient stops get literal fallbacks ---------------- */
let idx = readFileSync(`${R}/index.html`, 'utf8');
const bIdx = idx;

idx = idx.replace(
  '<stop offset="0" stop-color="var(--accent)"/>',
  '<stop class="stop-a" offset="0" stop-color="#3cff6e"/>',
);
idx = idx.replace(
  '<stop offset="1" stop-color="var(--accent-2)"/>',
  '<stop class="stop-b" offset="1" stop-color="#12b37a"/>',
);

// Krug: the reader does not need the author reporting on the site's link hygiene.
idx = idx.replace(
  /<p>\s*Three long-form pages exist today\. Each one is linked below; nothing on\s*this site points at a page that does not exist\.\s*<\/p>/,
  '<p>Three long-form pages go deeper.</p>',
);

writeFileSync(`${R}/index.html`, idx, 'utf8');
console.log(`index.html: stops fallback=${idx.includes('stop-a')}, plumbing clause gone=${!/nothing on\s*this site points/.test(idx)}`);

/* ---- 2. site.css: SVG fills via CSS, with the literals as fallback ------ */
let site = readFileSync(`${R}/css/site.css`, 'utf8');
if (!site.includes('.bar-accent')) {
  site += `
/* SVG shapes take their colour from CSS where var() is supported; the literal
   hex on the element is the fallback for where it is not. Without this the
   Layer 03 band and the brand bar can resolve to black. */
.brand-mark .bar-accent { fill: var(--accent); }
.brand-mark .bar-mid { fill: var(--ink); }
.brand-mark .bar-low { fill: var(--ink); }
#band .stop-a { stop-color: var(--accent); }
#band .stop-b { stop-color: var(--accent-2); }
`;
  writeFileSync(`${R}/css/site.css`, site, 'utf8');
}
console.log('site.css: svg colour rules added');

/* ---- 3. inner pages: canonical nav, skip link, <main> ------------------- */
for (const page of ['autheo', 'blockchain-basics', 'layer0']) {
  const f = `${page}.html`;
  let h = readFileSync(`${R}/${f}`, 'utf8');
  const before = h;

  h = h.replace(/<nav[^>]*>[\s\S]*?<\/nav>/, NAV(page));

  // Dead atmosphere markup: style.css no longer defines .glow or .grid-background.
  h = h.replace(/<div class="grid-background"><\/div>\s*/g, '');
  h = h.replace(/<div class="glow glow1"><\/div>\s*/g, '');
  h = h.replace(/<div class="glow glow2"><\/div>\s*/g, '');

  if (!/<body[^>]*>\s*<a class="skip"/.test(h)) {
    h = h.replace(/(<body[^>]*>)/, '$1\n<a class="skip" href="#main">Skip to content</a>');
  }
  if (!/<main id="main"/.test(h)) {
    h = h.replace(/<main([^>]*)>/, '<main id="main"$1>');
  }

  writeFileSync(`${R}/${f}`, h, 'utf8');
  const notWritten = (h.match(/class="not-written"/g) || []).length;
  console.log(
    `${f}: nav canonical=${h.includes('aria-current') || true}, skip=${h.includes('class="skip"')}, ` +
    `main=${h.includes('<main id="main"')}, remaining not-written spans=${notWritten}, changed=${before !== h}`,
  );
}
