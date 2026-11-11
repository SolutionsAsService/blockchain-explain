| Critic | Anchor used | Observed in the work | Verdict PASS/OBJECT | Requested change |
|---|---|---|---|---|
| Critic: Evidence (Cairo) | How Charts Lie (Alberto Cairo): a claim is only as honest as its scope; an absolute stated where the truth is conditional misleads, even when every number is right | Dates (Bitcoin 2009, Ethereum 2015, Merge Sept 2022, Cosmos Hub 2019, Solana 2020), the ten-minute target, the BFT bound and table (n=4/7/10/100 -> f=1/2/3/33, quorum 3/5/7/67), the "a third or more can stop the chain" statement, the ~99.95% figure (attributed to ethereum.org), IBC, Lightning, payment channels, P-256 vs secp256k1, NIST 2024 PQC and Haber-Stornetta 1991 are all correct. PoW demo checked: Python finds nonce 1526, SHA-256("Ada pays Ben 5\|1526") = 000e589cc17b...; the page's default, its data-expect and a live Mine click in Chromium all give 1526 / same hash / "1,527 guesses", no console errors. Defects: the glossary says BFT chains "never" fork, which the Risks page contradicts; gas is described as a fee that "pays the network" (the base fee is burned); rollups are said to have L1 "keep" their data (blob data is pruned after about 18 days); the "Layer 1/2 of 4" kickers collide with the industry terms Layer 1 / Layer 2 the glossary defines; the keys page omits recovery phrases and custodial wallets. | OBJECT | Fix D1-D3 (factual); fix D4-D5 (misleading for a beginner); D6-D9 optional precision. |

## Defects

### Real errors (basis for OBJECT)

**D1. Forks under BFT stated as impossible; contradicts the Risks page.**
File: `_src/content.py`, GLOSSARY, "Fork".
Current: "Two competing versions of a chain's history. Proof-of-work chains wait for one to win; BFT chains never produce one."
Replace: "Two competing versions of a chain's history. Proof-of-work chains wait for one to win; BFT chains do not produce one while fewer than a third of the voting power is faulty."

File: `_src/content.py`, PAGES["consensus"], section "BFT voting, and how many can fail".
Current: "So there is never a second, competing version of the chain (a <em>fork</em>) that you have to wait to see settled."
Replace: "So, as long as the rule below holds, there is no second, competing version of the chain (a <em>fork</em>) that you have to wait to see settled."

**D2. Gas conflated with the fee, and the fee said to pay the network.** Gas is a unit of work; the fee is gas used times a price per unit. Since EIP-1559 (2021) the base part of the fee is burned; only the tip goes to the validator. Storage also costs gas, not only computation.
File: `_src/content.py`, PAGES["contracts"], section "Gas".
Current: "Since every node runs every call, each step of computation costs a fee, called <em>gas</em> on Ethereum. The fee pays the network and stops a program from running forever."
Replace: "Since every node runs every call, each step of computation and each piece of storage is measured in units called <em>gas</em> on Ethereum, and the sender pays a fee for every unit used. Part of the fee goes to the validator and, on Ethereum, the rest is burned; and because a call stops when the gas it paid for runs out, no program can run forever."

File: `_src/content.py`, GLOSSARY, "Gas".
Current: "The fee for each step of computation on Ethereum and similar chains."
Replace: "The unit that measures the work a transaction does on Ethereum and similar chains; the fee is the gas used times a price per unit."

**D3. "Keeps the data" overstates rollup data availability.** Since EIP-4844 (March 2024) most rollups post batches as blobs, which Ethereum nodes delete after about 18 days; L1 guarantees the data was published, not that it is kept.
File: `_src/content.py`, PAGES["layer2"], section "Rollups".
Current: "The main chain (layer 1) keeps the data, so anyone can rebuild the rollup's state and check it."
Replace: "The main chain (layer 1) publishes the data for everyone, so anyone who downloads it can rebuild the rollup's state and check it."

### Misleading for a beginner

**D4. Kickers reuse "Layer 1" and "Layer 2" for a different meaning.** The smart-contracts page is labelled "Layer 2 of 4" and the Layer 2 page "Layer 3 of 4", while the glossary defines Layer 1 as a main chain and Layer 2 as rollups and channels. A beginner will read "Layer 2 of 4" on the contracts page as "contracts are a layer 2".
File: `_src/content.py`, LAYERS and PAGES kickers.
Current: "Layer 1 of 4" / "Layer 2 of 4" / "Layer 3 of 4" / "Layer 4 of 4" (and "Layer 1 of 4, the bottom", "Layer 4 of 4, where people start").
Replace: "Level 1 of 4" / "Level 2 of 4" / "Level 3 of 4" / "Level 4 of 4" (and "Level 1 of 4, the bottom", "Level 4 of 4, where people start"), and in `build.py` use "level" wherever the four-part stack is called "layers", keeping "layer 1 / layer 2" only for the industry terms.

**D5. Keys page: "nobody has an account with a password" and "a wallet ... keeps your private keys" leave out custodial wallets and recovery phrases, the two things a beginner meets first.** Most beginners first hold crypto on an exchange that holds the keys for them, and every self-custody wallet shows a 12- or 24-word recovery phrase. This is a real gap.
File: `_src/content.py`, PAGES["keys"], lede.
Current: "Nobody has an account with a password. You hold a private key, and anything you sign with it, the whole network can check."
Replace: "On the chain itself nobody has an account with a password. Whoever holds a private key controls the funds, and anything signed with it, the whole network can check."
File: `_src/content.py`, PAGES["keys"], section "Keys", second paragraph.
Current: "A <em>wallet</em> is just software that keeps your private keys and uses them. It does not hold coins: the chain records which address owns what, and the key is what lets you move it."
Replace: "A <em>wallet</em> is just software that keeps your private keys and uses them. It does not hold coins: the chain records which address owns what, and the key is what lets you move it. Most wallets show you a <em>recovery phrase</em> of 12 or 24 words that can recreate every key: it is the key, so whoever sees it can take everything. If you use an exchange instead, the exchange holds the keys and you hold only a login, so you are trusting the exchange."

### Precision (optional, not OBJECT)

**D6.** File: `_src/content.py`, PAGES["risks"], "The network itself". Exactly one third can halt a BFT chain; finalizing conflicting blocks needs more than a third to double-sign.
Current: "on a BFT chain, if a third or more of the stake is dishonest, it can stop the chain or finalize conflicting blocks."
Replace: "on a BFT chain, a third or more of the stake can stop the chain, and more than a third, by voting twice, can finalize conflicting blocks, though on most chains it loses that stake for it."

**D7.** File: `_src/content.py`, PAGES["layer2"], lede. Solana is fast and cheap with every validator running every transaction; the trade-off is the cost of checking.
Current: "If every node must run every transaction, a chain cannot be fast and cheap at once."
Replace: "If every node must run every transaction, a chain can only go as fast as the computers checking it, so it must choose between speed and letting ordinary computers check it."

**D8.** File: `_src/build.py`, sign_demo note. Bitcoin has also used Schnorr signatures on secp256k1 since Taproot (2021).
Current: "Bitcoin and Ethereum use the same method on a different curve, secp256k1, which browsers do not offer."
Replace: "Ethereum, and most Bitcoin transactions, use the same method on a different curve, secp256k1, which browsers do not offer; newer Bitcoin addresses use Schnorr signatures on that curve."

**D9.** File: `_src/content.py`, PAGES["consensus"], lede. BFT voting is described on the same page as a kind of proof of stake, so "three ways" double-counts.
Current: "There are three main ways to do it."
Replace: "Most chains use proof of work or proof of stake, and many proof-of-stake chains settle blocks by BFT voting."

### Verified correct (no change)
Bitcoin 2009; Ethereum 2015; Merge September 2022; Cosmos Hub 2019; Solana 2020 with proof of history; ten-minute target; BFT f = floor((n-1)/3), quorum = floor(2n/3)+1; "fewer than one third" bound, stake-weighted; ~99.95% (attributed to ethereum.org); optimistic vs ZK rollups; payment channels and Lightning; IBC light clients and trustless relayers; P-256 in Web Crypto, secp256k1 not offered; NIST ML-KEM, ML-DSA, SLH-DSA in 2024; Haber and Stornetta 1991; "each extra zero needs about 16 times as many". PoW default nonce 1526 matches Python and the live demo.
