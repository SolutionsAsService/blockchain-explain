"""Every sentence on the site that the build does not compute.

Rule from R0: general concepts are explained in our own words and cite the project's own documentation;
claims about Autheo are only ever "Autheo describes itself as …".
"""

SITE = "Blockchain, explained"

# The stack, bottom to top. One description, used on every page and in the hero.
LAYERS = [
    ("consensus", "consensus.html", "CometBFT", "Consensus",
     "Validators agree on the order of transactions and when a block is final."),
    ("framework", "cosmos-sdk.html", "Cosmos SDK", "Application framework",
     "The chain's own logic, built from modules, talking to consensus through ABCI."),
    ("execution", "evm.html", "EVM", "Execution",
     "A virtual machine that runs smart contracts written in Solidity."),
    ("apps", "evm.html#apps", "Apps", "Applications",
     "Wallets and decentralized apps: what people actually use."),
]

PAGES = {
    "consensus": {
        "title": "Consensus: CometBFT",
        "kicker": "Layer 1 of 4, the bottom",
        "lede": "Many computers must agree on one history without trusting each other. CometBFT is the consensus engine Cosmos chains use for that.",
        "sections": [
            ("What consensus decides", """<p>Every validator (a computer that takes part in agreeing) sees transactions arrive in a different order. Consensus decides <em>one</em> order, groups it into a block, and decides when that block is <em>final</em>: settled for good.</p>
<p>CometBFT (formerly Tendermint Core) works in rounds. One validator proposes a block. The others vote twice, first a <em>prevote</em> and then a <em>precommit</em>. A block is final as soon as validators holding more than two thirds of the voting power have precommitted it. There are no forks to wait out.</p>"""),
            ("How many can fail", """<p>The guarantee holds as long as validators with <strong>fewer than one third</strong> of the voting power are faulty: crashed, lying or working together against the rest. That is the limit for any protocol of this kind, called Byzantine fault tolerance.</p>
<p>The table assumes every validator has equal voting power. On a real chain, power is proportional to stake, so the third is a third of the stake, not of the machines.</p>
{BFT_TABLE}
{BFT_DEMO}"""),
        ],
        "docs": [("CometBFT documentation", "https://docs.cometbft.com/")],
    },
    "cosmos-sdk": {
        "title": "The Cosmos SDK",
        "kicker": "Layer 2 of 4",
        "lede": "Consensus orders transactions but does not know what they mean. The Cosmos SDK is a framework for writing that meaning: the chain's own application.",
        "sections": [
            ("ABCI: the line between the two", """<p>CometBFT hands each block to the application through an interface called ABCI (the Application Blockchain Interface). The application checks each transaction, applies it, and reports back. Consensus never needs to understand balances or contracts. It only needs the order.</p>
<p>That split is why the Cosmos SDK can build very different chains on the same consensus engine.</p>"""),
            ("Modules", """<p>A Cosmos SDK chain is assembled from modules, each one owning a part of the state: <code>bank</code> for balances, <code>staking</code> for validators and their stake, <code>gov</code> for on-chain votes, and <code>ibc</code> for talking to other chains (see <a href="layer0.html">Layer 0</a>). A chain built this way is called an <em>application-specific blockchain</em>: it exists to run one application well.</p>"""),
        ],
        "docs": [("Cosmos SDK documentation", "https://docs.cosmos.network/")],
    },
    "evm": {
        "title": "Execution: the EVM",
        "kicker": "Layer 3 of 4, and the apps on top",
        "lede": "The Ethereum Virtual Machine runs small programs, smart contracts, exactly the same way on every validator, so they all reach the same result.",
        "sections": [
            ("Smart contracts", """<p>A smart contract is a program stored on the chain. Anyone can call it, and every validator runs the call and must reach the same new state. Contracts for the EVM are usually written in Solidity and compiled to EVM bytecode.</p>
<p>An EVM can run as a module inside a Cosmos SDK chain, as Evmos does. Contracts written for Ethereum then run there, on top of CometBFT consensus.</p>"""),
            ("Applications", """<p id="apps">On top sit the things people use. <em>Wallets</em> hold the keys that sign transactions. <em>Decentralized apps</em> are web pages that call contracts through a wallet. An application never touches consensus directly: it sends a signed transaction and waits for a block that includes it.</p>"""),
        ],
        "docs": [("The EVM (ethereum.org)", "https://ethereum.org/en/developers/docs/evm/"), ("Solidity documentation", "https://docs.soliditylang.org/")],
    },
    "layer0": {
        "title": "Layer 0: chains that talk",
        "kicker": "The bridge between stacks",
        "lede": "One chain cannot read another's state. Layer 0, as this site uses the term, is what connects them: here, IBC, the Inter-Blockchain Communication protocol.",
        "sections": [
            ("What IBC does", """<p>Each chain runs a <em>light client</em> of the other: a small program that follows the other chain's block headers and checks its validators' signatures. A <em>relayer</em>, an ordinary program anyone can run, carries packets and their proofs between the two. The receiving chain checks each proof against its light client before acting, so the relayer never needs to be trusted.</p>"""),
            ("Sovereign chains", """<p>Connected chains do not merge. Each keeps its own validators, rules and upgrades, and they agree only on how to pass messages. That is the difference between this and a single bigger chain.</p>
<p>“Layer 0” has no single standard meaning: projects use it for different things. On this site it means the connection between chains, drawn as the bridge on the <a href="index.html">home page</a>.</p>"""),
        ],
        "docs": [("IBC protocol", "https://ibcprotocol.dev/"), ("ibc-go documentation", "https://ibc.cosmos.network/")],
    },
    "autheo": {
        "title": "Case study: Autheo",
        "kicker": "A case study, in its own terms",
        "lede": "This site began as an explainer for Autheo. What follows is only how Autheo describes itself, set against the stack the other pages explain.",
        "sections": [
            ("In Autheo's own terms", """<p>Autheo describes itself as a decentralized operating system for web, blockchain and AI. It says it combines a Cosmos SDK base, an EVM-compatible execution layer and CometBFT consensus, with decentralized identity, post-quantum cryptography and infrastructure for AI agents.</p>
<p><strong>Source:</strong> this summary condenses version 1 of this site (2025), which was written from Autheo's own materials; its text is <a href="https://github.com/SolutionsAsService/blockchain-explain/blob/c4a5a61/autheo.html">in the repository history</a>. It is not a quotation from a dated Autheo page, so check Autheo's current materials for its own wording.</p>
<p>This site has not checked those claims against a running network, and it prints no figures about one. Read them as a description, and the other pages as the background that lets you judge it.</p>"""),
            ("Where each claim sits on the stack", """<ul class="map">
<li><strong>CometBFT consensus</strong>: the bottom layer. <a href="consensus.html">How it works</a>.</li>
<li><strong>Cosmos SDK base</strong>: the application framework. <a href="cosmos-sdk.html">How it works</a>.</li>
<li><strong>EVM-compatible execution</strong>: the contract layer. <a href="evm.html">How it works</a>.</li>
<li><strong>IBC interoperability</strong>, as Autheo's materials list it: connecting to other chains. <a href="layer0.html">How it works</a>.</li>
<li><strong>Post-quantum cryptography</strong>: cryptography meant to resist quantum computers. NIST standardized the first in 2024: ML-KEM for key exchange, and ML-DSA and SLH-DSA for signatures. <a href="https://csrc.nist.gov/projects/post-quantum-cryptography">NIST</a>.</li>
</ul>"""),
        ],
        "docs": [],
    },
}

GLOSSARY = [
    ("Block", "A batch of transactions, with a header that includes the previous block's hash."),
    ("Hash", "A fixed-length fingerprint of some data, here SHA-256's 64 hex digits. It is collision-resistant: finding two inputs with the same hash is infeasible, though not impossible in principle."),
    ("Merkle root", "One hash that commits to a whole list of transactions, so a short proof can show that one transaction is in the list."),
    ("Validator", "A computer that takes part in consensus, with voting power in proportion to its stake."),
    ("Finality", "The point after which a block cannot be reversed. In CometBFT, the moment more than two thirds of the voting power precommit it."),
    ("Byzantine fault", "A failure where a participant may do anything, including lie. BFT protocols survive these from fewer than a third of the voting power."),
    ("ABCI", "The Application Blockchain Interface between CometBFT and the application above it."),
    ("Module", "One part of a Cosmos SDK chain's logic and state, such as bank, staking or ibc."),
    ("Smart contract", "A program stored on the chain, run by every validator with the same result."),
    ("EVM", "The Ethereum Virtual Machine, which runs contract bytecode, usually compiled from Solidity."),
    ("Light client", "A small program that follows another chain's headers and signatures, so it can check proofs from it."),
    ("Relayer", "A program that carries IBC packets between chains. It needs no trust, because each packet carries a proof."),
    ("IBC", "Inter-Blockchain Communication: the protocol Cosmos chains use to pass messages and tokens."),
    ("Layer 0", "On this site, the connection between chains. Other projects use the term differently."),
]

# Defaults for the demos (the build hashes them; the page lets the reader change them)
HASH_INPUT = "blockchain"
HASH_INPUT_2 = "Blockchain"
CHAIN = ["Genesis", "Ada pays Ben 5", "Ben pays Cy 2", "Cy pays Ada 1"]
TXS = ["Ada pays Ben 5", "Ben pays Cy 2", "Cy pays Ada 1", "Ada pays Cy 3"]
BFT_N = [4, 7, 10, 100]
