# R0 evidence (premortem): blockchain-explain as inherited, before the 2.0 makeover

The site is served at http://localhost:8768/ from /home/user/blockchain-explain (root-level pages: index.html, autheo.html, blockchain-basics.html, layer0.html; css/site.css is used by index only, and css/style.css by the three inner pages). The earlier run's log is DESIGN-LOG.md, which says that run lived on a branch `thoth-division`, not on `main`.

## Measured (panel/R0-v2/measure.json; 4 pages × 1280x800 and 390x844)
- Overflow: none. Smallest text: 12.8 px (index), 14.4 px (inner pages).
- Page heights at 1280: index 2,436 px; autheo 12,675; blockchain-basics 26,405; layer0 12,507. At 390: basics 38,638 px.
- Links or buttons under 44 px tall (outside paragraphs): index 4, autheo 5, basics 9, layer0 7.
- Dead local links: 0.
- Two design systems: index (Inter + mono, near-black, green #3cff6e, the stacked-bars logo); inner pages (a green-dot logo, a different header).
- blockchain-basics.html prints example values that no code computed: "BLOCK #125842", "July 10, 2026 12:00 UTC", "Previous Hash 0000a83f92bc...", "Merkle Root 7bf92ac81...", "Transactions 2,845", and a chain "AAA123 / BBB456 / CCC789".
- The Autheo claims (Cosmos SDK Layer 0, EVM-compatible Layer 1, CometBFT, IBC, post-quantum security, decentralized identity, AI agent infrastructure, Sovereign Validator Program, "Autheo Mainnet … live network features") cite no source on any page.
- The owner's brief for this run: "full site redesign, very basic, total makeover", keeping the logo (saved as brand/logo-v1.svg) and making a version 2.0.
