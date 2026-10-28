// Prints WCAG 2.x contrast ratios for every colour pair css/site.css uses.
// Every ratio quoted in DESIGN-LOG.md is reproducible by running:
//   node tools/contrast.mjs
// A pair that is not in this file cannot be claimed in the log.

const HEX = (h) => {
  const n = h.replace('#', '');
  return [0, 2, 4].map((i) => parseInt(n.slice(i, i + 2), 16) / 255);
};
const LIN = (c) => (c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);
const LUM = (h) => {
  const [r, g, b] = HEX(h).map(LIN);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
};
const RATIO = (a, b) => {
  const [x, y] = [LUM(a), LUM(b)].sort((m, n) => n - m);
  return (x + 0.05) / (y + 0.05);
};

// [label, foreground, background, minimum required]
const PAIRS = [
  ['dark: body ink on paper', '#e8ede9', '#0a0c0b', 4.5],
  ['dark: muted on paper', '#9ba8a0', '#0a0c0b', 4.5],
  ['dark: accent on paper', '#3cff6e', '#0a0c0b', 4.5],
  ['dark: ink on panel', '#e8ede9', '#121614', 4.5],
  ['dark: muted on panel', '#9ba8a0', '#121614', 4.5],
  ['dark: ink on raised', '#e8ede9', '#171c19', 4.5],
  ['dark: label on accent band', '#04120a', '#3cff6e', 4.5],
  ['dark: label on accent band (gradient end)', '#04120a', '#12b37a', 4.5],
  ['dark: nav link on paper', '#9ba8a0', '#0a0c0b', 4.5],
  ['light: body ink on paper', '#0a0c0b', '#f4f6f4', 4.5],
  ['light: muted on paper', '#4d5a53', '#f4f6f4', 4.5],
  ['light: accent on paper', '#0f7a3d', '#f4f6f4', 4.5],
  ['light: ink on panel', '#0a0c0b', '#ffffff', 4.5],
  ['light: muted on panel', '#4d5a53', '#ffffff', 4.5],
  ['light: ink on raised', '#0a0c0b', '#eef2ef', 4.5],
  ['light: label on accent band', '#ffffff', '#0f7a3d', 4.5],
  ['dark: focus ring on paper', '#3cff6e', '#0a0c0b', 3.0],
  ['light: focus ring on paper', '#0f7a3d', '#f4f6f4', 3.0],
];

let fails = 0;
for (const [label, fg, bg, min] of PAIRS) {
  const r = RATIO(fg, bg);
  const ok = r >= min;
  if (!ok) fails += 1;
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${r.toFixed(2)}:1  (min ${min})  ${label}  ${fg} on ${bg}`);
}
console.log(fails === 0 ? '\nall pairs pass' : `\n${fails} pair(s) below threshold`);
process.exit(fails === 0 ? 0 : 1);
