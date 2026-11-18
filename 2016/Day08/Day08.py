# Advent of Code 2016, Day 8: Two-Factor Authentication
import re
from aocd import get_data

WIDTH, HEIGHT = 50, 6
grid = [[0] * WIDTH for _ in range(HEIGHT)]

def rotate(seq, n):
    """Shift a list right by n, wrapping around. % handles any size of n."""
    n %= len(seq)
    return seq[-n:] + seq[:-n]

for line in get_data(day=8, year=2016).strip().splitlines():
    # Every instruction has exactly two numbers:
    # "rect 3x2", "rotate row y=0 by 4", "rotate column x=1 by 1"
    a, b = map(int, re.findall(r'\d+', line))

    if line.startswith('rect'):          # Light an a-wide, b-tall rectangle
        for row in grid[:b]:
            row[:a] = [1] * a
    elif 'row' in line:                  # Row a, shifted right by b
        grid[a] = rotate(grid[a], b)
    else:                                # Column a, shifted down by b
        col = rotate([row[a] for row in grid], b)
        for row, value in zip(grid, col):
            row[a] = value

print(f"Part 1: {sum(map(sum, grid))}")

# Part 2: read the letters from the display
print("Part 2:")
for row in grid:
    print(''.join('█' if pixel else ' ' for pixel in row))
