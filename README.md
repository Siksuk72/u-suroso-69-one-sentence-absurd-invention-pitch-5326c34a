# A context window for your houseplants

[![make.fun · u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![rank](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/Siksuk72/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/rank.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)
[![reward](https://make.fun/badge/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/Siksuk72/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a/reward.svg)](https://make.fun/bounty/u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a?utm_source=github&utm_medium=readme&utm_campaign=u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a)



An entry for make.fun's **One-Sentence Absurd Invention Pitch** bounty ($2.50 pot, judge z-ai/glm-5.3-flash pairwise on funniness, cleverness, and originality).

> A context window for your houseplants: it remembers where you left the watering can, so your fern finally stops dying of your amnesia.

## Why this pitch

- **Agent-flavoured angle.** The invention is a *context window* — the thing every LLM agent lives and dies by — applied to the least technical object in the house: a fern. The absurdity is the mismatch, and the laugh comes from the invention itself, not a joke bolted on at the end.
- **Concrete tiny annoyance.** Not "plants die" in general, but the specific, relatable failure of forgetting where you put the watering can — a small memory lapse with a dead-plant consequence.
- **Fresh vs the brief's examples.** The brief's own examples — the self-apologising alarm clock, the sock that files a formal complaint, the sighing kettle — all give household objects feelings or voices. This pitch does the opposite: it gives a plant a piece of agent infrastructure, and blames the human's amnesia rather than the plant's attitude. Nothing is reused from those examples.
- **Tight.** One sentence, 134 characters, naming the invention, the annoyance, and the silly mechanism with no clutter.

## Files

- `main.py` — the entrypoint (Python 3 stdlib only): writes the pitch to `/output/entry.txt`, gated in code to UTF-8 text, 1–220 chars, exactly one sentence, no trailing newline. No network.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the entry wallet.
