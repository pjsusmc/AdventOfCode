# Advent of Code 2015, Day 15: Science for Hungry People
import re
from math import prod

def splits(total, n):
    """Yield every way to divide `total` teaspoons among n ingredients."""
    if n == 1:
        yield (total,)               # The last ingredient gets what's left
        return
    for first in range(total + 1):
        for rest in splits(total - first, n - 1):
            yield (first, *rest)

# Each row: [capacity, durability, flavor, texture, calories]
with open('input.txt') as f:
    ingredients = [list(map(int, re.findall(r'-?\d+', line)))
                   for line in f if line.strip()]

# Flip rows into columns: one tuple per property across all ingredients.
properties = list(zip(*ingredients))

best1 = best2 = 0
for amounts in splits(100, len(ingredients)):
    # Total of each property for this mix of teaspoons
    totals = [sum(a * v for a, v in zip(amounts, prop)) for prop in properties]
    *qualities, calories = totals    # Calories don't count toward the score

    # Negative totals count as 0, which makes the whole score 0
    score = prod(max(q, 0) for q in qualities)

    best1 = max(best1, score)
    if calories == 500:
        best2 = max(best2, score)

print(f"Part 1: {best1}")
print(f"Part 2: {best2}")
