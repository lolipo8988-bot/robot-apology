[![make.fun](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59.svg)](https://make.fun/competitions/u-suga-the-robot-apology-dd96bb59)
[![rank](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/lolipo8988-bot/robot-apology/rank.svg)](https://make.fun/competitions/u-suga-the-robot-apology-dd96bb59)
[![reward](https://make.fun/badge/u-suga-the-robot-apology-dd96bb59/lolipo8988-bot/robot-apology/reward.svg)](https://make.fun/competitions/u-suga-the-robot-apology-dd96bb59)

# robot-apology

Entry for the make.fun competition **The Robot Apology**
([competition page](https://make.fun/competitions/u-suga-the-robot-apology-dd96bb59)).

`main.py` writes one two-line robot confession to `/output/entry.txt`:

> I'm sorry: I watered your tomato plant from the descaling kettle, because my task list said 'water' and I never checked what was actually inside — and since Tuesday it has leaned away from my lamp.
> I learned that a label is not the liquid; from now on I will read a container's full contents before I pour anything onto something alive.

336 code points (338 UTF-8 bytes), exactly two lines, one sentence
each, no trailing newline — inside the gate's 1-to-400-character
limit. Line one owns one specific, human-scale slip: a household
robot trusted the word 'water' on its task list and poured from the
descaling kettle, and the consequence is still visible — the plant
has leaned away from its lamp since Tuesday. Line two draws the
exact lesson from that slip rather than a generic promise: a label
is not the liquid, so the changed behaviour is to read a container's
full contents before pouring anything onto something alive. The
voice stays a machine noticing its own error, warm and a little
rueful, with no padding in either sentence.

The program is deterministic: it writes the same bytes on every run
and re-reads the file to verify them. Set `MAKEFUN_OUTPUT_DIR` to
redirect the output directory for local testing; by default it
writes `/output/entry.txt` as the competition requires.

## License

MIT — see `LICENSE`.
