# Advent of Code 2015, Day 13: Knights of the Dinner Table
from itertools import permutations

happiness = {}
guests = set()

with open('input.txt') as f:
    for line in f:
        words = line.strip().rstrip('.').split()
        if not words:
            continue
        # "Alice would gain 54 happiness units by sitting next to Bob"
        # *_ soaks up the middle words; b gets the last one.
        a, _, sign, amount, *_, b = words
        happiness[a, b] = int(amount) if sign == 'gain' else -int(amount)
        guests.update((a, b))

# Combined score for a pair sitting together: both people's feelings.
pair = {(a, b): happiness[a, b] + happiness[b, a] for a, b in happiness}

# Fix one guest in place: rotating the table gives the same arrangement.
first, *rest = guests

best1 = best2 = float('-inf')
for perm in permutations(rest):
    table = (first, *perm)
    # Each neighbouring pair, including last seat back to first
    links = [pair[a, b] for a, b in zip(table, table[1:] + table[:1])]
    total = sum(links)

    best1 = max(best1, total)
    # Part 2: you sit in the weakest link, removing that pair's score
    # and adding 0 for yourself.
    best2 = max(best2, total - min(links))

print(f"Part 1: {best1}")
print(f"Part 2: {best2}")
