# Advent of Code 2016, Day 2: Bathroom Security
from aocd import get_data

instructions = get_data(day=2, year=2016).strip().splitlines()

# Screen coordinates: y increases downward.
MOVES = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

# Keypads drawn as pictures; '.' marks a gap with no button.
KEYPAD_1 = """
123
456
789
"""

KEYPAD_2 = """
..1..
.234.
56789
.ABC.
..D..
"""

def build(layout):
    """Turn a keypad picture into {(x, y): key}, skipping gaps."""
    return {(x, y): ch
            for y, row in enumerate(layout.strip().splitlines())
            for x, ch in enumerate(row)
            if ch != '.'}

def decode(instructions, keypad, start='5'):
    # Find where the start key is instead of typing its coordinates.
    x, y = next(pos for pos, key in keypad.items() if key == start)
    code = []
    for line in instructions:
        for char in line:
            dx, dy = MOVES[char]
            # Only move if there's a button there.
            if (x + dx, y + dy) in keypad:
                x, y = x + dx, y + dy
        code.append(keypad[x, y])          # The button at the end of each line
    return ''.join(code)

print(f"Part 1: {decode(instructions, build(KEYPAD_1))}")
print(f"Part 2: {decode(instructions, build(KEYPAD_2))}")
