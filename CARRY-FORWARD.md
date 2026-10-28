# CARRY-FORWARD — durable facts for DADA runs on static sites

Read this before Step 1 of any later DADA run on this project or on a sibling
static site. Facts established by measurement, of the kind a later run would
otherwise rediscover the hard way.

## What worked in earlier runs, and is worth repeating

**Measure the inheritance before the first move.** On LearnCOBOL the R0 premortem
table (links that resolve, contrast ratios, longest line at 2560px, bytes of the
whole site) did more work than any later move: it turned eight critics' opinions
into eight objections with numbers attached, and it let one objection be
**OVERRULED by measurement** rather than answered with a move. Premortem tables
are cheap and they change the verdicts.

**One generated file, one source of truth.** LearnCOBOL ships `programs.js`,
generated from the `.cbl` files by `tools/index-programs.mjs`. Every figure the
page prints is recomputed at build time, so the page cannot go stale, and the
"every number here is measured" claim is checkable by re-running one command.
Where a figure is printed in markup *and* derived from data, reconcile them at
load so a stale number cannot survive.

**A measurement tool that lives in the repo.** `tools/contrast.mjs` lists every
colour pair the site uses with its required minimum and prints PASS/FAIL. A pair
that is not in that file cannot be claimed in the log. This converted "the palette
looks accessible" into 16 printed ratios.

**The instrument, not a texture.** LearnCOBOL's 80-column ruler teaches the fixed
format *and* lays out the code beneath it. WTF-revamp's hero is a large inline SVG
(a gradient sun cut by mask bands), not stock art. Both were the strongest single
element in their respective runs. A diagram that earns its place by being the thing
explained beats decoration every time.

**A build pipeline for multi-page sites.** WTF-revamp keeps `_src/pages/*.html`,
wraps them in `_src/layout.html` via `_src/build.py`, and writes the result to the
repository root. Editing seven pages means editing seven files, not seven copies of
a header.

**Real metadata.** WTF-revamp ships `og:` tags, `theme-color`, favicon in both
`.svg` and `.ico`, and a skip link. Cheap, and it is the difference between a page
and a project.

## Facts about the medium (CSS/HTML), each with the measurement that established it

- **A media query adds no specificity.** A later plain rule beats an earlier
  media-query rule at equal specificity. Any responsive override must either come
  after the plain rule in source order or raise its specificity deliberately.
  *(Found on LearnCOBOL: `body.light-mode` never overrode the `p`/`ul` colour
  rules, so the "accessible" light theme measured 2.17:1 where the dark theme
  measured 7.68:1.)*
- **`ch` resolves to the advance of "0", which is wider than the average character
  in a proportional face.** A measure set to `66ch` lands nearer 72 real
  characters. Calibrate down — LearnCOBOL uses `60ch`.
- **A percentage width on a grid item sized by an `fr` track is inert**, because
  the track absorbs it. Set the measure on the text element, not the container.
- **`--col: calc(100% / 80)` makes a column a fraction of whatever box it sits
  in** — true inside the code field and false in a full-width ruler. Derive the
  column from an absolute `1ch` of the monospace face instead.
- **Missing stylesheets and scripts fail silently.** A `<link>` to a file that does
  not exist produces an unstyled page with no console error a casual check catches.
  Grep every `href`/`src` against the filesystem before judging the design.
- **Dead links are the fastest measure of a site's honesty.** Counting them takes
  one script and predicts almost everything a Provocateur critic will say.
- **A webfont import is a third-party request.** If the page claims anything about
  privacy, a `fonts.googleapis.com` link refutes it in one line.

## Facts about this toolchain

- **exFAT cannot host a Node build.** No hard links, no symlinks. `npm install`
  takes ~12 min instead of ~8 and `next build` dies with
  `EISDIR: illegal operation on a directory, readlink '.../node_modules/next/dist/pages/_app.js'`.
  gm's spool fails the same way. Put Node projects on NTFS (`H:`, or `d:\new folder`).
- **Never pipe a verbose gm dispatch straight to output.** One dispatch produced
  14 MB of stack trace and pushed an already-full C: to 239 MB. Redirect to a file
  and grep it.

## Process notes

- Launch panel seats **three at a time**, each writing its verdict to a file as its
  last action. A verdict is a file, not a return value; a seat that appears to fail
  may still have filed. Check the directory before spending the seat again.
- Give each seat the measured facts in the prompt. Seats that cannot see the
  artifact (no browser in this environment) produce far better verdicts when the
  numbers are handed to them.
