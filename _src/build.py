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
    fy = ys[1]  # framework layer: where IBC lives
    s = [f'<svg class="hero-svg hero-wide" viewBox="0 0 {W} {H}" role="group" aria-labelledby="hw-t">',
         '<title id="hw-t">Two blockchain stacks on one bedrock, joined by an IBC bridge</title>',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>',
         # bedrock
         f'<a href="blockchain-basics.html" class="bedrock" aria-label="The bedrock: blocks, hashes, the chain and Merkle trees. Blockchain basics">'
         f'<polygon points="40,{base + 66} 740,{base + 66} 760,{base + 124} 20,{base + 124}" class="br"/>'
         f'<text x="390" y="{base + 100}" text-anchor="middle" class="br-t">Bedrock: blocks, hashes and Merkle trees → Basics</text></a>',
         a, b,
         # bridge
         f'<a href="layer0.html" class="bridge" aria-label="Layer 0: IBC, the bridge that lets the two chains pass messages">'
         f'<path d="M{205 + hw - 6},{fy + 6} L{575 - hw + 6},{fy + 6}" class="br-line" marker-start="url(#ah)" marker-end="url(#ah)"/>'
         f'<rect x="{390 - 66}" y="{fy - 52}" width="132" height="52" rx="26" class="br-pill"/>'
         f'<text x="390" y="{fy - 21}" text-anchor="middle" class="br-pt">IBC · Layer 0 →</text></a>',
         # chain names
         f'<text x="205" y="{ys[-1] - hh - 18}" text-anchor="middle" class="ch">Chain A</text>',
         f'<text x="575" y="{ys[-1] - hh - 18}" text-anchor="middle" class="ch">Chain B</text>',
         # the transaction path down chain A
         f'<path d="M135,{ys[-1] - hh - 6} L135,{base + 60}" class="tx" marker-end="url(#ah)"/>',
         f'<text x="128" y="{ys[-1] - hh - 2}" text-anchor="end" class="tx-t">a transaction</text>',
         f'<text x="128" y="{ys[-1] - hh + 16}" text-anchor="end" class="tx-t">travels down</text>',
         '</svg>']
    return "".join(s)


def hero_narrow():
    W, H = 360, 490
    hw, hh, t, gap = 128, 50, 18, 84
    base = 355
    a, ys = stack(150, base, hw, hh, t, gap, True, "n", chain_name="Chain A, ")
    fy = ys[1]
    s = [f'<svg class="hero-svg hero-narrow" viewBox="0 0 {W} {H}" role="group" aria-labelledby="hn-t">',
         '<title id="hn-t">A blockchain stack on its bedrock, with an IBC bridge to another chain</title>',
         '<defs><marker id="ahn" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="ahead"/></marker></defs>',
         f'<a href="blockchain-basics.html" class="bedrock" aria-label="The bedrock: blocks, hashes, the chain and Merkle trees. Blockchain basics">'
         f'<polygon points="8,{base + 74} 352,{base + 74} 360,{base + 132} 0,{base + 132}" class="br"/>'
         f'<text x="180" y="{base + 99}" text-anchor="middle" class="br-t">Bedrock: hashes and blocks</text>'
         f'<text x="180" y="{base + 120}" text-anchor="middle" class="br-t">→ Basics</text></a>',
         a,
         f'<a href="layer0.html" class="bridge" aria-label="Layer 0: IBC, the bridge to another chain">'
         f'<path d="M{150 + hw - 4},{fy + 4} L330,{fy + 4}" class="br-line" marker-end="url(#ahn)"/>'
         f'<rect x="332" y="{fy - 40}" width="28" height="96" rx="4" class="stub"/>'
         f'<text x="346" y="{fy + 8}" text-anchor="middle" class="stub-t" transform="rotate(-90 346 {fy + 8})">Chain B</text>'
         f'<rect x="252" y="{fy - 54}" width="78" height="48" rx="10" class="br-pill"/>'
         f'<text x="291" y="{fy - 34}" text-anchor="middle" class="br-pt">IBC →</text>'
         f'<text x="291" y="{fy - 15}" text-anchor="middle" class="br-pt">Layer 0</text></a>',
         f'<path d="M80,{ys[-1] - hh + 22} L80,{base + 66}" class="tx" marker-end="url(#ahn)"/>',
         f'<text x="150" y="{ys[-1] - hh - 14}" text-anchor="middle" class="ch">Chain A</text>',
         f'<text x="8" y="{ys[-1] - hh - 2}" class="tx-t">a transaction</text>',
         f'<text x="8" y="{ys[-1] - hh + 15}" class="tx-t">travels down</text>',
         '</svg>']
    return "".join(s)


# ------------------------------------------------------------------ layout
NAV = [("index.html", "Home"), ("blockchain-basics.html", "Basics"), ("consensus.html", "Consensus"), ("cosmos-sdk.html", "Cosmos SDK"),
       ("evm.html", "EVM"), ("layer0.html", "Layer 0"), ("autheo.html", "Autheo"), ("glossary.html", "Glossary")]


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
{pager(path)}
</main>
<footer class="foot">
  <p><strong>{K.SITE}.</strong> Every hash on this site is SHA-256, computed by the build and recomputed in your browser. <a href="about.html">About</a> · <a href="https://github.com/SolutionsAsService/blockchain-explain">Source</a> · MIT licence.</p>
</footer>
</body>
</html>
"""
    (OUT / path).write_text(doc)


def layer_strip(active_key):
    """The stack, as a row of four, with this page's layer marked."""
    items = "".join(f'<li class="ls-{k}{" on" if k == active_key else ""}"><a href="{h}"{" aria-current=\"true\"" if k == active_key else ""}><span>{e(name)}</span><small>{e(role)}</small></a></li>'
                    for k, h, name, role, _ in reversed(K.LAYERS))
    return f'<nav class="lstrip" aria-label="The stack, top to bottom"><ol>{items}</ol></nav>'


# ------------------------------------------------------------------ pages
def build_home(ex):
    rows = "".join(f'<li class="lrow s-{k}"><a href="{h}"><span class="lr-n">{len(K.LAYERS) - i}</span><span class="lr-t">{e(role)}: {e(name)}</span><span class="lr-l">{e(line)}</span></a></li>'
                   for i, (k, h, name, role, line) in enumerate(reversed(K.LAYERS)))
    f100, q100 = bft(100)
    body = f"""<section class="hero" aria-labelledby="h1">
  <div class="hero-text">
    <p class="kicker">One stack, from the bedrock up</p>
    <h1 id="h1">Blockchain, explained</h1>
    <p class="lede">How a blockchain fits together, layer by layer, and how two chains talk. Every hash on the site is real, and you can change the input yourself.</p>
    <a class="start" href="blockchain-basics.html">Start with the basics →</a>
  </div>
  {hero_wide(ex)}
  {hero_narrow()}
</section>
<section class="wrap">
  <h2>The stack, top to bottom</h2>
  <ol class="lrows">{rows}
    <li class="lrow s-bridge"><a href="layer0.html"><span class="lr-n">↔</span><span class="lr-t">Layer 0: IBC</span><span class="lr-l">The bridge between chains, each keeping its own validators.</span></a></li>
    <li class="lrow s-bedrock"><a href="blockchain-basics.html"><span class="lr-n">0</span><span class="lr-t">Bedrock: the basics</span><span class="lr-l">Blocks, hashes, the chain and Merkle trees: what every layer stands on.</span></a></li>
    <li class="lrow s-case"><a href="autheo.html"><span class="lr-n">?</span><span class="lr-t">Case study: Autheo</span><span class="lr-l">One project's description of itself, set against the stack.</span></a></li>
  </ol>
  <h2>Three facts, computed</h2>
  <ul class="facts">
    <li><code>SHA-256("{e(K.HASH_INPUT)}")</code> begins <code>{ex["h1"][:12]}</code>, and changing one letter gives <code>{ex["h2"][:12]}</code>. <a href="blockchain-basics.html#hash">Try it</a>.</li>
    <li>A chain of {len(K.CHAIN)} blocks ends at <code>{ex["chain"][-1]["hash"][:12]}</code>. Edit any block and the link after it breaks. <a href="blockchain-basics.html#chain">Break it</a>.</li>
    <li>With 100 equal validators, CometBFT finalizes a block once {q100} agree, and stays safe with up to {f100} faulty. <a href="consensus.html">Why</a>.</li>
  </ul>
</section>"""
    page("index.html", None, body, "How a blockchain stack fits together, from hashes to consensus to two chains talking over IBC. Every hash on the site is real, and you can change the input.", active="index.html")


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
    cmp_html = f"""<div class="cmp" role="group" aria-label="Both hashes, the matching digits marked">
    <p><span>{e(K.HASH_INPUT)}</span><code>{marked(h1, h2)}</code></p>
    <p><span>{e(K.HASH_INPUT_2)}</span><code>{marked(h2, h1)}</code></p>
    <p class="cmp-n">{64 - ex["diff"]} of 64 digits match by position (marked); {ex["diff"]} differ.</p></div>"""
    body = f"""<article class="wrap">
  <p class="kicker">The bedrock, under every layer</p>
  <h1>The basics</h1>
  <p class="lede">A blockchain is a list of blocks, each holding the fingerprint of the one before, kept by many computers at once. Three ideas make it work. Each one below runs in your browser.</p>
  <nav class="toc" aria-label="On this page"><a href="#hash">1 · Hashes</a><a href="#chain">2 · The chain</a><a href="#merkle">3 · Merkle trees</a></nav>

  <h2 id="hash">1 · A hash is a fingerprint</h2>
  <p>SHA-256 turns any text into 64 hexadecimal digits. The same input always gives the same hash, and the smallest change gives a completely different one. It is <em>collision-resistant</em>: nobody knows how to find two inputs with the same hash.</p>
  <div class="demo" data-demo="hash">
    <label>Type anything <input type="text" value="{e(K.HASH_INPUT)}" data-role="in"></label>
    <p class="hx big"><span>SHA-256</span><code data-role="out" data-expect="{ex["h1"]}">{ex["h1"]}</code></p>
  </div>
  <p>Changing one letter, <code>{e(K.HASH_INPUT)}</code> to <code>{e(K.HASH_INPUT_2)}</code>, changes almost every digit:</p>
  {cmp_html}

  <h2 id="chain">2 · The chain</h2>
  <p>Each block's hash covers its number, its data and the previous block's hash: <code>SHA-256(number | previous | data)</code>. Change any old block and its hash changes, so the next block's “previous” no longer matches. Edit a block below and watch the link after it break. Press “Re-link” to repair it: that block's hash changes too, so the break moves to the next block. To hide one edit, you must rewrite every block after it.</p>
  <div class="demo" data-demo="chain"><ol class="chain">{chain_html}</ol>
    <p class="sr-only" data-role="live" aria-live="polite"></p>
    <button type="button" data-role="relink">Re-link the broken block</button>
    <p class="relinked" data-role="count" role="status"></p>
    <p class="demo-note">Re-linking is easy here because one person holds every copy. On a real network, the other validators keep the original chain, and <a href="consensus.html">consensus</a> decides which one counts.</p></div>

  <h2 id="merkle">3 · Merkle trees</h2>
  <p>A block's header does not list every transaction. It holds one <em>Merkle root</em>: hash each transaction, hash the hashes in pairs, and repeat until one is left. A short path of hashes then proves that one transaction is in the block, without the whole list.</p>
  <div class="demo" data-demo="merkle">
    <p class="mk-row">Leaves: each transaction and its hash, H(1) to H(4). Pairs: the hash of two leaf hashes joined.</p>
    <div class="mk-tree">{groups}</div>
    <p class="hx big mk-root"><span>Root: H(pairs)</span><code data-role="root" data-expect="{lv[-1][0]}">{lv[-1][0]}</code></p>
  </div>
  <p class="docs">Further: <a href="https://bitcoin.org/bitcoin.pdf">the Bitcoin paper</a>, which put hash chains and Merkle trees to work in a currency, citing Haber and Stornetta's 1991 time-stamping work · <a href="https://csrc.nist.gov/pubs/fips/180-4/upd1/final">FIPS 180-4, the SHA-256 standard</a></p>
</article>"""
    page("blockchain-basics.html", "Basics", body, "Hashes, the chain and Merkle trees, each running in your browser with real SHA-256.", active="blockchain-basics.html", demos=True)


def bft_table():
    rows = "".join(f"<tr><td>{n}</td><td>{bft(n)[1]}</td><td>{bft(n)[0]}</td></tr>" for n in K.BFT_N)
    return f"""<table class="tbl"><caption>Equal voting power</caption><thead><tr><th scope="col">Validators</th><th scope="col">Needed to finalize (more than ⅔)</th><th scope="col">Faulty it can survive (fewer than ⅓)</th></tr></thead><tbody>{rows}</tbody></table>"""


def bft_demo():
    f, q = bft(10)
    return f"""<div class="demo" data-demo="bft"><label>Validators <input type="number" min="1" max="1000" value="10" data-role="n"></label>
<p class="demo-out" role="status">Needed to finalize (more than ⅔): <strong data-role="q">{q}</strong> · faulty it can survive (fewer than ⅓): <strong data-role="f">{f}</strong></p></div>"""


def build_topic(key, ex):
    P = K.PAGES[key]
    lkey = {"consensus": "consensus", "cosmos-sdk": "framework", "evm": "execution"}.get(key)
    secs = ""
    for t, h in P["sections"]:
        secs += f"<h2>{e(t)}</h2>{h.replace('{BFT_TABLE}', bft_table()).replace('{BFT_DEMO}', bft_demo())}"
    docs = " · ".join(f'<a href="{u}">{e(n)}</a>' for n, u in P["docs"])
    strip = layer_strip(lkey) if lkey else ""
    body = f"""<article class="wrap">
  <p class="kicker">{e(P["kicker"])}</p>
  <h1>{e(P["title"])}</h1>
  {strip}
  <p class="lede">{e(P["lede"])}</p>
  {secs}
  {f'<p class="docs">Further: {docs}</p>' if docs else ''}
</article>"""
    path = {"layer0": "layer0.html", "autheo": "autheo.html"}.get(key, f"{key}.html")
    page(path, P["title"], body, P["lede"], active=path, demos=(key == "consensus"))


def build_glossary():
    items = "".join(f'<div class="gl"><dt id="{re.sub("[^a-z0-9]+", "-", t.lower()).strip("-")}">{e(t)}</dt><dd>{e(d)}</dd></div>' for t, d in K.GLOSSARY)
    body = f"""<article class="wrap"><p class="kicker">{len(K.GLOSSARY)} terms</p><h1>Glossary</h1><dl class="glossary">{items}</dl></article>"""
    page("glossary.html", "Glossary", body, "The terms this site uses, in plain words.", active="glossary.html")


def build_about(ex):
    body = f"""<article class="wrap"><p class="kicker">Version 2.0</p><h1>About this site</h1>
<p class="lede">A plain explainer of the blockchain stack. Version 2.0 rebuilds an earlier site about Autheo. Its numbers were typed by hand, so this version computes them.</p>
<h2>How the numbers are made</h2>
<p><code>_src/build.py</code> computes every hash on the site with Python's SHA-256 and writes it into the pages. In your browser, <code>js/demos.js</code> recomputes the same values with Web Crypto, so when you change an input, the result is real. The two must agree: on load the page checks its own defaults against the values the build wrote.</p>
<h2>The logo</h2>
<p>Version 1 was three bars, the lowest one green. Version 2.0 turns them into three slabs of the stack, with the green base and a transaction's path running down through them. Both are in the repository, in <code>brand/</code>.</p>
<h2>Sources</h2>
<p>Each page links the documentation it rests on. What Autheo says about itself is quoted only as that: <a href="autheo.html">the case study</a>.</p></article>"""
    page("about.html", "About", body, "How the site is built, and its logo 2.0.", active=None)


def build_404():
    page("404.html", "Not found", '<article class="wrap"><p class="kicker">hash mismatch</p><h1>404</h1><p class="lede">This page is not in the chain. <a href="index.html">Back to the home page</a>.</p></article>', "Page not found.")


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
          "chain": chain_blocks(K.CHAIN), "merkle": merkle(K.TXS)}
    for f in OUT.glob("*.html"):
        f.unlink()
    build_home(ex)
    build_basics(ex)
    for key in K.PAGES:
        build_topic(key, ex)
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
