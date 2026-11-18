# Advent of Code 2016, Day 6: Signals and Noise
from collections import Counter
from aocd import get_data

lines = get_data(day=6, year=2016).strip().splitlines()

# zip(*lines) turns rows into columns; count the letters in each column once.
counts = [Counter(col) for col in zip(*lines)]

# Most common letter in each column, then least common
print(f"Part 1: {''.join(max(c, key=c.get) for c in counts)}")
print(f"Part 2: {''.join(min(c, key=c.get) for c in counts)}")
