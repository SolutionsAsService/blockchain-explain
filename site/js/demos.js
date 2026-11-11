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
    var blocks = Array.prototype.slice.call(d.querySelectorAll(".blk")), rewritten = 0;
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
    blocks.forEach(function (b) { q(b, "data").addEventListener("input", function () { q(d, "count").textContent = ""; rewritten = 0; rehash(b).then(status); }); });
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


  // 5. proof of work: smallest nonce with SHA-256(data|nonce) starting with k zeros
  document.querySelectorAll('[data-demo="pow"]').forEach(function (d) {
    var btn = q(d, "mine"), busy = false;
    if (!canHash) return;
    btn.addEventListener("click", function () {
      if (busy) return;
      busy = true; btn.disabled = true;
      var data = q(d, "data").value, k = Math.max(1, Math.min(5, Math.floor(+q(d, "zeros").value) || 1)), target = "0".repeat(k), n = 0;
      q(d, "out").textContent = "Mining…";
      function batch() {
        var tries = [];
        for (var b = 0; b < 256; b++) tries.push(sha(data + "|" + (n + b)));
        Promise.all(tries).then(function (hs) {
          for (var b = 0; b < hs.length; b++) {
            if (hs[b].indexOf(target) === 0) {
              q(d, "nonce").textContent = n + b; q(d, "hash").textContent = hs[b];
              q(d, "out").textContent = (n + b + 1).toLocaleString("en") + " guesses for " + k + " zero" + (k > 1 ? "s" : "") + ". Each extra zero needs about 16 times as many.";
              busy = false; btn.disabled = false; return;
            }
          }
          n += hs.length;
          q(d, "nonce").textContent = n;
          setTimeout(batch, 0);
        });
      }
      batch();
    });
  });

  // 6. signing: ECDSA P-256 in the browser (Bitcoin and Ethereum use secp256k1, which Web Crypto lacks)
  document.querySelectorAll('[data-demo="sign"]').forEach(function (d) {
    if (!canHash) return;
    var pair = null, sig = null, alg = { name: "ECDSA", hash: "SHA-256" };
    function hex(buf) { return Array.from(new Uint8Array(buf)).map(function (x) { return x.toString(16).padStart(2, "0"); }).join(""); }
    q(d, "keys").addEventListener("click", function () {
      crypto.subtle.generateKey({ name: "ECDSA", namedCurve: "P-256" }, false, ["sign", "verify"]).then(function (p) {
        pair = p; sig = null;
        return crypto.subtle.exportKey("raw", p.publicKey);
      }).then(function (raw) {
        q(d, "pub").textContent = hex(raw); q(d, "sig").textContent = "none yet";
        q(d, "sign").disabled = false; q(d, "verify").disabled = true;
        q(d, "out").textContent = "New key pair. The private key stays hidden inside your browser; the public key is shown.";
      });
    });
    q(d, "sign").addEventListener("click", function () {
      var m = q(d, "msg").value;
      crypto.subtle.sign(alg, pair.privateKey, enc.encode(m)).then(function (s) {
        sig = s; q(d, "sig").textContent = hex(s); q(d, "check").value = m; q(d, "verify").disabled = false;
        q(d, "out").textContent = "Signed. Now change the transaction below, or leave it, and check.";
      });
    });
    q(d, "verify").addEventListener("click", function () {
      crypto.subtle.verify(alg, pair.publicKey, sig, enc.encode(q(d, "check").value)).then(function (ok) {
        q(d, "out").textContent = ok ? "Valid: this exact transaction was signed by this key." : "Invalid: the transaction is not the one that was signed. A node would reject it.";
      });
    });
  });

  // self-check: the browser's defaults must equal what the build wrote
  if (canHash) setTimeout(function () {
    var bad = Array.prototype.filter.call(document.querySelectorAll("[data-expect]"), function (el) {
      return el.textContent !== el.dataset.expect;
    });
    document.documentElement.dataset.selfcheck = bad.length ? "mismatch" : "ok";
  }, 400);
})();
