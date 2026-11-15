# Advent of Code 2015, Day 6: Probably a Fire Hazard
import re

# The input format is fixed, so spell it out.
pattern = re.compile(r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')

# Parse every line once into (action, x1, y1, x2, y2).
instructions = []
with open('input.txt') as f:
    for line in f:
        m = pattern.match(line.strip())
        if m:
            action = m.group(1)
            x1, y1, x2, y2 = map(int, m.groups()[1:])
            instructions.append((action, x1, y1, x2, y2))

SIZE = 1000
# [0] * SIZE is safe for the inner rows because ints can't be changed in place.
# The outer list must be a comprehension, or every row would be the same list.
lit = [[0] * SIZE for _ in range(SIZE)]      # Part 1: on (1) or off (0)
bright = [[0] * SIZE for _ in range(SIZE)]   # Part 2: brightness level

for action, x1, y1, x2, y2 in instructions:
    n = y2 - y1 + 1            # Number of lights per row (inclusive range)
    cols = slice(y1, y2 + 1)   # The same column range for every row

    for x in range(x1, x2 + 1):   # Inclusive range again
        row1 = lit[x]
        row2 = bright[x]

        # One check per row, then the whole slice updates at once.
        if action == 'turn on':
            row1[cols] = [1] * n
            row2[cols] = [v + 1 for v in row2[cols]]
        elif action == 'turn off':
            row1[cols] = [0] * n
            row2[cols] = [max(v - 1, 0) for v in row2[cols]]
        else:  # toggle
            row1[cols] = [1 - v for v in row1[cols]]
            row2[cols] = [v + 2 for v in row2[cols]]

# sum(map(sum, grid)) adds up each row, then adds the row totals.
print(f"Part 1: {sum(map(sum, lit))}")
print(f"Part 2: {sum(map(sum, bright))}")
