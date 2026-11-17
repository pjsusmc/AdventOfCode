# Advent of Code 2015, Day 17: No Such Thing as Too Much
from collections import Counter
from itertools import combinations

with open('input.txt') as f:
    containers = [int(line) for line in f if line.strip()]

TARGET = 150

# For each number of containers r, count the combinations that hold
# exactly TARGET litres. combinations() works by position, so containers
# with the same size are still counted as different containers.
by_size = Counter(
    r
    for r in range(1, len(containers) + 1)
    for combo in combinations(containers, r)
    if sum(combo) == TARGET
)

# Part 1: every valid combination, whatever its size
print(f"Part 1: {sum(by_size.values())}")

# Part 2: how many combinations use the fewest containers
print(f"Part 2: {by_size[min(by_size)]}")
