# Blockchain, explained

**https://blockchain-explain.shadw.app**

A plain explainer of how a blockchain fits together, drawn as what it is: two stacks of layers
(consensus, the Cosmos SDK, the EVM, apps) on one bedrock of hashes and Merkle trees, joined by an IBC
bridge. One topic per page, and every hash on the site is real SHA-256: computed by the build, and
recomputed in your browser when you change the input. You can break the chain yourself.

| Page | What it covers |
|---|---|
| Basics | Hashes, the chain and Merkle trees, each a live demo |
| Consensus | CometBFT: rounds, finality, and the one-third bound, with a calculator |
| Cosmos SDK | ABCI and modules |
| EVM | Smart contracts and the apps on top |
| Layer 0 | IBC: light clients, relayers, sovereign chains |
| Autheo | A case study, strictly in Autheo's own terms |
| Glossary | 14 terms |

## Build

```bash
python3 _src/build.py
```

Words live in `_src/content.py`; pages, the hero and the computed values in `_src/build.py`. See
[CONTRIBUTING.md](CONTRIBUTING.md). Deployed from `site/` (Shadw/Vercel: `vercel.json`, `site/vercel.json`, `fluid.json`).

## Logo

`brand/logo-v1.svg` is the original mark: a frame and three bars, the lowest green. Logo 2.0
(`brand/logo-v2.svg`, `brand/logo-v2-dark.svg`, written by the build) turns the bars into three slabs of
the stack, keeps the green base, and runs a transaction's path through them.

Design record: [DESIGN-LOG.md](DESIGN-LOG.md) (version 1: `DESIGN-LOG-v1.md`). MIT licence.
