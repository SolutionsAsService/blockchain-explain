/* Bringhurst's R1 resolution. Run: node _src/apply-moves-5.mjs */
import { readFileSync, writeFileSync } from 'node:fs';

const R = 'H:/blockchain-explain';
let css = readFileSync(`${R}/css/site.css`, 'utf8');
const before = css;
const changes = [];

/* 1. The h1 clamp: the fluid term bound only across 549-558px, so below that
      the headline was pinned at 38.4px on a 280px measure — 14.6 characters
      per line at 320px, five lines for a 68-character headline. */
if (css.includes('clamp(2.4rem, 7vw, var(--t-4))')) {
  css = css.replace(
    'clamp(2.4rem, 7vw, var(--t-4))',
    'clamp(1.75rem, 4.6vw + 1rem, var(--t-4))',
  );
  changes.push('h1 clamp: fluid term now governs 320-501px');
}

/* 2. Guard the unguarded exit: on a fallback face whose "0" is wider (DejaVu
      Sans, 0.636em) 62ch measures 77 characters, past Bringhurst's ceiling. */
if (css.includes('max-width: var(--measure);')) {
  css = css.replace('max-width: var(--measure);', 'max-width: min(var(--measure), 34em);');
  changes.push('p measure capped at min(62ch, 34em)');
}

/* 3. Use --t-2, which was declared and referenced nowhere. The figure's layer
      names are the largest text on the page after the headline. */
if (css.includes('clamp(1rem, 2.4vw, var(--t-1))')) {
  css = css.replace('clamp(1rem, 2.4vw, var(--t-1))', 'clamp(1rem, 2.4vw, var(--t-2))');
  changes.push('.s-name now spends --t-2');
}

/* 4. --t-3 was declared and referenced nowhere. The scale in use is
      --t--1, --t-0, --t-1, --t-2, --t-4. */
if (css.includes('  --t-3: 1.953rem;\n')) {
  css = css.replace('  --t-3: 1.953rem;\n', '');
  css = css.replace(
    '  /* Type: one modular scale, ratio 1.25. */',
    '  /* Type: one modular scale, ratio 1.25. Steps in use: --t--1, --t-0,\n     --t-1, --t-2 and --t-4. A step declared and never spent is noise, so\n     --t-3 is not declared. */',
  );
  changes.push('--t-3 removed (was dead)');
}

/* 5. Heading air: a heading wants more space above it than below it. The
      layer card gave 8px on both sides while a paragraph break got 24px. */
if (css.includes('.layer-num {\n  font-family: var(--font-mono);')) {
  css = css.replace(
    /(\.layer-num \{[^}]*?)margin-bottom: var\(--u\);/,
    '$1margin-bottom: calc(var(--u) * 1.5);',
  );
  changes.push('layer heading: more air above than below');
}

writeFileSync(`${R}/css/site.css`, css, 'utf8');
console.log(changed(before, css) ? 'changes applied:' : 'no change');
changes.forEach((c) => console.log('  - ' + c));

function changed(a, b) {
  return a !== b;
}
