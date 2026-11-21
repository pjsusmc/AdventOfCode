# Advent of Code 2017, Day 3: Spiral Memory
import math
from aocd import get_data

NEIGHBORS_8 = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
)
SPIRAL_DIRS = ((1, 0), (0, 1), (-1, 0), (0, -1))  # Right, Up, Left, Down


def spiral_coords(n: int) -> tuple[int, int]:
    """Return (x, y) coordinates of square n >= 1 with square 1 at (0, 0)."""
    if n == 1:
        return (0, 0)

    # Odd side length k of the ring containing n: (k - 2)^2 < n <= k^2.
    # isqrt keeps this exact for large n, where float sqrt could round wrongly.
    k = math.isqrt(n - 1) + 1
    if k % 2 == 0:
        k += 1

    ring = k // 2
    side_len = k - 1  # Steps along each of the 4 sides of this ring
    side, pos = divmod(k * k - n, side_len)

    # Corner (k*k) sits at (ring, -ring); walk backward along the ring perimeter.
    match side:
        case 0:  # Bottom edge going left from (ring, -ring)
            return (ring - pos, -ring)
        case 1:  # Left edge going up from (-ring, -ring)
            return (-ring, -ring + pos)
        case 2:  # Top edge going right from (-ring, ring)
            return (-ring + pos, ring)
        case _:  # Right edge going down from (ring, ring)
            return (ring, ring - pos)


def manhattan_distance(n: int) -> int:
    """Manhattan distance from square n to square 1 at (0, 0)."""
    x, y = spiral_coords(n)
    return abs(x) + abs(y)


def spiral_path():
    """Yield (x, y) for squares 2, 3, 4, ... in spiral order."""
    x = y = 0
    step_len = 1
    dir_idx = 0
    while True:
        for _ in range(2):              # Each step length is used for two sides
            dx, dy = SPIRAL_DIRS[dir_idx]
            for _ in range(step_len):
                x += dx
                y += dy
                yield x, y
            dir_idx = (dir_idx + 1) % 4
        step_len += 1


def first_larger_stress_value(target: int) -> int:
    """Return the first spiral stress-test value strictly greater than target."""
    if target < 1:
        return 1
    grid = {(0, 0): 1}
    for x, y in spiral_path():
        # Sum of all neighbours written so far; unwritten squares count as 0
        val = sum(grid.get((x + dx, y + dy), 0) for dx, dy in NEIGHBORS_8)
        if val > target:
            return val
        grid[x, y] = val


target = int(get_data(day=3, year=2017).strip())

print(f"Part 1: {manhattan_distance(target)}")
print(f"Part 2: {first_larger_stress_value(target)}")
