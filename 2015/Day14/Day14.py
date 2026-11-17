# Advent of Code 2015, Day 14: Reindeer Olympics
import re

def distance(speed, fly, rest, t):
    """How far a reindeer has gone after t seconds."""
    # Each cycle is `fly` seconds flying plus `rest` seconds resting.
    cycles, remainder = divmod(t, fly + rest)
    # Full cycles, plus up to `fly` seconds of flying in the partial cycle
    return speed * (cycles * fly + min(remainder, fly))

# Each line has exactly three numbers: speed, fly time, rest time.
reindeer = []
with open('input.txt') as f:
    for line in f:
        nums = list(map(int, re.findall(r'\d+', line)))
        if nums:
            reindeer.append(nums)

RACE = 2503

# --- Part 1 ---
# No simulation needed: calculate each distance at the end of the race.
print(f"Part 1: {max(distance(*r, RACE) for r in reindeer)}")

# --- Part 2 ---
points = [0] * len(reindeer)
for t in range(1, RACE + 1):          # Score after each second, from 1
    dists = [distance(*r, t) for r in reindeer]
    lead = max(dists)
    for i, d in enumerate(dists):
        if d == lead:                 # Everyone tied for the lead scores
            points[i] += 1

print(f"Part 2: {max(points)}")
