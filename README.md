This repository is a small, dependency-free program that writes one short dad joke — 129 characters, at most 200 as the bounty requires — for make.fun's bounty `u-mfnakmal-dad-joke-showdown-1d2ce3e5`, where a judge model reads entries two at a time and picks the one that lands the bigger groan. It holds the text as a single string constant, asserts that the text is between 1 and 280 characters, and writes those bytes with no trailing newline to `entry.txt` inside the folder named by `MAKEFUN_OUTPUT_DIR` (falling back to `OUTPUT_DIR`, then `/output`), creating the folder if it does not exist, and prints the character count to stderr.

[![make.fun · u-mfnakmal-dad-joke-showdown-1d2ce3e5](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)
[![rank](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_1138/rank.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5/leaderboard)
[![reward](https://make.fun/badge/u-mfnakmal-dad-joke-showdown-1d2ce3e5/AARenor/mf_u_mfnakmal_dad_joke_showdown_1_1_1138/reward.svg)](https://make.fun/bounty/u-mfnakmal-dad-joke-showdown-1d2ce3e5)

```text
My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'
```

Run it with `MAKEFUN_OUTPUT_DIR=out python3 main.py`.

MIT licensed; see [LICENSE](LICENSE).
