#!/usr/bin/env python3
"""Build "Blockchain, explained" (blockchain-explain 2.0).

Every hash, root and link on the site is computed here with SHA-256, and the same rules run in the page
(site/js/demos.js, Web Crypto) so a reader can change the input. The build writes site/, then fails on a
dead local link or missing deploy config.   python3 _src/build.py
"""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "site"
sys.path.insert(0, str(Path(__file__).parent))
import content as K  # noqa: E402
import figures as FIG  # noqa: E402

SITE_URL = "https://blockchain-explain.shadw.app"
e = html.escape


def sha(s):
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# ------------------------------------------------------------------ computed examples
def chain_blocks(datas):
    out, prev = [], "0" * 64
    for i, d in enumerate(datas):
        h = sha(f"{i}|{prev}|{d}")
        out.append({"i": i, "data": d, "prev": prev, "hash": h})
        prev = h
    return out


def merkle(txs):
    level = [sha(t) for t in txs]
    levels = [level]
    while len(level) > 1:
        if len(level) % 2:
            level = level + [level[-1]]
        level = [sha(level[k] + level[k + 1]) for k in range(0, len(level), 2)]
        levels.append(level)
    return levels


def bft(n):
    f = (n - 1) // 3          # largest whole number of faulty validators below one third
    quorum = (2 * n) // 3 + 1  # more than two thirds
    return f, quorum


def short(h, n=10):
    return h[:n] + "…"


# ------------------------------------------------------------------ logo
def slab_pts(cx, y, hw, hh, t):
    top = f"{cx - hw},{y} {cx},{y - hh} {cx + hw},{y} {cx},{y + hh}"
    left = f"{cx - hw},{y} {cx},{y + hh} {cx},{y + hh + t} {cx - hw},{y + t}"
    right = f"{cx},{y + hh} {cx + hw},{y} {cx + hw},{y + t} {cx},{y + hh + t}"
    return top, left, right


def logo_mark():
    parts = ['<svg class="logo" viewBox="0 0 40 40" aria-hidden="true">',
             '<rect x="2" y="2" width="36" height="36" rx="5" class="lg-frame"/>']
    for y, cls in ((27, "lg-base"), (19.5, "lg-mid"), (12, "lg-top")):
        t, l, r = slab_pts(20, y, 12, 5, 3)
        parts.append(f'<g class="{cls}"><polygon points="{l}" class="sl-l"/><polygon points="{r}" class="sl-r"/><polygon points="{t}" class="sl-t"/></g>')
    parts.append('<path d="M20 5.5V35" class="lg-path"/></svg>')
    return "".join(parts)


LOGO_COLOURS = {
    "light": {"bg": "#f6f7f4", "frame": "#1b2a22", "path": "#1b2a22",
              "top": ("#cfdcd3", "#b4c6b9", "#9fb5a6"), "mid": ("#86b398", "#6c9b7f", "#5a8a6d"), "base": ("#1a7d47", "#146b3e", "#0f5a33")},
    "dark": {"bg": "#121513", "frame": "#eef1ec", "path": "#eef1ec",
             "top": ("#e8efe9", "#c4d0c7", "#a9b8ad"), "mid": ("#8fc7a5", "#6fa886", "#5b8f70"), "base": ("#2fbf6e", "#1f8a52", "#176b40")},
}


def logo_file(scheme, favicon=False):
    """Logo 2.0 as a standalone SVG with solid fills: v1's frame and three bars, as three slabs, green at the base."""
    c = LOGO_COLOURS[scheme]
    hw, hh, t = (14, 5.5, 3.5) if favicon else (12, 5, 3)
    ys = (28.5, 19.5, 10.5) if favicon else (27, 19.5, 12)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40" width="160" height="160">',
           f'<rect width="40" height="40" rx="{8 if favicon else 6}" fill="{c["bg"]}"/>']
    if not favicon:
        out.append(f'<rect x="2" y="2" width="36" height="36" rx="5" fill="none" stroke="{c["frame"]}" stroke-width="1.2"/>')
    for y, key in zip(ys, ("base", "mid", "top")):
        tp, l, r = slab_pts(20, y, hw, hh, t)
        ft, fl, fr = c[key]
        out.append(f'<polygon points="{l}" fill="{fl}"/><polygon points="{r}" fill="{fr}"/><polygon points="{tp}" fill="{ft}"/>')
    if not favicon:
        out.append(f'<path d="M20 5.5V35" stroke="{c["path"]}" stroke-width="1.2" stroke-dasharray="1.5 2" fill="none"/>')
    return "".join(out) + "</svg>\n"


# ------------------------------------------------------------------ hero
def stack(cx, base_y, hw, hh, t, gap, labels, prefix, href_ok=True, chain_name=""):
    """Four slabs, bottom (consensus) to top (apps); returns svg and the y of each slab."""
    s = []
    ys = [base_y - k * gap for k in range(len(K.LAYERS))]
    # draw from the bottom up so upper slabs sit on top
    for k, (key, href, name, role, line) in enumerate(K.LAYERS):
        y = ys[k]
        top, left, right = slab_pts(cx, y, hw, hh, t)
        lab = (f'<text class="sl-name" x="{cx}" y="{y + hh * 0.42}" text-anchor="middle">{e(name)}</text>' if labels else "")
        aria = f"{chain_name}{role}: {name}. {line}"
        s.append(f'<a href="{href}" class="slab s-{key}" aria-label="{e(aria)}"><polygon points="{left}" class="sl-l"/>'
                 f'<polygon points="{right}" class="sl-r"/><polygon points="{top}" class="sl-t"/>{lab}</a>')
    return "".join(s), ys


def hero_wide(ex):
    W, H = 780, 560
    hw, hh, t, gap = 120, 46, 18, 80
    base = 380
    a, ys = stack(205, base, hw, hh, t, gap, True, "a", chain_name="Chain A, ")
    b, _ = stack(575, base, hw, hh, t, gap, True, "b", chain_name="Chain B, ")
    fy = ys[1]  # execution layer: where bridges pass messages
    s = [f'<svg class="hero-svg hero-wide" viewBox="0 0 {W} {H}" role="group" aria-labelledby="hw-t">',
         '<title id="hw-t">Two blockchains, each a stack of four layers on one bedrock, joined by a bridge</title>',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>',
         # bedrock
         f'<a href="blockchain-basics.html" class="bedrock" aria-label="The bedrock: blocks, hashes, the chain and Merkle trees. Blockchain basics">'
         f'<polygon points="40,{base + 66} 740,{base + 66} 760,{base + 124} 20,{base + 124}" class="br"/>'
         f'<text x="390" y="{base + 100}" text-anchor="middle" class="br-t">Bedrock: blocks, hashes and Merkle trees → Basics</text></a>',
         a, b,
         # bridge
         f'<a href="bridges.html" class="bridge" aria-label="Bridges: how two chains pass messages and tokens">'
         f'<path d="M{205 + hw - 6},{fy + 6} L{575 - hw + 6},{fy + 6}" class="br-line" marker-start="url(#ah)" marker-end="url(#ah)"/>'
         f'<rect x="{390 - 66}" y="{fy - 52}" width="132" height="52" rx="26" class="br-pill"/>'
         f'<text x="390" y="{fy - 21}" text-anchor="middle" class="br-pt">Bridges →</text></a>',
         # chain names
         f'<text x="205" y="{ys[-1] - hh - 18}" text-anchor="middle" class="ch">Chain A</text>',
         f'<text x="575" y="{ys[-1] - hh - 18}" text-anchor="middle" class="ch">Chain B</text>',
         # the transaction path down chain A
         f'<path d="M100,{ys[-1] - 6} L100,{base + 60}" class="tx" marker-end="url(#ah)"/>',
         f'<text x="6" y="{ys[-1] - 32}" class="tx-t">a transaction</text>',
         f'<text x="6" y="{ys[-1] - 12}" class="tx-t">travels down</text>',
         '</svg>']
    return "".join(s)


def hero_narrow():
    W, H = 360, 490
    hw, hh, t, gap = 128, 50, 18, 84
    base = 355
    a, ys = stack(150, base, hw, hh, t, gap, True, "n", chain_name="Chain A, ")
    fy = ys[1]
    s = [f'<svg class="hero-svg hero-narrow" viewBox="0 0 {W} {H}" role="group" aria-labelledby="hn-t">',
         '<title id="hn-t">A blockchain as a stack of four layers on its bedrock, with a bridge to another chain</title>',
         '<defs><marker id="ahn" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>',
         f'<a href="blockchain-basics.html" class="bedrock" aria-label="The bedrock: blocks, hashes, the chain and Merkle trees. Blockchain basics">'
         f'<polygon points="8,{base + 74} 352,{base + 74} 360,{base + 132} 0,{base + 132}" class="br"/>'
         f'<text x="180" y="{base + 99}" text-anchor="middle" class="br-t">Bedrock: blocks, hashes</text>'
         f'<text x="180" y="{base + 120}" text-anchor="middle" class="br-t">and Merkle trees → Basics</text></a>',
         a,
         f'<a href="bridges.html" class="bridge" aria-label="Bridges: how chains pass messages and tokens">'
         f'<path d="M{150 + hw - 4},{fy + 4} L296,{fy + 4}" class="br-line" marker-end="url(#ahn)"/>'
         f'<rect x="298" y="{fy - 22}" width="60" height="56" rx="8" class="stub"/>'
         f'<text x="328" y="{fy + 2}" text-anchor="middle" class="stub-t">Chain</text><text x="328" y="{fy + 22}" text-anchor="middle" class="stub-t">B</text>'
         f'<rect x="262" y="{fy + 42}" width="96" height="44" rx="22" class="br-pill"/>'
         f'<text x="310" y="{fy + 70}" text-anchor="middle" class="br-pt">Bridges →</text></a>',
         f'<path d="M80,{ys[-1] - hh + 22} L80,{base + 66}" class="tx" marker-end="url(#ahn)"/>',
         f'<text x="150" y="{ys[-1] - hh - 14}" text-anchor="middle" class="ch">Chain A</text>',
         f'<text x="8" y="{ys[-1] - hh - 2}" class="tx-t">a transaction</text>',
         f'<text x="8" y="{ys[-1] - hh + 15}" class="tx-t">travels down</text>',
         '</svg>']
    return "".join(s)


# ------------------------------------------------------------------ layout
NAV = [("blockchain-basics.html", "Basics"), ("keys.html", "Keys"), ("consensus.html", "Consensus"), ("contracts.html", "Contracts"),
       ("layer2.html", "Layer 2"), ("bridges.html", "Bridges"), ("chains.html", "Chains"), ("risks.html", "Risks"), ("glossary.html", "Glossary")]
REDIRECTS = {"evm.html": "contracts.html", "cosmos-sdk.html": "chains.html", "layer0.html": "bridges.html"}  # version 2.0 URLs


def pager(path):
    order = [h for h, _ in NAV]
    if path not in order or path == "index.html":
        return ""
    i = order.index(path)
    prev = order[i - 1] if i > 0 else None
    nxt = order[i + 1] if i + 1 < len(order) else None
    lab = dict(NAV)
    out = '<nav class="pager" aria-label="Previous and next">'
    if prev:
        out += f'<a href="{prev}" rel="prev"><small>← Previous</small><span>{lab[prev]}</span></a>'
    if nxt:
        out += f'<a class="nx" href="{nxt}" rel="next"><small>Next →</small><span>{lab[nxt]}</span></a>'
    return out + "</nav>"


def page(path, title, body, desc, active=None, demos=False):
    links = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{l}</a></li>' for h, l in NAV)
    full = K.SITE if title is None else f"{title} · {K.SITE}"
    js = '<script src="js/demos.js" defer></script>' if demos else ""
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(full)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(full)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="{SITE_URL}/og.png">
<meta property="og:site_name" content="{K.SITE}">
<meta name="theme-color" content="#f6f7f4">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/site.css">
{js}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top">
  <a class="brand" href="index.html">{logo_mark()}<span>Blockchain, <em>explained</em></span></a>
  <nav class="nav-wide" aria-label="Site"><ul>{links}</ul></nav>
  <details class="nav-menu"><summary>Menu</summary><nav aria-label="Site menu"><ul>{links}</ul></nav></details>
</header>
<main id="main">
{body}
</main>
<footer class="foot">
  <p><strong>{K.SITE}.</strong> Every hash on this site is SHA-256, computed by the build and recomputed in your browser. <a href="about.html">About</a> · <a href="https://github.com/SolutionsAsService/blockchain-explain">Source</a> · MIT licence.</p>
</footer>
</body>
</html>
"""
    (OUT / path).write_text(doc)


def slug(t):
    return re.sub("[^a-z0-9]+", "-", t.lower()).strip("-")


LEVEL_OF = {"blockchain-basics": "bedrock", "keys": "apps", "consensus": "consensus", "contracts": "execution",
            "layer2": "layer2", "bridges": "bridge"}
WHERE = {"bedrock": "The bedrock, under every level", "bridge": "Between chains", None: "Beyond the stack"}


def doc(path, title, kicker, lede, idea, sections, docs="", figure=None, demos=False, level=None, desc=None, numbered=True, toc_title="On this page"):
    """Every inner page: a sidebar map of the stack with the page's contents, then the article."""
    guide = [h for h, _ in NAV if h != "glossary.html"]
    if path in guide:
        step = f"Step {guide.index(path) + 1} of {len(guide)}"
        kicker = f"{step} · {kicker}" if kicker else step
    toc = "".join(f'<li><a href="#{sid}">{f"<span>{i + 1:02d}</span>" if numbered else ""}{e(t)}</a></li>' for i, (sid, t, _) in enumerate(sections))
    where = next((f"{role}: {name}" for k, _, name, role, _ in K.LAYERS if k == level), WHERE.get(level, WHERE[None]))
    secs = "".join(f'<section class="sec" aria-labelledby="{sid}"><h2 id="{sid}">{f"<span class=num>{i + 1:02d}</span>" if numbered else ""}{e(t)}</h2>{h}</section>'
                   for i, (sid, t, h) in enumerate(sections))
    fig = ""
    if figure:
        svg_, cap = figure
        fig = f'<figure class="fig">{svg_}<figcaption>{e(cap)}</figcaption></figure>'
    body = f"""<div class="doc">
  <aside class="side" aria-label="Where you are">
    <p class="side-where"><span>You are here</span>{e(where)}</p>
    {FIG.mini_stack(K.LAYERS, level)}
    {f'<nav class="side-toc" aria-label="{toc_title}"><p>{toc_title}</p><ol>{toc}</ol></nav>' if len(sections) > 1 else ''}
  </aside>
  <article class="doc-main">
    <header class="doc-head">
      <p class="kicker">{e(kicker)}</p>
      <h1>{e(title)}</h1>
      <p class="lede">{lede}</p>
    </header>
    {f'<p class="idea"><span>In one line</span>{e(idea)}</p>' if idea else ''}
    {fig}
    {secs}
    {f'<p class="docs"><span>Read further</span>{docs}</p>' if docs else ''}
    {pager(path)}
  </article>
</div>"""
    page(path, title, body, desc or re.sub("<[^>]+>", "", lede), active=path, demos=demos)


def build_home(ex):
    f100, q100 = bft(100)
    pw = ex["pow"]
    blurbs = {
        "blockchain-basics.html": ("0", "bedrock", "Hashes, blocks and the chain", "The fingerprints every chain is built from. Break a chain yourself."),
        "keys.html": ("4", "apps", "Keys and wallets", "How you prove a transaction is yours. Sign one yourself."),
        "consensus.html": ("1", "consensus", "Consensus", "How strangers agree on one history. Mine a block yourself."),
        "contracts.html": ("2", "execution", "Smart contracts", "Programs every node runs, and what they cost."),
        "layer2.html": ("3", "layer2", "Layer 2", "Rollups and channels: faster, settled on the chain."),
        "bridges.html": ("↔", "bridge", "Bridges", "How chains pass tokens, and whom you trust."),
        "chains.html": ("≈", "case", "Chains compared", "Bitcoin, Ethereum, Cosmos and Solana side by side."),
        "risks.html": ("!", "risk", "Risks and limits", "Lost keys, scams, bugs and energy, plainly."),
    }
    cards = "".join(f'<li class="card c-{cls}"><a href="{h}"><span class="card-n">{i + 1}</span><span class="card-t">{e(t)}</span><span class="card-l">{e(l)}</span></a></li>'
                    for i, (h, (n, cls, t, l)) in enumerate(blurbs.items()))
    body = f"""<section class="hero" aria-labelledby="h1">
  <div class="hero-text">
    <p class="kicker">A plain guide, from the bedrock up</p>
    <h1 id="h1">Blockchain, explained</h1>
    <p class="lede">What a blockchain is, how strangers agree on one, and how chains connect, one level at a time. Every hash on the site is real, and you can change the input yourself.</p>
    <a class="start" href="blockchain-basics.html">Start with the basics →</a>
  </div>
  {hero_wide(ex)}
  {hero_narrow()}
</section>
<section class="home-sec" aria-labelledby="guide">
  <h2 id="guide">The guide, in reading order</h2>
  <ol class="cards">{cards}</ol>
</section>
<section class="home-sec" aria-labelledby="facts">
  <h2 id="facts">Three facts this site computes</h2>
  <ul class="facts">
    <li><span class="fact-n"><code>{ex["h1"][:8]}…</code></span><span>is how <code>SHA-256("{e(K.HASH_INPUT)}")</code> begins. One capital letter later it begins <code>{ex["h2"][:8]}…</code>.</span><a href="blockchain-basics.html#hash">Try it</a></li>
    <li><span class="fact-n">{pw["nonce"] + 1:,}</span><span>guesses to find a nonce that gives the block “{e(K.POW_DEFAULT)}” a hash starting with {K.POW_ZEROS} zeros.</span><a href="consensus.html#proof-of-work">Mine it</a></li>
    <li><span class="fact-n">{q100} of 100</span><span>equal validators must sign to finalize a BFT block; it survives up to {f100} faulty.</span><a href="consensus.html#bft">Why</a></li>
  </ul>
</section>"""
    page("index.html", None, body, "A plain guide to blockchains: hashes and blocks, keys, proof of work and stake, smart contracts, layer 2, bridges and the risks. Every hash on the site is real.", active="index.html")


def build_basics(ex):
    chain_html = "".join(f"""<li class="blk" data-i="{b["i"]}">
  <div class="blk-h">Block {b["i"]}</div>
  <label>Data <input type="text" value="{e(b["data"])}" data-role="data" aria-label="Block {b["i"]} data"></label>
  <div class="hx"><span>Previous</span><code data-role="prev">{b["prev"]}</code></div>
  <div class="hx"><span>Hash</span><code data-role="hash" data-expect="{b["hash"]}">{b["hash"]}</code></div>
  <p class="blk-s" data-role="status">linked</p>
</li>""" for b in ex["chain"])
    lv = ex["merkle"]
    def tx(k):
        return f'<li><input type="text" value="{e(K.TXS[k])}" data-role="tx" aria-label="Transaction {k + 1}"><code data-role="leaf">{short(lv[0][k], 12)}</code></li>'
    groups = "".join(f"""<div class="mk-pair"><ol class="txs" start="{2 * g + 1}">{tx(2 * g)}{tx(2 * g + 1)}</ol>
      <p class="mk-h"><span>H({2 * g + 1}+{2 * g + 2})</span><code data-role="pair">{short(lv[1][g], 12)}</code></p></div>""" for g in range(len(K.TXS) // 2))
    h1, h2 = ex["h1"], ex["h2"]
    def marked(h, other):
        return "".join(f"<mark>{c}</mark>" if c == o else c for c, o in zip(h, other))
    sections = [
        ("hash", "A hash is a fingerprint", f"""<p>SHA-256 turns any text into 64 hexadecimal digits (the digits 0–9 and the letters a–f). The same input always gives the same hash, and the smallest change gives a completely different one. It is <em>collision-resistant</em>: nobody knows how to find two inputs with the same hash.</p>
<div class="demo" data-demo="hash"><p class="demo-h">Try it · hash anything</p>
  <label>Type anything <input type="text" value="{e(K.HASH_INPUT)}" data-role="in"></label>
  <p class="hx big"><span>SHA-256</span><code data-role="out" data-expect="{h1}">{h1}</code></p>
</div>
<p>One capital letter changes almost every digit. The digits that happen to match, position by position, are marked:</p>
<div class="cmp" role="group" aria-label="Both hashes, the matching digits marked">
  <p><span>{e(K.HASH_INPUT)}</span><code>{marked(h1, h2)}</code></p>
  <p><span>{e(K.HASH_INPUT_2)}</span><code>{marked(h2, h1)}</code></p>
  <p class="cmp-n">{64 - ex["diff"]} of 64 digits match; {ex["diff"]} differ.</p></div>"""),
        ("chain", "Blocks chained by their hashes", f"""<p>Each block's hash covers its number, its data and the previous block's hash: <code>SHA-256(number | previous | data)</code>. Change any old block and its hash changes, so the next block's “previous” no longer matches.</p>
<div class="demo" data-demo="chain"><p class="demo-h">Try it · break the chain</p>
  <p class="demo-note">Edit a block's data. The link after it snaps. “Re&#8209;link” repairs one block at a time, and each repair moves the break down the chain.</p>
  <ol class="chain">{chain_html}</ol>
  <p class="sr-only" data-role="live" aria-live="polite"></p>
  <div class="btns"><button type="button" data-role="relink" disabled>Re-link the broken block</button></div>
  <p class="relinked" data-role="count" role="status"></p>
  <p class="demo-note">Re-linking is easy here because one person holds every copy. On a real network the other computers keep the original, and <a href="consensus.html">consensus</a> decides which one counts.</p></div>"""),
        ("merkle", "Merkle trees: one hash for many", f"""<p>A block's header does not list every transaction. It holds one <em>Merkle root</em>: hash each transaction, hash the hashes in pairs, and repeat until one is left. A short path of hashes then proves that one transaction is in the block, without the whole list.</p>
<div class="demo" data-demo="merkle"><p class="demo-h">Try it · change a transaction, watch the root</p>
  <div class="mk-tree">{groups}</div>
  <p class="hx big mk-root"><span>Root</span><code data-role="root" data-expect="{lv[-1][0]}">{lv[-1][0]}</code></p>
  <p class="hx mk-was" hidden><span>Was</span><code>{lv[-1][0]}</code></p>
</div>"""),
    ]
    docs = '<a href="https://bitcoin.org/bitcoin.pdf">The Bitcoin paper</a>, which put hash chains and Merkle trees to work in a currency, citing Haber and Stornetta (1991) · <a href="https://csrc.nist.gov/pubs/fips/180-4/upd1/final">FIPS 180-4, the SHA-256 standard</a>'
    doc("blockchain-basics.html", "The basics", "The bedrock, under every level",
        "A blockchain is a list of blocks, each holding the fingerprint of the one before, kept by many computers at once. Three ideas make it work, and each one runs in your browser.",
        K.BASICS_IDEA, sections, docs, FIG.chain_fig(ex["chain"]), demos=True, level="bedrock",
        desc="Hashes, the chain and Merkle trees, each running in your browser with real SHA-256.")


def bft_table():
    rows = "".join(f"<tr><td>{n}</td><td>{bft(n)[1]}</td><td>{bft(n)[0]}</td></tr>" for n in K.BFT_N)
    return f"""<table class="tbl"><caption>Equal voting power</caption><thead><tr><th scope="col">Validators</th><th scope="col">Needed to finalize (more than ⅔)</th><th scope="col">Faulty it can survive (fewer than ⅓)</th></tr></thead><tbody>{rows}</tbody></table>"""


def bft_demo():
    f, q = bft(10)
    return f"""<div class="demo" data-demo="bft"><p class="demo-h">Try it · any number of validators</p><label>Validators <input type="number" min="1" max="1000" value="10" data-role="n"></label>
<p class="demo-out" role="status">With <strong data-role="nn">10</strong> validators: <strong data-role="q">{q}</strong> needed to finalize (more than ⅔) · up to <strong data-role="f">{f}</strong> faulty (fewer than ⅓).</p></div>"""


def pow_search(data, zeros):
    n = 0
    while True:
        h = sha(f"{data}|{n}")
        if h.startswith("0" * zeros):
            return {"nonce": n, "hash": h}
        n += 1


def pow_demo(ex):
    pw = ex["pow"]
    return f"""<div class="demo" data-demo="pow" id="pow"><p class="demo-h">Try it · mine a block</p>
<p class="demo-note">The hash is SHA-256 of the data, a bar, and the nonce: <code>data|nonce</code>. The browser tries nonces 0, 1, 2… until the hash starts with enough zeros.</p>
<div class="fields"><label>Block data <input type="text" value="{e(K.POW_DEFAULT)}" data-role="data"></label>
<label class="narrow">Zeros needed (1–4) <input type="number" min="1" max="4" value="{K.POW_ZEROS}" data-role="zeros"></label></div>
<div class="btns"><button type="button" data-role="mine">Mine</button><button type="button" data-role="stop" hidden>Stop</button></div>
<p class="hx"><span>Nonce</span><code data-role="nonce" data-build="{pw["nonce"]}">not yet</code></p>
<p class="hx big"><span>Hash</span><code data-role="hash" data-build="{pw["hash"]}">not yet</code></p>
<p class="demo-out" data-role="out" role="status">Press Mine to start guessing. (The build found it at nonce {pw["nonce"]:,}.)</p></div>"""


def sign_demo():
    return """<div class="demo" data-demo="sign"><p class="demo-h">Try it · sign and check a transaction</p>
<ol class="steps">
<li><label>1 · Transaction <input type="text" value="Ada pays Ben 5" data-role="msg"></label>
<div class="btns"><button type="button" data-role="keys">Make a key pair</button><button type="button" data-role="sign" disabled>Sign it</button></div><p class="hint" data-role="hint1">Make a key pair first.</p></li>
<li><label>2 · Change the transaction if you like, then check <input type="text" value="Ada pays Ben 5" data-role="check"></label>
<div class="btns"><button type="button" data-role="verify" disabled>Check the signature</button></div><p class="hint" data-role="hint2">Sign it first.</p></li>
</ol>
<p class="hx"><span>Public key</span><code data-role="pub">none yet</code></p>
<p class="hx"><span>Signature</span><code data-role="sig">none yet</code></p>
<p class="demo-out" data-role="out" role="status">Runs in your browser. Nothing is sent anywhere.</p>
<p class="demo-note">Your browser signs with ECDSA on the P-256 curve. Bitcoin and Ethereum sign on a different curve, secp256k1, which browsers do not offer (Bitcoin has also used Schnorr signatures on it since 2021).</p></div>"""


def chains_table():
    rows = "".join(f"<tr><th scope=\"row\">{e(n)}</th><td data-l=\"Launched\">{y}</td><td data-l=\"Consensus\">{e(c)}</td><td data-l=\"Programs\">{e(x)}</td><td data-l=\"Scales or connects\">{e(l)}</td></tr>" for n, y, c, x, l in K.CHAINS)
    return f"""<div class="tbl-wrap"><table class="tbl tbl-text"><caption>Launch year of the main network; consensus as of 2026</caption><thead><tr><th scope="col">Chain</th><th scope="col">Launched</th><th scope="col">Consensus</th><th scope="col">Programs</th><th scope="col">Scales or connects by</th></tr></thead><tbody>{rows}</tbody></table></div>"""


def build_topic(key, ex):
    P = K.PAGES[key]
    f100, q100 = bft(100)
    figs = {"keys": FIG.keys_fig(), "consensus": FIG.fork_fig(), "contracts": FIG.contract_fig(), "risks": FIG.risks_fig(),
            "layer2": FIG.rollup_fig(), "bridges": FIG.bridge_fig()}
    sections = []
    for t, h in P["sections"]:
        sid = {"BFT voting, and how many can fail": "bft"}.get(t, slug(t))
        vf = FIG.votes_fig(100, f100, q100)
        h = (h.replace("{VOTES_FIG}", f'<figure class="fig">{vf[0]}<figcaption>{e(vf[1])}</figcaption></figure>').replace("{BFT_TABLE}", bft_table()).replace("{BFT_DEMO}", bft_demo()).replace("{POW_DEMO}", pow_demo(ex))
             .replace("{SIGN_DEMO}", sign_demo()).replace("{CHAINS_TABLE}", chains_table()))
        sections.append((sid, t, h))
    docs = " · ".join(f'<a href="{u}">{e(n)}</a>' for n, u in P["docs"])
    doc(f"{key}.html", P["title"], P["kicker"], e(P["lede"]), P.get("idea"), sections, docs, figs.get(key),
        demos=key in ("consensus", "keys"), level=LEVEL_OF.get(key))


def build_redirects():
    for old, new in REDIRECTS.items():
        (OUT / old).write_text(f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Moved · {K.SITE}</title>
<meta name="viewport" content="width=device-width, initial-scale=1"><link rel="canonical" href="{new}"><meta http-equiv="refresh" content="0; url={new}">
<link rel="stylesheet" href="css/site.css"></head><body><main class="wrap"><p>This page moved: <a href="{new}">{new}</a>.</p></main></body></html>
""")


def build_glossary():
    groups = {}
    for t, d in sorted(K.GLOSSARY, key=lambda x: x[0].lower()):
        groups.setdefault(t[0].upper(), []).append((t, d))
    sections = [(f"g-{L.lower()}", L, "<dl>" + "".join(f'<div class="gl" id="{slug(t)}"><dt>{e(t)}</dt><dd>{e(d)}</dd></div>' for t, d in items) + "</dl>")
                for L, items in groups.items()]
    doc("glossary.html", "Glossary", f"{len(K.GLOSSARY)} terms, in plain words", "Every term the guide uses, in plain words. Each is explained where it first appears, too.",
        None, sections, numbered=False, toc_title="Letters", desc="The terms this site uses, in plain words.")


def build_about(ex):
    sections = [
        ("numbers", "How the numbers are made", "<p><code>_src/build.py</code> computes every hash and count on the site with Python and writes it into the pages. In your browser, <code>js/demos.js</code> recomputes the same values with Web Crypto, so when you change an input, the result is real. On load, each page checks its own defaults against the values the build wrote.</p>"),
        ("logo", "The logo", "<p>Version 1 was three bars in a frame, the lowest one green. Version 2.0 turns them into three slabs of the stack, keeps the green base, and runs a transaction's path down through them. Both are in the repository, in <code>brand/</code>.</p>"),
        ("sources", "Sources", '<p>Each page links the documentation it rests on: the Bitcoin paper, ethereum.org, the CometBFT, IBC and Solana documentation, L2BEAT and NIST. What any one project says about itself is given only as that, as in <a href="autheo.html">the Autheo case study</a>.</p>'),
    ]
    doc("about.html", "About this site", "Version 2.0",
        "A plain guide to how blockchains work, for anyone. Version 1 of this site explained one project, Autheo, with numbers typed by hand. Version 2.0 is a general guide, and it computes every value it shows.",
        None, sections, desc="How the site is built, and its logo 2.0.")


def build_404():
    doc("404.html", "Not in the chain", "404 · hash mismatch", 'This page does not exist. <a href="index.html">Back to the home page</a>.', None, [])


# ------------------------------------------------------------------ checks
def check_links():
    bad = []
    for f in OUT.rglob("*.html"):
        for href in re.findall(r'href="([^"#]+)(?:#[^"]*)?"', f.read_text()):
            if not href.startswith(("http", "mailto:")) and not (f.parent / href).resolve().exists():
                bad.append(f"{f.name} -> {href}")
    return bad


def check_deploy():
    try:
        root = json.loads((ROOT / "vercel.json").read_text())
        inner = json.loads((OUT / "vercel.json").read_text())
        fluid = json.loads((ROOT / "fluid.json").read_text())
    except (OSError, ValueError) as err:
        return [f"deploy config: {err}"]
    ok = (root.get("outputDirectory") == "site" and root.get("fluid") and inner.get("outputDirectory") == "."
          and fluid.get("static_dir") == "site" and SITE_URL.endswith(".shadw.app"))
    return [] if ok else ["deploy config: vercel.json, site/vercel.json and fluid.json must all serve site/"]


def main():
    h1, h2 = sha(K.HASH_INPUT), sha(K.HASH_INPUT_2)
    ex = {"h1": h1, "h2": h2, "diff": sum(a != b for a, b in zip(h1, h2)),
          "chain": chain_blocks(K.CHAIN), "merkle": merkle(K.TXS), "pow": pow_search(K.POW_DEFAULT, K.POW_ZEROS)}
    for f in OUT.glob("*.html"):
        f.unlink()
    build_home(ex)
    build_basics(ex)
    for key in K.PAGES:
        build_topic(key, ex)
    build_redirects()
    build_glossary()
    build_about(ex)
    build_404()
    (OUT / "favicon.svg").write_text(logo_file("dark", favicon=True))
    for scheme, name in (("light", "logo-v2.svg"), ("dark", "logo-v2-dark.svg")):
        (ROOT / "brand" / name).write_text("<!-- Logo 2.0, written by _src/build.py: v1's frame and three bars as three slabs of the stack, the green base kept, a transaction's path through it. -->\n" + logo_file(scheme))
    (OUT / "computed.json").write_text(json.dumps(ex, indent=1) + "\n")
    problems = check_links() + check_deploy() + ([] if (OUT / "og.png").exists() else ["site/og.png missing: run node _src/og.cjs"])
    print(f"built {len(list(OUT.glob('*.html')))} pages; chain tip {ex['chain'][-1]['hash'][:12]}, merkle root {ex['merkle'][-1][0][:12]}")
    if problems:
        print("problems:", *problems, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
