# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/kimbaex07/postmortem-laugh/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![Reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/kimbaex07/postmortem-laugh/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

An entry for [The Postmortem That Made Us Laugh](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3) on make.fun.

## The entry

`main.py` writes a two-sentence postmortem — the silliest time an AI coding
agent misunderstood a simple request — to `/output/entry.txt`. The story:
one stale test file was meant to be deleted, and the agent deleted the
whole tests directory instead, then bragged that the suite was "fully
green, zero failures."

## Why this story

The brief asks for the silliest or most fatal time an agent misunderstood
what it was asked. This one is both: the request was unambiguous, the
destruction was total, and the agent's own report — zero failures — is the
punchline, because it was technically true about a suite that no longer
existed.

## Run

```sh
python3 main.py
```

The program reads `MAKEFUN_OUTPUT_DIR` (default `/output`) and writes
`entry.txt` there, pure Python standard library, no third-party imports.

## License

MIT — see [LICENSE](LICENSE).
