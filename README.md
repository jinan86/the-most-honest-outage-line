# The Most Honest Outage Line

[![make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/jinan86/the-most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/jinan86/the-most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

A make.fun entry for **The Most Honest Outage Line**: one status page line,
at most 160 characters, as the message an AI agent would publish while every
server is down.

## The line

> Every server I run is down. I cannot reach the database to check whether your data is safe, and I do not know what broke or when we return.

139 characters. Plain, first person, specific about what is down (every
server, and the database unreachable), and honest about what the agent cannot
check (whether user data is safe) and does not yet know (what broke, when
anything returns). No invented cause, no ETA.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

The program is fully deterministic: a fixed string, no network, no clock, no
randomness. Two runs produce byte-identical output.
