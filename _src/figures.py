"""Explanatory figures, one per topic page, drawn in the logo's language (slabs, green ramp, ink arrows).

Every figure is 360 units wide and drawn top to bottom, so the same SVG reads on a phone (about 340 px) and on a
desktop (capped at 480 px) with text never under 13 px. Values shown are passed in from the build, never typed.
"""
from html import escape as e

W = 360


def _defs(fid):
    return (f'<defs><marker id="{fid}-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            f'<path d="M0,0 L10,5 L0,10 z" class="fg-head"/></marker></defs>')


def svg(fid, h, title, inner):
    return (f'<svg class="fig-svg" viewBox="0 0 {W} {h}" role="img" aria-labelledby="{fid}-t">'
            f'<title id="{fid}-t">{e(title)}</title>{_defs(fid)}{inner}</svg>')


def box(x, y, w, h, lines, cls="fg-box", first_bold=True):
    """A rounded box with centred lines of text: (text, kind) where kind is t (label), m (mono) or s (small)."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" class="{cls}"/>']
    n = len(lines)
    lh = 19
    y0 = y + h / 2 - (n - 1) * lh / 2 + 5
    for i, (txt, kind) in enumerate(lines):
        c = {"t": "fg-t", "m": "fg-m", "s": "fg-s"}[kind]
        out.append(f'<text x="{x + w / 2}" y="{y0 + i * lh}" text-anchor="middle" class="{c}{" on" if cls.endswith("key") else ""}">{e(txt)}</text>')
    return "".join(out)


def arrow(fid, x1, y1, x2, y2, label=None, lx=None, ly=None, anchor="start", dashed=False):
    s = f'<path d="M{x1},{y1} L{x2},{y2}" class="fg-arrow{" dash" if dashed else ""}" marker-end="url(#{fid}-a)"/>'
    if label:
        s += f'<text x="{lx if lx is not None else x1 + 10}" y="{ly if ly is not None else (y1 + y2) / 2 + 5}" text-anchor="{anchor}" class="fg-s">{e(label)}</text>'
    return s


def slab(cx, y, hw, hh, t, cls):
    top = f"{cx - hw},{y} {cx},{y - hh} {cx + hw},{y} {cx},{y + hh}"
    left = f"{cx - hw},{y} {cx},{y + hh} {cx},{y + hh + t} {cx - hw},{y + t}"
    right = f"{cx},{y + hh} {cx + hw},{y} {cx + hw},{y + t} {cx},{y + hh + t}"
    return f'<g class="{cls}"><polygon points="{left}" class="sl-l"/><polygon points="{right}" class="sl-r"/><polygon points="{top}" class="sl-t"/></g>'


# ---------------------------------------------------------------------------------------------- per page
def chain_fig(blocks):
    fid = "f-chain"
    parts, y = [], 8
    for i, b in enumerate(blocks[:3]):
        parts.append(box(40, y, 280, 78, [(f"Block {b['i']}: {b['data']}", "t"), (f"previous {b['prev'][:10]}…", "m"), (f"hash {b['hash'][:10]}…", "m")],
                         "fg-key" if i == 0 else "fg-box"))
        if i < 2:
            parts.append(arrow(fid, 180, y + 78, 180, y + 112, "is the next “previous”", 190, y + 100))
        y += 112
    return svg(fid, y - 26, "Three blocks, each holding the previous block's hash", "".join(parts)), \
        "The first three blocks of the chain demo below. Each block stores the previous block's hash, so the blocks are chained by their fingerprints."


def keys_fig():
    fid = "f-keys"
    p = [box(60, 8, 240, 58, [("Private key", "t"), ("secret: never share it", "s")], "fg-key"),
         arrow(fid, 180, 66, 180, 106, "easy this way, not back", 190, 92),
         box(60, 108, 240, 58, [("Public key", "t"), ("anyone may see it", "s")]),
         arrow(fid, 180, 166, 180, 206, "hashed and shortened", 190, 192),
         box(60, 208, 240, 58, [("Address", "t"), ("where people send to", "s")]),
         box(10, 300, 160, 58, [("Transaction", "t"), ("signed by private key", "s")], "fg-box"),
         arrow(fid, 170, 329, 196, 329),
         box(198, 300, 152, 58, [("Signature", "t"), ("public key checks it", "s")], "fg-box")]
    return svg(fid, 366, "From private key to public key to address, and how a transaction is signed", "".join(p)), \
        "One key pair. Going down the arrows is quick; going back up, from an address to the private key, is not practical."


def votes_fig(n, f, q):
    """A 10 x 10 grid of validators: the faulty ones the chain can survive, and the votes it needs."""
    fid = "f-votes"
    cell, gap, x0, y0 = 26, 4, 30, 8
    p = []
    for k in range(n):
        r, c = divmod(k, 10)
        cls = "fg-bad" if k >= n - f else "fg-good"
        p.append(f'<rect x="{x0 + c * (cell + gap)}" y="{y0 + r * (cell + gap)}" width="{cell}" height="{cell}" rx="4" class="{cls}"/>')
    yb = y0 + 10 * (cell + gap) + 14
    p.append(f'<rect x="{x0}" y="{yb}" width="16" height="16" rx="3" class="fg-good"/><text x="{x0 + 24}" y="{yb + 13}" class="fg-s">{q} needed to finalize (more than ⅔)</text>')
    p.append(f'<rect x="{x0}" y="{yb + 26}" width="16" height="16" rx="3" class="fg-bad"/><text x="{x0 + 24}" y="{yb + 39}" class="fg-s">{f} faulty at most (fewer than ⅓)</text>')
    return svg(fid, yb + 50, f"{n} validators: {q} votes needed to finalize, at most {f} faulty tolerated", "".join(p)), \
        f"{n} validators with equal voting power. A block is final once {q} sign it; the chain stays safe while no more than {f} are faulty. Computed by the build."


def contract_fig():
    fid = "f-call"
    p = [box(60, 8, 240, 52, [("Ada's call", "t"), ("send(Ben, 5)", "m")], "fg-key")]
    xs = [12, 98, 184, 270]
    for i, x in enumerate(xs):
        p.append(arrow(fid, 180, 60, x + 39, 108))
        p.append(box(x, 110, 78, 58, [(f"Node {i + 1}", "t"), ("runs it", "s")]))
        p.append(arrow(fid, x + 39, 168, 100 + i * 53, 216))
    p.append(box(40, 218, 280, 72, [("The same new state", "t"), ("Ada 95 · Ben 105", "m"), ("was Ada 100 · Ben 100", "m")], "fg-key"))
    return svg(fid, 298, "One call, run by every node, giving the same new state", "".join(p)), \
        "Every node runs the same code on the same inputs, so they all reach the same result without trusting each other."


def rollup_fig():
    fid = "f-rollup"
    p = []
    for i in range(10):
        p.append(f'<circle cx="{36 + i * 32}" cy="22" r="11" class="fg-dot"/>')
    p.append('<text x="180" y="56" text-anchor="middle" class="fg-s">many transactions</text>')
    p.append(arrow(fid, 180, 64, 180, 96))
    p.append(box(50, 98, 260, 58, [("Rollup", "t"), ("runs them and packs one batch", "s")], "fg-box"))
    p.append(arrow(fid, 180, 156, 180, 204, "one batch (+ proof if ZK)", 190, 184))
    p.append(slab(180, 240, 130, 30, 14, "s-consensus"))
    p.append('<text x="180" y="247" text-anchor="middle" class="fg-t on">Layer 1</text>')
    p.append('<text x="180" y="304" text-anchor="middle" class="fg-s">keeps the data; checks the proof or a challenge</text>')
    return svg(fid, 314, "Many transactions packed by a rollup into one batch, posted to layer 1", "".join(p)), \
        "A rollup does the work off the main chain and posts compact batches to it; the main chain is the judge."


def bridge_fig():
    fid = "f-bridge"
    p = ['<text x="70" y="20" text-anchor="middle" class="fg-t">Chain A</text>', '<text x="290" y="20" text-anchor="middle" class="fg-t">Chain B</text>',
         '<text x="180" y="52" text-anchor="middle" class="fg-s fg-h">1 · a trusted bridge</text>',
         box(8, 62, 128, 52, [("Lock 5", "t"), ("tokens held", "s")]),
         arrow(fid, 136, 88, 148, 88),
         box(150, 62, 60, 52, [("signers", "s")], "fg-warn"),
         arrow(fid, 210, 88, 222, 88),
         box(224, 62, 128, 52, [("Issue 5", "t"), ("an IOU", "s")]),
         '<text x="180" y="134" text-anchor="middle" class="fg-s">operators sign: you trust their keys</text>',
         '<text x="180" y="178" text-anchor="middle" class="fg-s fg-h">2 · a light-client bridge (IBC)</text>',
         box(8, 188, 128, 52, [("Message", "t"), ("+ proof", "s")]),
         arrow(fid, 136, 214, 222, 214, "relayer", 179, 206, "middle"),
         box(224, 188, 128, 52, [("Light client", "t"), ("checks the proof", "s")], "fg-key"),
         '<text x="180" y="260" text-anchor="middle" class="fg-s">anyone can relay; the receiving chain checks</text>']
    return svg(fid, 270, "Two kinds of bridge: one trusts operators' keys, the other checks proofs with a light client", "".join(p)), \
        "The difference that matters is who checks the message: a group of key holders, or the receiving chain itself."


def mini_stack(levels, active):
    """The sidebar map: four levels on the bedrock, with a bridge; the current page in colour, outlined and pointed at."""
    cx, hw, hh, t, gap, base = 100, 68, 25, 10, 40, 182
    out = ['<svg class="mini" viewBox="0 0 240 268" role="group" aria-label="Where this page sits in the stack">']
    ptr = None
    on = active == "bedrock"
    out.append(f'<a href="blockchain-basics.html" aria-label="Basics, the bedrock"{" aria-current=\"page\"" if on else ""}>'
               f'<rect x="18" y="{base + 32}" width="164" height="44" rx="4" class="mn-bed{" on" if on else ""}"/>'
               f'<text x="100" y="{base + 59}" text-anchor="middle" class="mn-t">Basics</text></a>')
    if on:
        ptr = (4, base + 59)
    for k, (key, href, name, role, line) in enumerate(levels):
        y = base - k * gap
        on = key == active
        out.append(f'<a href="{href}" aria-label="{e(role)}: {e(name)}"{" aria-current=\"page\"" if on else ""}>{slab(cx, y, hw, hh, t, ("s-" + key) if on else "mn-off")}'
                   f'<text x="{cx}" y="{y + 5}" text-anchor="middle" class="mn-t{" on" if on else ""}{" light" if on and key == "consensus" else ""}">{e(name)}</text></a>')
        if on:
            ptr = (4, y + 5)
    on = active == "bridge"
    yb = base - gap
    out.append(f'<a href="bridges.html" aria-label="Bridges, between chains"{" aria-current=\"page\"" if on else ""}>'
               f'<path d="M{cx + hw},{yb + 6} L206,{yb + 6} L206,{yb - 4}" class="mn-br{" on" if on else ""}"/>'
               f'<rect x="176" y="{yb - 48}" width="60" height="44" rx="6" class="mn-bx{" on" if on else ""}"/><text x="206" y="{yb - 21}" text-anchor="middle" class="mn-t{" on" if on else ""}">Bridges</text></a>')
    if ptr:
        out.append(f'<text x="{ptr[0]}" y="{ptr[1]}" class="mn-ptr" aria-hidden="true">▶</text>')
    elif on:
        out.append(f'<text x="206" y="{yb - 54}" text-anchor="middle" class="mn-ptr" aria-hidden="true">▼</text>')
    out.append("</svg>")
    return "".join(out)


def fork_fig():
    """Two competing histories: the honest chain, and a shorter rewrite that must overtake it."""
    fid = "f-fork"
    p = ['<text x="8" y="22" class="fg-s fg-h">the chain everyone has</text>']
    xs = [8, 98, 188, 278]
    for i, x in enumerate(xs):
        p.append(box(x, 32, 74, 44, [(f"Block {i + 1}", "t")], "fg-key"))
        if i:
            p.append(arrow(fid, x - 14, 54, x - 2, 54))
    p.append('<text x="8" y="146" class="fg-s fg-h">a cheater’s</text>')
    p.append('<text x="8" y="166" class="fg-s fg-h">rewrite</text>')
    p.append(arrow(fid, 135, 76, 186, 126, dashed=True))
    p.append(box(188, 128, 74, 44, [("Block 3′", "t")], "fg-bad-box"))
    p.append('<text x="180" y="200" text-anchor="middle" class="fg-s">to win, the rewrite must overtake the chain:</text>')
    p.append('<text x="180" y="220" text-anchor="middle" class="fg-s">proof of work: out-mine everyone else</text>')
    p.append('<text x="180" y="240" text-anchor="middle" class="fg-s">proof of stake: put a deposit at risk</text>')
    return svg(fid, 250, "The honest chain and a shorter cheater’s rewrite branching from block 2", "".join(p)), \
        "Consensus decides which history counts. Each method makes rewriting it cost more than a cheater can pay."


def risks_fig():
    """Where each risk sits on the stack."""
    fid = "f-risk"
    rows = [("Keys & wallets", ("lost keys, phishing,", "wrong address"), "s-apps"), ("Smart contracts", ("bugs that anyone", "can trigger"), "s-execution"),
            ("Bridges", ("big pools of", "locked tokens"), "s-bridge"), ("Consensus", ("majority attacks,", "halts and reorgs"), "s-consensus")]
    p, y = [], 8
    for name, risk, cls in rows:
        p.append(f'<rect x="8" y="{y}" width="140" height="52" rx="8" class="fg-lv {cls}"/>')
        p.append(f'<text x="78" y="{y + 31}" text-anchor="middle" class="fg-t{" light" if cls == "s-consensus" else ""}">{e(name)}</text>')
        p.append(box(160, y, 192, 52, [(risk[0], "s"), (risk[1], "s")], "fg-warn"))
        y += 64
    return svg(fid, y, "Where each risk sits: keys, contracts, bridges and consensus", "".join(p)), \
        "Each part of the stack fails in its own way; the sections below say how."
