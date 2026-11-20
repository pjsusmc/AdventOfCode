# Advent of Code 2016, Day 22: Grid Computing
import re
from collections import deque
from aocd import get_data

LINE_RE = re.compile(r"/dev/grid/node-x(\d+)-y(\d+)\s+\d+T\s+(\d+)T\s+(\d+)T\s+\d+%")
NEIGHBORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def parse_nodes(text: str) -> dict[tuple[int, int], tuple[int, int]]:
    """Return {(x, y): (used, avail)} for all parsed grid nodes."""
    nodes: dict[tuple[int, int], tuple[int, int]] = {}
    for line in text.splitlines():
        if m := LINE_RE.match(line.strip()):      # Skip the header lines
            x, y, used, avail = map(int, m.groups())
            nodes[x, y] = (used, avail)
    return nodes


def count_viable_pairs(nodes: dict[tuple[int, int], tuple[int, int]]) -> int:
    """Count ordered pairs (a, b) with a != b, used_a > 0, and used_a <= avail_b."""
    items = list(nodes.items())
    return sum(
        1
        for pos_a, (used_a, _) in items if used_a > 0
        for pos_b, (_, avail_b) in items
        if pos_a != pos_b and used_a <= avail_b
    )


def min_goal_moves(nodes: dict[tuple[int, int], tuple[int, int]]) -> int:
    """Fewest moves to bring the data at (max_x, 0) to (0, 0).

    Treat the grid as a sliding puzzle: the only move is shifting a
    neighbour's data into the single empty node, which moves the "hole".
    """
    max_x = max(x for x, _ in nodes)
    max_y = max(y for _, y in nodes)

    empties = [pos for pos, (used, _) in nodes.items() if used == 0]
    if len(empties) != 1:
        raise ValueError(f"Expected 1 empty node, found {len(empties)}")
    empty_start = empties[0]
    goal_start = (max_x, 0)

    # A node's data can move into the hole only if it fits. The huge,
    # nearly full nodes fail this test, so they act as walls.
    empty_size = sum(nodes[empty_start])          # used + avail = total size
    movable = {pos for pos, (used, _) in nodes.items() if used <= empty_size}

    # State: where the goal data is, and where the hole is.
    start = (*goal_start, *empty_start)
    queue: deque[tuple[int, int, int, int, int]] = deque([(*start, 0)])
    seen = {start}

    while queue:
        gx, gy, ex, ey, steps = queue.popleft()
        if (gx, gy) == (0, 0):
            return steps

        for dx, dy in NEIGHBORS:
            nx, ny = ex + dx, ey + dy
            if not (0 <= nx <= max_x and 0 <= ny <= max_y) or (nx, ny) not in movable:
                continue
            # The neighbour's data moves into the hole, so the hole moves to
            # the neighbour. If that data was the goal, the goal moves too.
            goal = (ex, ey) if (nx, ny) == (gx, gy) else (gx, gy)
            state = (*goal, nx, ny)
            if state not in seen:
                seen.add(state)
                queue.append((*state, steps + 1))

    raise RuntimeError("No path found for goal data")


nodes = parse_nodes(get_data(day=22, year=2016))

print(f"Part 1: {count_viable_pairs(nodes)}")
print(f"Part 2: {min_goal_moves(nodes)}")
