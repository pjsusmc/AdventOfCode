# Advent of Code 2016, Day 18: Like a Rogue
from aocd import get_data

def parse_row(line: str) -> tuple[int, int]:
    """Return (trap_mask, width): '^' is a 1 bit, leftmost tile is the highest bit."""
    return int(line.replace(".", "0").replace("^", "1"), 2), len(line)

def count_safe(seed: str, rows: int) -> int:
    row, width = parse_row(seed)
    bounds = (1 << width) - 1   # width 1-bits: trims the bit that << pushes past the left edge
    safe = width - row.bit_count()

    for _ in range(rows - 1):
        # Shifting lines every tile up with a neighbour; 0 bits shifted in act as safe walls.
        left = row >> 1
        right = (row << 1) & bounds
        # All four trap rules reduce to: left and right neighbours differ.
        row = left ^ right
        safe += width - row.bit_count()

    return safe

seed = get_data(day=18, year=2016).strip()

print(f"Part 1: {count_safe(seed, 40)}")
print(f"Part 2: {count_safe(seed, 400_000)}")
