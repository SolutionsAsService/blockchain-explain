// The acceptance test the R0 panel asked for: one command, no judgement.
//
//   node tools/verify.mjs
//
// For every page: every href/src resolves to a file that exists; no reference
// to a stylesheet or script that is missing; the document ends in </html>; and
// opened structural tags balance closed ones (void elements excluded).
// Exits non-zero if any page fails.

import { readdir, readFile } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { join, dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const VOID = new Set(['area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr']);

const files = (await readdir(root)).filter((f) => f.endsWith('.html')).sort();
let failures = 0;

for (const file of files) {
  const src = await readFile(join(root, file), 'utf8');
  const problems = [];

  // 1. every local reference resolves
  const refs = [...src.matchAll(/(?:href|src)="([^"]+)"/g)].map((m) => m[1]);
  for (const ref of new Set(refs)) {
    if (/^(https?:|mailto:|#|data:)/.test(ref)) continue;
    const target = resolve(root, dirname(file), ref.split('#')[0]);
    if (!existsSync(target)) problems.push(`unresolved reference: ${ref}`);
  }

  // 2. the document closes
  if (!/<\/html>\s*$/.test(src.trim())) problems.push('does not end with </html>');

  // 3. structural tags balance
  const stack = [];
  for (const m of src.matchAll(/<(\/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*?)(\/?)>/g)) {
    const [, slash, tag, attrs, selfClose] = m;
    const name = tag.toLowerCase();
    if (VOID.has(name) || selfClose === '/') continue;
    if (slash) {
      if (stack[stack.length - 1] === name) stack.pop();
      else problems.push(`closing </${name}> does not match <${stack[stack.length - 1] ?? 'nothing'}>`);
    } else {
      stack.push(name);
    }
  }
  if (stack.length) problems.push(`unclosed tags: ${stack.join(', ')}`);

  // 4. no third-party request
  const hosts = [...new Set([...src.matchAll(/https?:\/\/([^\/"']+)/g)].map((m) => m[1]))]
    .filter((h) => !h.includes('github.com') && !h.includes('gnucobol') && !h.includes('wikipedia'));
  if (hosts.length) problems.push(`third-party host(s): ${hosts.join(', ')}`);

  const ok = problems.length === 0;
  if (!ok) failures++;
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${file}`);
  problems.forEach((p) => console.log(`        ${p}`));
}

console.log(failures === 0 ? '\nall pages pass the acceptance test' : `\n${failures} page(s) failed`);
process.exit(failures === 0 ? 0 : 1);
