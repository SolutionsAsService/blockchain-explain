# crit_use_krug — R0 (premortem)

- **Anchor used:** Krug, *Don't Make Me Think*: the five-second glance and the trunk test (site ID, page name, sections, "you are here", local nav, search).

- **Observed:** Home 1280x800: H1 "Autheo is a decentralized operating system…" plus two CTAs above the fold. Home 390x844: nav wraps ("Layer 0" alone on row 2); primary button clipped at the bottom edge. blockchain-basics.html: brand "Understanding Autheo" (home: "Autheo Explained"), not a link; all four nav links identical in colour/weight (aria-current invisible); "Skip to content" permanently visible top-left; H2 run "Understanding Blocks … What Is A Merkle Tree?" appears twice (y≈3504, y≈8249); no search, 2 in-page anchors on 26,405 px.

- **Findings:**
  - F1 [claim] Home passes five seconds at 1280.
  - F2 [defect] At 390 the first action is below the fold.
  - F3 [defect] Trunk test fails: no visible "you are here", site ID not clickable.
  - F4 [defect] Two names, logos, headers: four pages read as two sites.
  - F5 [defect] Block/hash/Merkle section printed twice.
  - F6 [defect] Unhidden skip link looks like a bug.
  - F7 [defect] 26k-px page with no local navigation.

- **Verdict:** OBJECT

- **Requested change:** F1 keep H1 + two CTAs. F2 one-row nav, CTA above fold at 390. F3/F4 one header, one name, logo links home, current item visibly marked. F5 delete duplicate. F6 hide until focus. F7 add section index or split page.
