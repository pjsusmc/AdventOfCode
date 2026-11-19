# Advent of Code 2016, Day 17: Two Steps Forward
from collections import deque
from hashlib import md5
from aocd import get_data

OPEN_CHARS = frozenset("bcdef")   # b-f mean open; 0-9 and a mean closed
MOVES = (                         # Same order as the first 4 hash characters
    ("U", 0, -1),
    ("D", 0, 1),
    ("L", -1, 0),
    ("R", 1, 0),
)
GOAL = (3, 3)

def open_moves(base, x: int, y: int, path: str):
    """Yield (direction, new x, new y) for every open door from this room."""
    h = base.copy()                      # Passcode already hashed in
    h.update(path.encode())              # Add just the path so far
    digest = h.hexdigest()[:4]           # Up, down, left, right
    for (direction, dx, dy), ch in zip(MOVES, digest):
        nx, ny = x + dx, y + dy
        if ch in OPEN_CHARS and 0 <= nx < 4 and 0 <= ny < 4:
            yield direction, nx, ny

def solve_paths(passcode: str) -> tuple[str | None, int]:
    base = md5(passcode.encode())        # Hash the passcode once
    shortest: str | None = None
    longest = 0

    # No visited set: which doors are open depends on the whole path,
    # so reaching the same room by different routes is a different state.
    queue = deque([(0, 0, "")])          # (x, y, path so far)
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == GOAL:
            if shortest is None:
                shortest = path          # BFS: the first path to arrive is the shortest
            longest = len(path)          # ...and each later one is at least as long
            continue                     # Reaching the vault ends the path

        for direction, nx, ny in open_moves(base, x, y, path):
            queue.append((nx, ny, path + direction))

    return shortest, longest

passcode = get_data(day=17, year=2016).strip()
part1, part2 = solve_paths(passcode)
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
