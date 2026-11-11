# CARRY-FORWARD: blockchain-explain 2.0

What the 2.0 run left open, for the next run. (Version 1's list is in `CARRY-FORWARD-v1.md`.)

1. **Autheo source.** autheo.com was outside the build session's network, so the case study cites version 1 of this site, not a dated Autheo page. Next run: read Autheo's own current page, quote it with an "as of" date, and re-check the IBC line against it.
2. **Bedrock projection** (Greenberg, R3 note): the bedrock is drawn in perspective under isometric slabs. Draw it as a wide isometric slab.
3. **Two left edges on the home page** (Greenberg, R3 note): the hero sits on the 40 px gutter while the content below sits on the centred 46 rem column.
4. **Escape does not close the mobile menu** (Mace, R2 note): the native `details` element; add a few lines of script if it matters.
5. **og.png is a capture**: rerun `node _src/og.cjs` after any change to the home page; the build fails only if the file is missing, not if it is stale.
6. **Deploy**: connect the repository to Shadw/Vercel; `vercel.json` serves `site/` at https://blockchain-explain.shadw.app.
