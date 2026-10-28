/* Second pass: discharge Mace's Andon and Holmes's nav-truth condition on the
   inner pages. Run: node _src/apply-moves-2.mjs */
import { readFileSync, writeFileSync } from 'node:fs';

const R = 'H:/blockchain-explain';
const DEAD = ['layer1','cosmos-sdk','evm','ibc','validators','did','pqcnet','ai-agents','faq','glossary'];

/* ---- 1. Mace: delete the rule that removes the native focus ring -------- */
let css = readFileSync(`${R}/css/style.css`, 'utf8');
const beforeOutline = (css.match(/outline:\s*none/gi) || []).length;
css = css.replace(/^\s*outline:\s*none\s*;?\s*$/gm, '');
css = css.replace(/\.search-box input:focus\b/g, '.search-box input:focus-visible');
writeFileSync(`${R}/css/style.css`, css, 'utf8');
const afterOutline = (css.match(/outline:\s*none/gi) || []).length;
console.log(`outline:none declarations : ${beforeOutline} -> ${afterOutline}  ${afterOutline === 0 ? 'PASS' : 'FAIL'}`);
console.log(`:focus-visible present     : ${/:focus-visible/.test(css) ? 'yes' : 'no'}`);

/* ---- 2. Holmes: no affordance may look like a door that opens ----------- */
const NOT_WRITTEN = `
/* Holmes: a topic with no page must not look like a link. */
.not-written {
  color: var(--muted, #888);
  text-decoration: line-through;
  text-decoration-color: var(--rule, #333);
  cursor: default;
  opacity: .75;
}
`;
css = readFileSync(`${R}/css/style.css`, 'utf8');
if (!css.includes('.not-written')) css += NOT_WRITTEN;
writeFileSync(`${R}/css/style.css`, css, 'utf8');

let site = readFileSync(`${R}/css/site.css`, 'utf8');
if (!site.includes('.not-written')) {
  site += `
/* A topic with no page must not look like a door. */
.not-written {
  color: var(--muted);
  text-decoration: line-through;
  cursor: default;
  opacity: .75;
}
`;
  writeFileSync(`${R}/css/site.css`, site, 'utf8');
}

/* ---- 3. inner pages: dead links become struck-through text -------------- */
for (const f of ['autheo.html', 'blockchain-basics.html', 'layer0.html']) {
  let h = readFileSync(`${R}/${f}`, 'utf8');
  let converted = 0;

  for (const dead of DEAD) {
    // Multi-line-tolerant: an <a> pointing at a file that does not exist.
    const re = new RegExp(`<a\\s+href="${dead}\\.html"[^>]*>([\\s\\S]*?)</a>`, 'g');
    h = h.replace(re, (_m, inner) => {
      converted++;
      return `<span class="not-written">${inner.trim()}</span>`;
    });
  }

  // No third-party request: the webfont goes, the system stack takes over.
  const b = h;
  h = h.replace(/<link rel="preconnect"[^>]*>\s*/g, '');
  h = h.replace(/<link[^>]*fonts\.googleapis\.com[^>]*>\s*/g, '');
  writeFileSync(`${R}/${f}`, h, 'utf8');
  console.log(`${f}: dead links -> not-written: ${converted}, webfont removed: ${b !== h}`);
}
