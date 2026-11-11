# Blockchain, explained

**https://blockchain-explain.shadw.app**

A plain, general guide to how blockchains work: hashes and blocks, keys and signatures, proof of work,
proof of stake and BFT voting, smart contracts, layer 2, bridges, major chains compared, and the risks. The home
page draws every chain as the same stack of four layers on one bedrock, with a bridge between two chains. Every
value on the site is real: the build computes it, and your browser recomputes it when you change the input. You can
break a chain, mine a block and sign a transaction yourself.

| Page | What it covers |
|---|---|
| Basics | Hashes, the chain and Merkle trees, each a live demo |
| Keys | Private and public keys, wallets, signing (live demo) |
| Consensus | Proof of work (mine a block), proof of stake, BFT voting (calculator) |
| Contracts | Smart contracts, the EVM, gas |
| Layer 2 | Rollups and payment channels |
| Bridges | Trusted bridges and light-client bridges (IBC) |
| Chains | Bitcoin, Ethereum, Cosmos Hub and Solana compared; an Autheo case study |
| Risks | Lost keys, scams, contract bugs, bridges, majority attacks, energy |
| Glossary | 20 terms |

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
