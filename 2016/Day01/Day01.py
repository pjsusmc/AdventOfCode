# Advent of Code 2016, Day 1: No Time for a Taxicab
from aocd import get_data

# Clockwise order: North, East, South, West
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(text):
    facing = 0                 # Index into DIRECTIONS; start facing North
    x = y = 0
    visited = {(0, 0)}
    first_repeat = None

    for move in text.strip().split(','):
        move = move.strip()
        turn, steps = move[0], int(move[1:])

        # Turning right moves clockwise through DIRECTIONS, left anticlockwise.
        # % 4 wraps around; in Python, -1 % 4 is 3 (West).
        facing = (facing + (1 if turn == 'R' else -1)) % 4
        dx, dy = DIRECTIONS[facing]

        # One step at a time, so paths that cross mid-move are caught.
        for _ in range(steps):
            x += dx
            y += dy
            if first_repeat is None and (x, y) in visited:
                first_repeat = abs(x) + abs(y)
            visited.add((x, y))

    return abs(x) + abs(y), first_repeat

part1, part2 = solve(get_data(day=1, year=2016))
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
