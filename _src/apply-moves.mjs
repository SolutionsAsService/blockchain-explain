/* DADA move application + repair pass. Run: node _src/apply-moves.mjs */
import { readFileSync, writeFileSync } from 'node:fs';

const R = 'H:/blockchain-explain';

/* ---- helper: remove a CSS rule block by its opening line ---------------- */
function removeBlocks(src, starts) {
  const lines = src.split('\n');
  const out = [];
  let i = 0;
  let removed = 0;
  while (i < lines.length) {
    const t = lines[i].trim();
    const hit = starts.find((s) => t === s || t.startsWith(s + '{') || t.startsWith(s + ' ') || t.startsWith(s + ','));
    if (hit) {
      let depth = 0;
      let j = i;
      do {
        depth += (lines[j].match(/\{/g) || []).length - (lines[j].match(/\}/g) || []).length;
        j++;
      } while (j < lines.length && depth > 0);
      removed += j - i;
      i = j;
      continue;
    }
    out.push(lines[i]);
    i++;
  }
  return { text: out.join('\n'), removed };
}

/* ---- 1. index.html retargets the new sheet ----------------------------- */
let idx = readFileSync(`${R}/index.html`, 'utf8');
const idxBefore = idx;
idx = idx.replace('<link rel="stylesheet" href="css/style.css">', '<link rel="stylesheet" href="css/site.css">');
writeFileSync(`${R}/index.html`, idx, 'utf8');
console.log(`index.html stylesheet -> site.css : ${idxBefore !== idx ? 'APPLIED' : 'NO CHANGE'}`);

/* ---- 2. style.css: strip the atmosphere, add the access floor ---------- */
let css = readFileSync(`${R}/css/style.css`, 'utf8');
const before = {
  gridMove: (css.match(/gridMove/g) || []).length,
  blur: (css.match(/filter:\s*blur\(/g) || []).length,
  bytes: Buffer.byteLength(css),
};

for (const sel of ['@keyframes gridMove', '.grid-background', '.glow', '.glow1', '.glow2']) {
  const r = removeBlocks(css, [sel]);
  css = r.text;
}

// Any surviving reference to the removed animation or to a blur.
css = css.split('\n').filter((l) => !/animation:\s*gridMove/.test(l) && !/filter:\s*blur\(/.test(l)).join('\n');

css += `
/* --- appended by the DADA R0 resolution -------------------------------- */
/* Mace / Holmes: one focus ring on every interactive element, in both
   themes. The inherited sheet had exactly one :focus rule and it removed the
   ring; there are 28 anchors on the home page. */
:focus-visible {
  outline: 3px solid var(--primary) !important;
  outline-offset: 2px !important;
}

/* Holmes: the four infinite animations had no opt-out at all. */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation: none !important;
    transition: none !important;
    scroll-behavior: auto !important;
  }
}

/* Holmes: the sticky header occluded its own jump target
   (scroll-padding-top / scroll-margin-top count was 0). */
html {
  scroll-padding-top: 6rem;
}

/* Debord: 12 classes were used in the HTML with no rule anywhere in this
   sheet, so the centrepiece "How Autheo Is Built" stack rendered as bare text
   with down-arrow glyphs. These are the diagram classes. */
.architecture-stack { display: grid; gap: 0; margin: 2rem 0; }
.stack-layer {
  border: 1px solid var(--border, #1e1e1e);
  background: var(--panel, #0d0d0d);
  padding: 1.25rem 1.5rem;
  border-radius: 3px;
}
.stack-layer.highlight {
  border-color: var(--primary);
  background: rgba(60, 255, 110, 0.08);
}
.stack-arrow { text-align: center; color: var(--primary); padding: 0.35rem 0; font-size: 1.1rem; }
.network-map { display: grid; gap: 1rem; }
.network-node { border: 1px solid var(--border, #1e1e1e); padding: 1rem; border-radius: 3px; }
.network-node.center-node { border-color: var(--primary); }
.network-node.connected { border-style: solid; }
.application { border: 1px solid var(--border, #1e1e1e); padding: 1rem; border-radius: 3px; }
.block-visual { border: 1px solid var(--border, #1e1e1e); padding: 1rem; border-radius: 3px; }
.block-header { font-weight: 700; margin-bottom: 0.5rem; }
.block-row { display: flex; justify-content: space-between; gap: 1rem; padding: 0.35rem 0; }
`;

writeFileSync(`${R}/css/style.css`, css, 'utf8');
const after = {
  gridMove: (css.match(/gridMove/g) || []).length,
  blur: (css.match(/filter:\s*blur\(/g) || []).length,
  bytes: Buffer.byteLength(css),
};
console.log(`style.css gridMove : ${before.gridMove} -> ${after.gridMove}  ${after.gridMove === 0 ? 'PASS' : 'FAIL'}`);
console.log(`style.css blur     : ${before.blur} -> ${after.blur}  ${after.blur === 0 ? 'PASS' : 'FAIL'}`);
console.log(`style.css bytes    : ${before.bytes} -> ${after.bytes}`);

/* ---- 3. inner pages: drop references to files that do not exist -------- */
const FIX = `
</main>
<footer class="footer"><div class="wrap"><p>Autheo, explained.</p></div></footer>
</body>
</html>
`;
for (const f of ['autheo.html', 'blockchain-basics.html', 'layer0.html']) {
  let h = readFileSync(`${R}/${f}`, 'utf8');
  const b = h;
  h = h.replace(/<link rel="stylesheet" href="css\/animations\.css">\s*/g, '');
  h = h.replace(/<link rel="stylesheet" href="css\/responsive\.css">\s*/g, '');
  h = h.replace(/<script src="js\/app\.js"><\/script>\s*/g, '');
  // A document that never closes is not a document.
  if (!/<\/html>\s*$/.test(h.trim())) {
    h = h.replace(/\s*$/, '\n') + FIX;
  }
  writeFileSync(`${R}/${f}`, h, 'utf8');
  const open = (h.match(/<[a-zA-Z][a-zA-Z0-9]*[\s>]/g) || []).length;
  const closed = (h.match(/<\/[a-zA-Z]/g) || []).length;
  console.log(`${f}: refs removed=${b !== h}, ends </html>=${/<\/html>/.test(h)}, tags ${open}/${closed}`);
}
