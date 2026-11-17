# Advent of Code 2015, Day 18: Like a GIF For Your Yard
from collections import Counter

with open('input.txt') as f:
    lines = [line.strip() for line in f if line.strip()]

SIZE = len(lines)
CORNERS = {(0, 0), (0, SIZE - 1), (SIZE - 1, 0), (SIZE - 1, SIZE - 1)}
# The 8 directions around a light (every offset except (0, 0))
OFFSETS = [(dr, dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)]

# The set of lit positions, parsed once
start = {(r, c) for r, row in enumerate(lines)
                for c, ch in enumerate(row) if ch == '#'}

def step(on):
    """One animation step. `on` is the set of lit positions."""
    # Each lit light adds 1 to each of its 8 neighbors. Positions that
    # never appear have no lit neighbors, so they'll be off anyway.
    counts = Counter((r + dr, c + dc) for r, c in on for dr, dc in OFFSETS)
    return {
        (r, c) for (r, c), n in counts.items()
        if 0 <= r < SIZE and 0 <= c < SIZE        # Neighbors can fall off the edge
        and (n == 3 or (n == 2 and (r, c) in on))  # Game of Life rules
    }

def run(stuck=False):
    on = (start | CORNERS) if stuck else start    # Corners stuck from the start
    for _ in range(100):
        on = step(on)
        if stuck:
            on |= CORNERS                         # ...and after every step
    return len(on)

print(f"Part 1: {run()}")
print(f"Part 2: {run(stuck=True)}")
