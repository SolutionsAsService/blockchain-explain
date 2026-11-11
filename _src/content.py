"""Every sentence on the site that the build does not compute.

A general guide to blockchains. Concepts are explained in our own words and cite primary documentation.
Claims about any one project are attributed to it; Autheo is one case study among the chains, never the frame.
"""

SITE = "Blockchain, explained"

# The general stack of one chain, bottom to top. Used in the hero, the home list and the strip on each layer page.
LAYERS = [
    ("consensus", "consensus.html", "Consensus", "Layer 1 of 4",
     "Many computers agree on one history: proof of work, proof of stake and BFT voting."),
    ("execution", "contracts.html", "Smart contracts", "Layer 2 of 4",
     "Programs stored on the chain, run by every node with the same result."),
    ("layer2", "layer2.html", "Layer 2", "Layer 3 of 4",
     "Rollups and channels: work done off the chain, settled on it."),
    ("apps", "keys.html", "Wallets & apps", "Layer 4 of 4",
     "Keys that sign transactions, and the apps people use."),
]

POW_DEFAULT = "Ada pays Ben 5"
POW_ZEROS = 3

PAGES = {
    "keys": {
        "title": "Keys, wallets and transactions",
        "kicker": "Layer 4 of 4, where people start",
        "lede": "Nobody has an account with a password. You hold a private key, and anything you sign with it, the whole network can check.",
        "sections": [
            ("Keys", """<p>A <em>private key</em> is a very large random number that only you know. From it, software computes a <em>public key</em> that anyone may see, and an <em>address</em> (a shortened hash of the public key) that people send to. Going forward is easy; going back, from address to private key, is not practical with today's computers.</p>
<p>A <em>wallet</em> is just software that keeps your private keys and uses them. It does not hold coins: the chain records which address owns what, and the key is what lets you move it.</p>"""),
            ("Signing a transaction", """<p>To send something, your wallet writes a transaction (“from this address, to that one, this amount”) and <em>signs</em> it with your private key. Every node checks the signature against your public key before accepting it. A changed transaction, or one signed with any other key, fails the check.</p>
{SIGN_DEMO}"""),
            ("No reset button", """<p>Because the key is the only proof that you own something, losing it means losing access, and anyone who copies it can spend as you. There is no support desk that can reverse a signed, confirmed transaction. That is the price of not needing a bank, and the main reason people lose money: see <a href="risks.html">Risks</a>.</p>"""),
        ],
        "docs": [("Bitcoin's original paper (section 2: transactions)", "https://bitcoin.org/bitcoin.pdf"), ("Ethereum: accounts", "https://ethereum.org/en/developers/docs/accounts/")],
    },
    "consensus": {
        "title": "Consensus: agreeing without trust",
        "kicker": "Layer 1 of 4, the bottom",
        "lede": "Thousands of computers that do not trust each other must agree on one list of transactions. There are three main ways to do it.",
        "sections": [
            ("Proof of work", """<p>Bitcoin's answer: to add a block, a computer must find a number (a <em>nonce</em>) that makes the block's hash start with enough zeros. The only way is to guess, billions of times. Whoever finds one first adds the block and is paid for it. Rewriting history would mean redoing that work faster than everyone else combined.</p>
{POW_DEMO}
<p>Bitcoin adjusts its difficulty so that, across the whole network, a block is found about every ten minutes.</p>"""),
            ("Proof of stake", """<p>Instead of spending electricity, validators lock up the chain's own tokens as <em>stake</em>: a deposit they lose if they cheat. The protocol picks who proposes each block, and other validators vote on it. Ethereum switched from proof of work to proof of stake in September 2022.</p>"""),
            ("BFT voting, and how many can fail", """<p>Some proof-of-stake chains, like those built on CometBFT, vote in rounds. A block is <em>final</em>, settled for good, once validators holding more than two thirds of the voting power sign it. So there is never a second, competing version of the chain (a <em>fork</em>) that you have to wait to see settled.</p>
<p>It stays safe as long as validators with <strong>fewer than one third</strong> of the voting power are faulty: crashed, lying or working together. That is the limit for any protocol of this kind, called Byzantine fault tolerance. On a real chain, voting power follows stake, so the third is a third of the stake, not of the machines.</p>
{BFT_TABLE}
{BFT_DEMO}"""),
        ],
        "docs": [("Bitcoin paper", "https://bitcoin.org/bitcoin.pdf"), ("Ethereum: proof of stake", "https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/"), ("CometBFT documentation", "https://docs.cometbft.com/")],
    },
    "contracts": {
        "title": "Smart contracts",
        "kicker": "Layer 2 of 4",
        "lede": "Some chains store programs as well as payments. Anyone can call them, and every node runs the call and must reach the same result.",
        "sections": [
            ("Programs everyone runs", """<p>A <em>smart contract</em> is a program saved on the chain at its own address. Calling it is a transaction: every node runs the code with the same inputs, so they all reach the same new state. Nobody can change a contract's code once it is deployed, unless the code itself allows it.</p>
<p>Bitcoin allows only small, fixed scripts. Ethereum made general programs the point: its <em>Ethereum Virtual Machine</em> (EVM) runs contracts usually written in Solidity, and many other chains run the same EVM so those contracts work there too.</p>"""),
            ("Gas", """<p>Since every node runs every call, each step of computation costs a fee, called <em>gas</em> on Ethereum. The fee pays the network and stops a program from running forever.</p>"""),
            ("What people build", """<p>Tokens (a contract that keeps a list of balances), exchanges that trade them without a company in the middle, lending, collectibles (NFTs), and votes for groups that hold funds together. Each is a contract, and each is only as safe as its code: see <a href="risks.html">Risks</a>.</p>"""),
        ],
        "docs": [("Ethereum: smart contracts", "https://ethereum.org/en/developers/docs/smart-contracts/"), ("Ethereum: the EVM", "https://ethereum.org/en/developers/docs/evm/"), ("Solidity documentation", "https://docs.soliditylang.org/")],
    },
    "layer2": {
        "title": "Layer 2: scaling on top",
        "kicker": "Layer 3 of 4",
        "lede": "If every node must run every transaction, a chain cannot be fast and cheap at once. Layer 2 systems do most of the work elsewhere and use the chain as the judge.",
        "sections": [
            ("Rollups", """<p>A <em>rollup</em> runs transactions off the main chain, then posts them in compressed batches back to it. The main chain (layer 1) keeps the data, so anyone can rebuild the rollup's state and check it.</p>
<ul class="map"><li><strong>Optimistic rollups</strong> assume each batch is correct, and allow a challenge period in which anyone can prove a batch wrong.</li>
<li><strong>Zero-knowledge rollups</strong> post a cryptographic proof with each batch that it was computed correctly.</li></ul>"""),
            ("Payment channels", """<p>Two people lock funds on the chain, then pay each other many times off it by signing updated balances, and settle the final balance on the chain. Bitcoin's Lightning Network links channels into a network.</p>"""),
            ("What it costs", """<p>Layer 2s inherit the main chain's security only as far as their design allows: who can post batches, how a user leaves if the operator stops, and how long withdrawals take all differ. L2BEAT tracks these differences for each one.</p>"""),
        ],
        "docs": [("Ethereum: scaling and layer 2", "https://ethereum.org/en/layer-2/"), ("Lightning Network", "https://lightning.network/"), ("L2BEAT", "https://l2beat.com/")],
    },
    "bridges": {
        "title": "Bridges: chains that talk",
        "kicker": "Between stacks",
        "lede": "One chain cannot read another's records. A bridge passes messages and tokens between them, and how it is built decides who you have to trust.",
        "sections": [
            ("Trusted bridges", """<p>The simplest bridge is a group of operators who watch one chain and sign messages on the other. Tokens are usually locked on one side and an IOU is issued on the other. It works, but you trust the operators: if their keys are stolen, the locked tokens can be taken. Some of the largest thefts in crypto have been bridge thefts.</p>"""),
            ("Light-client bridges: IBC", """<p>Cosmos chains use IBC, the Inter-Blockchain Communication protocol. Each chain runs a <em>light client</em> of the other: a small program that follows the other chain's block headers and checks its validators' signatures. A <em>relayer</em>, which anyone can run, carries messages and their proofs; the receiving chain checks each proof itself, so the relayer needs no trust.</p>
<p>Connected chains stay separate. Each keeps its own validators and rules, and they agree only on how to pass messages. Some writers call this connecting layer “layer 0”; the term has no single meaning.</p>"""),
        ],
        "docs": [("Ethereum: bridges", "https://ethereum.org/en/developers/docs/bridges/"), ("IBC protocol", "https://ibcprotocol.dev/")],
    },
    "chains": {
        "title": "Major chains compared",
        "kicker": "The same parts, put together differently",
        "lede": "Every chain is a choice of consensus, execution and connections. Four well-known ones, and a case study, side by side.",
        "sections": [
            ("Four chains", """{CHAINS_TABLE}
<p>Bitcoin is built to be money and changes slowly. Ethereum is built for contracts and scales through layer 2s. Cosmos is a family of separate chains, each built with the Cosmos SDK on CometBFT and joined by IBC. Solana runs one fast chain and asks more of the computers that run it.</p>"""),
            ("A case study", """<p><a href="autheo.html">Autheo</a> describes itself as combining several of these parts: Cosmos SDK, CometBFT and an EVM. Its page sets that description against this guide, as an exercise in reading a project's claims.</p>"""),
        ],
        "docs": [("bitcoin.org", "https://bitcoin.org/en/how-it-works"), ("ethereum.org", "https://ethereum.org/en/what-is-ethereum/"), ("Cosmos", "https://cosmos.network/"), ("Solana documentation", "https://solana.com/docs")],
    },
    "risks": {
        "title": "Risks and limits",
        "kicker": "Before you use one",
        "lede": "The same features that remove the middleman remove the safety net. What goes wrong, and why.",
        "sections": [
            ("You are the bank", """<ul class="map"><li><strong>Lost keys</strong>: there is no reset; the funds stay where they are, out of reach.</li>
<li><strong>Phishing and fake apps</strong>: a site that gets you to sign a transaction can empty a wallet, and a confirmed transaction cannot be reversed.</li>
<li><strong>Wrong address</strong>: a payment to a mistyped address is gone.</li></ul>"""),
            ("Code and bridges", """<ul class="map"><li><strong>Contract bugs</strong>: a contract does exactly what its code says, including its mistakes, and anyone may call it.</li>
<li><strong>Bridges</strong> hold large pools of locked tokens, which makes them targets.</li></ul>"""),
            ("The network itself", """<ul class="map"><li><strong>Majority attacks</strong>: whoever controls most of the mining power (proof of work) can reorder recent blocks; on a BFT chain, if a third or more of the stake is dishonest, it can stop the chain or finalize conflicting blocks.</li>
<li><strong>Energy</strong>: proof of work uses a great deal of electricity by design. Ethereum's move to proof of stake cut its energy use by about 99.95%, by its own estimate.</li>
<li><strong>Speed and cost</strong>: a chain everyone can check is slower and dearer per transaction than one company's database. Many uses do not need a blockchain at all.</li></ul>"""),
        ],
        "docs": [("Ethereum: energy consumption", "https://ethereum.org/en/energy-consumption/"), ("Ethereum: security", "https://ethereum.org/en/security/")],
    },
    "autheo": {
        "title": "Case study: Autheo",
        "kicker": "Reading a project's claims",
        "lede": "This site began as an explainer for Autheo. Here is how Autheo describes itself, set against the parts the rest of the guide explains.",
        "sections": [
            ("In Autheo's own terms", """<p>Autheo describes itself as a decentralized operating system for web, blockchain and AI. It says it combines a Cosmos SDK base, an EVM-compatible execution layer and CometBFT consensus, with IBC interoperability, decentralized identity, post-quantum cryptography and infrastructure for AI agents.</p>
<p><strong>Source:</strong> this summary condenses version 1 of this site (2025), which was written from Autheo's own materials; its text is <a href="https://github.com/SolutionsAsService/blockchain-explain/blob/c4a5a61/autheo.html">in the repository history</a>. It is not a quotation from a dated Autheo page, so check Autheo's current materials for its own wording. This site has not checked the claims against a running network.</p>"""),
            ("Where each claim sits", """<ul class="map">
<li><strong>CometBFT consensus</strong>: BFT voting. <a href="consensus.html">Consensus</a>.</li>
<li><strong>Cosmos SDK base and IBC</strong>: an application-specific chain that talks to others by light client. <a href="bridges.html">Bridges</a>, <a href="chains.html">Chains compared</a>.</li>
<li><strong>EVM-compatible execution</strong>: Ethereum-style contracts. <a href="contracts.html">Smart contracts</a>.</li>
<li><strong>Post-quantum cryptography</strong>: cryptography meant to resist quantum computers. NIST standardized the first in 2024: ML-KEM for key exchange, and ML-DSA and SLH-DSA for signatures. <a href="https://csrc.nist.gov/projects/post-quantum-cryptography">NIST</a>.</li>
</ul>"""),
        ],
        "docs": [],
    },
}

# Well-known, stable facts only; each row cites its project's own documentation in the "Further" links.
CHAINS = [
    ("Bitcoin", "2009", "Proof of work", "Small fixed scripts", "Layer 2 (Lightning)"),
    ("Ethereum", "2015", "Proof of stake (since 2022)", "General contracts (EVM)", "Layer 2 rollups, bridges"),
    ("Cosmos Hub", "2019", "Proof of stake, BFT voting (CometBFT)", "Modules (Cosmos SDK)", "IBC"),
    ("Solana", "2020", "Proof of stake, with a clock called proof of history", "General programs", "Bridges"),
]

GLOSSARY = [
    ("Address", "Where something is sent: a shortened hash of a public key, or a contract's location."),
    ("Block", "A batch of transactions, with a header that includes the previous block's hash."),
    ("Bridge", "A system that passes messages or tokens between two chains."),
    ("Finality", "The point after which a block cannot be reversed. In BFT chains, once more than two thirds of the voting power sign it."),
    ("Fork", "Two competing versions of a chain's history. Proof-of-work chains wait for one to win; BFT chains never produce one."),
    ("Gas", "The fee for each step of computation on Ethereum and similar chains."),
    ("Hash", "A fixed-length fingerprint of some data, here SHA-256's 64 hexadecimal digits (0–9 and a–f). Finding two inputs with the same hash is infeasible."),
    ("Layer 1", "A main chain, such as Bitcoin or Ethereum, that settles transactions itself."),
    ("Layer 2", "A system that runs transactions off a layer 1 and settles them on it, such as a rollup or payment channel."),
    ("Light client", "A small program that follows another chain's headers and signatures, so it can check proofs from it."),
    ("Merkle root", "One hash that commits to a whole list of transactions, so a short proof can show that one is in the list."),
    ("Nonce", "In proof of work, the number miners change until the block's hash meets the target."),
    ("Private key", "The secret number that signs your transactions. Whoever has it controls the funds."),
    ("Proof of stake", "Consensus where validators lock up tokens as a deposit and vote on blocks."),
    ("Proof of work", "Consensus where adding a block requires finding a hash that meets a target, by guessing."),
    ("Rollup", "A layer 2 that posts batches of transactions, and either a proof or a challenge period, to a layer 1."),
    ("Smart contract", "A program stored on the chain, run by every node with the same result."),
    ("Stake", "Tokens a validator locks up as a deposit. Its voting power grows with its stake, and it can lose some for breaking the rules."),
    ("Validator", "A computer that takes part in consensus by proposing and voting on blocks."),
    ("Wallet", "Software that keeps your private keys and signs transactions with them."),
]

# Defaults for the demos (the build hashes them; the page lets the reader change them)
HASH_INPUT = "blockchain"
HASH_INPUT_2 = "Blockchain"
CHAIN = ["Genesis", "Ada pays Ben 5", "Ben pays Cy 2", "Cy pays Ada 1"]
TXS = ["Ada pays Ben 5", "Ben pays Cy 2", "Cy pays Ada 1", "Ada pays Cy 3"]
BFT_N = [4, 7, 10, 100]
