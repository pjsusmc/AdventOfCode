# Advent of Code 2016, Day 13: A Maze of Cubicles
from collections import deque
from aocd import get_data

FAVORITE = int(get_data(day=13, year=2016).strip())
TARGET = (31, 39)
MAX_STEPS = 50

def is_open(x, y):
    if x < 0 or y < 0:              # Negative coordinates are off the map
        return False
    value = x*x + 3*x + 2*x*y + y + y*y + FAVORITE
    return value.bit_count() % 2 == 0   # Even number of 1 bits = open space

def explore(start=(1, 1)):
    """Breadth-first search from start. Cells come off the queue in order
    of distance, so the first time we reach the target is the shortest path."""
    queue = deque([(start, 0)])     # (position, steps)
    visited = {start}
    part1 = None
    part2 = 0

    while queue:
        (x, y), steps = queue.popleft()

        # Once the target is found and we're past 50 steps, every cell
        # within 50 has already been counted, so stop. The office is
        # infinite, so without this the search might never end.
        if part1 is not None and steps > MAX_STEPS:
            break

        if steps <= MAX_STEPS:
            part2 += 1
        if (x, y) == TARGET:        # Reached only once, thanks to visited
            part1 = steps

        for nxt in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if nxt not in visited and is_open(*nxt):   # Cheap set check first
                visited.add(nxt)
                queue.append((nxt, steps + 1))

    return part1, part2

part1, part2 = explore()
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
