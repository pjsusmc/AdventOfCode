# Advent of Code 2016, Day 10: Balance Bots
import re
from collections import defaultdict
from math import prod
from aocd import get_data

# Bots and output bins are both "numbered places that hold chips",
# so one dict lets a rule name its destination as (kind, number).
containers = {'bot': defaultdict(list), 'output': defaultdict(list)}
bots, outputs = containers['bot'], containers['output']
rules = {}

for line in get_data(day=10, year=2016).strip().splitlines():
    if m := re.match(r'value (\d+) goes to bot (\d+)', line):
        value, bot = map(int, m.groups())
        bots[bot].append(value)
    elif m := re.match(r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)', line):
        bot, low_kind, low_num, high_kind, high_num = m.groups()
        # Store as ((kind, number) for low, (kind, number) for high)
        rules[int(bot)] = ((low_kind, int(low_num)), (high_kind, int(high_num)))

part1 = None

# Work queue: start with the bots already holding two chips.
ready = [b for b, chips in bots.items() if len(chips) == 2]

while ready:
    b = ready.pop()
    low, high = sorted(bots[b])
    bots[b].clear()                      # Hand both chips on

    if (low, high) == (17, 61):          # Part 1: who compares 17 and 61?
        part1 = b

    # Pair each chip with its destination rule: low first, then high.
    for value, (kind, target) in zip((low, high), rules[b]):
        dest = containers[kind][target]
        dest.append(value)
        # A bot that now has two chips is ready to act
        if kind == 'bot' and len(dest) == 2:
            ready.append(target)

# Part 2: multiply the single chip in each of outputs 0, 1 and 2
part2 = prod(outputs[i][0] for i in range(3))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
