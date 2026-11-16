# Advent of Code 2015, Day 9: All in a Single Night
from itertools import permutations, pairwise

distances = {}
cities = set()

with open('input.txt') as f:
    for line in f:
        if line.strip():
            # Format: "London to Dublin = 464"
            a, _, b, _, dist = line.split()
            distances[a, b] = distances[b, a] = int(dist)  # Same both ways
            cities.update((a, b))

totals = []
for route in permutations(cities):
    # A route and its reverse have the same length, so keep only one
    # of each pair: the one whose first city sorts before its last.
    if route[0] > route[-1]:
        continue
    # pairwise gives consecutive stops: (A, B), (B, C), (C, D), ...
    totals.append(sum(distances[a, b] for a, b in pairwise(route)))

print(f"Part 1: {min(totals)}")
print(f"Part 2: {max(totals)}")
