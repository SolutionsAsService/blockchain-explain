# R0 premortem: Critic: Evidence (Cairo)

- Anchor used: How Charts Lie (Cairo): a figure is honest only if a reader can trace and reproduce it.
- Observed: `node tools/verify.mjs` passes (it checks links and tags, not figures). There is no `<script>`, so every hash and count is static text.
- Findings:
  - F1 [defect] blockchain-basics.html:398-503: block #125842, the 2026 timestamp, 0000a83f…, 7bf92ac81…, 2,845 and 0000ff92aa… are all invented.
  - F2 [defect] The block, hashing, chain and Merkle sections appear twice (:340-914 repeated at :915-1490).
  - F3 [claim] Chain :694-757: Block 1's hash is never shown, so "Previous: BBB456" cannot be traced.
  - F4 [claim] :874: the root "ABCD892FF" comes from three transactions. Merkle trees prove inclusion; they do not replace storing transactions.
  - F5 [claim] The "0000" hashes imply proof-of-work, but the block carries a validator signature.
  - F6 [claim] index puts CometBFT above Cosmos SDK, while layer0 puts Cosmos SDK on top of CometBFT. Calling Cosmos SDK "Layer 0" is a framing, not a spec.
  - F7 [claim] "Tolerating a minority" is wrong: the bound is fewer than one third of voting power.
  - F8 [premise] autheo.html:905-1002 prints 399/275/124 validator slots and "live" with no source or date. These figures are absent from the evidence file.
  - F9 [claim] Hashes are called "unique"; they are collision-resistant.
- Verdict: OBJECT
- Requested change: F1/F3-F5: compute SHA-256 live from input the reader can edit. F2: print each section once. F6/F7: one stack and the exact fault bound. F8: a source and as-of date for each figure, or remove it. F9: say "collision-resistant". Make verify.mjs fail on any hex string that no code computes.
