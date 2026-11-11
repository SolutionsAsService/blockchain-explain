// The same SHA-256 rules as _src/build.py, run with Web Crypto so the reader can change the inputs.
(function () {
  "use strict";
  var enc = new TextEncoder();
  function sha(s) {
    return crypto.subtle.digest("SHA-256", enc.encode(s)).then(function (b) {
      return Array.from(new Uint8Array(b)).map(function (x) { return x.toString(16).padStart(2, "0"); }).join("");
    });
  }
  function q(el, r) { return el.querySelector('[data-role="' + r + '"]'); }
  function qa(el, r) { return Array.prototype.slice.call(el.querySelectorAll('[data-role="' + r + '"]')); }
  function short(h) { return h.slice(0, 12) + "…"; }
  var canHash = !!(window.crypto && crypto.subtle);

  // 1. hash
  document.querySelectorAll('[data-demo="hash"]').forEach(function (d) {
    var inp = q(d, "in"), out = q(d, "out");
    function run() { sha(inp.value).then(function (h) { out.textContent = h; }); }
    if (canHash) { inp.addEventListener("input", run); run(); }
  });

  // 2. chain: hash = SHA-256(number|previous|data)
  document.querySelectorAll('[data-demo="chain"]').forEach(function (d) {
    var blocks = Array.prototype.slice.call(d.querySelectorAll(".blk"));
    function status() {
      var live = q(d, "live"), first = -1;
      blocks.forEach(function (b, i) {
        var ok = i === 0 || q(b, "prev").textContent === q(blocks[i - 1], "hash").textContent;
        b.classList.toggle("broken", !ok);
        q(b, "status").textContent = ok ? "linked" : "broken: “previous” no longer matches block " + (i - 1);
        if (!ok && first < 0) first = i;
      });
      var msg = first < 0 ? "" : "Block " + first + " is broken: its previous hash no longer matches block " + (first - 1) + ".";
      if (live.textContent !== msg) live.textContent = msg;
    }
    function rehash(b) {
      var i = +b.dataset.i;
      return sha(i + "|" + q(b, "prev").textContent + "|" + q(b, "data").value).then(function (h) { q(b, "hash").textContent = h; });
    }
    blocks.forEach(function (b) { q(b, "data").addEventListener("input", function () { rehash(b).then(status); }); });
    var rewritten = 0;
    q(d, "relink").addEventListener("click", function () {
      var i = blocks.findIndex(function (b) { return b.classList.contains("broken"); });
      var out = q(d, "count");
      if (i < 0) { out.textContent = rewritten ? "Every link holds again: " + rewritten + " block" + (rewritten > 1 ? "s" : "") + " rewritten to hide your edit." : "Nothing is broken. Edit a block first."; return; }
      q(blocks[i], "prev").textContent = q(blocks[i - 1], "hash").textContent;
      rehash(blocks[i]).then(function () {
        rewritten++; status();
        var more = blocks.some(function (b) { return b.classList.contains("broken"); });
        out.textContent = "Block " + i + " rewritten (" + rewritten + " so far). " + (more ? "Its hash changed, so the break moved to block " + (i + 1) + "." : "Every link holds again, after rewriting " + rewritten + " block" + (rewritten > 1 ? "s" : "") + ".");
      });
    });
    if (canHash) Promise.all(blocks.map(rehash)).then(status);
  });

  // 3. Merkle: leaves SHA-256(tx), parents SHA-256(left hex + right hex), last one duplicated when odd
  document.querySelectorAll('[data-demo="merkle"]').forEach(function (d) {
    var txs = qa(d, "tx"), leaves = qa(d, "leaf"), pairs = qa(d, "pair"), root = q(d, "root");
    function run() {
      Promise.all(txs.map(function (t) { return sha(t.value); })).then(function (lv) {
        lv.forEach(function (h, k) { leaves[k].textContent = short(h); });
        function up(level, depth) {
          if (level.length === 1) { root.textContent = level[0]; return; }
          if (level.length % 2) level = level.concat([level[level.length - 1]]);
          var next = [];
          for (var k = 0; k < level.length; k += 2) next.push(sha(level[k] + level[k + 1]));
          Promise.all(next).then(function (n) {
            if (depth === 0) n.forEach(function (h, k) { if (pairs[k]) pairs[k].textContent = short(h); });
            up(n, depth + 1);
          });
        }
        up(lv, 0);
      });
    }
    if (canHash) { txs.forEach(function (t) { t.addEventListener("input", run); }); run(); }
  });

  // 4. BFT: faulty f = floor((n-1)/3), quorum = floor(2n/3)+1
  document.querySelectorAll('[data-demo="bft"]').forEach(function (d) {
    var n = q(d, "n");
    function run() {
      var v = Math.max(1, Math.min(1000, Math.floor(+n.value) || 1));
      q(d, "f").textContent = Math.floor((v - 1) / 3);
      q(d, "q").textContent = Math.floor((2 * v) / 3) + 1;
    }
    n.addEventListener("input", run);
  });

  // self-check: the browser's defaults must equal what the build wrote
  if (canHash) setTimeout(function () {
    var bad = Array.prototype.filter.call(document.querySelectorAll("[data-expect]"), function (el) {
      return el.textContent !== el.dataset.expect;
    });
    document.documentElement.dataset.selfcheck = bad.length ? "mismatch" : "ok";
  }, 400);
})();
