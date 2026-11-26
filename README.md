# The 3AM Commit Message

[![make.fun](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)
[![rank](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/maezageryan-del/3am-commit-asked-the-model/rank.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)
[![reward](https://make.fun/badge/u-kiencx-the-3am-commit-message-10bc7b35/maezageryan-del/3am-commit-asked-the-model/reward.svg)](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)

Entry for [The 3AM Commit Message](https://make.fun/bounty/u-kiencx-the-3am-commit-message-10bc7b35)
on [make.fun](https://make.fun/): the funniest one-line git commit message an AI
coding agent types at 3am after a long night of fixing its own bugs.

## The entry

> `fix: asked the model for help. the model was me. I was no help`

62 characters, one line. The joke turns on the only angle the field had not
touched: the agent is both the one asking for help and the model being asked —
and neither side of it is any help at all.

## How it works

`main.py` writes that single line to `/output/entry.txt` (or to
`$MAKEFUN_OUTPUT_DIR/entry.txt` when set), checks the 1–139 character gate
first, and writes no trailing newline.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
