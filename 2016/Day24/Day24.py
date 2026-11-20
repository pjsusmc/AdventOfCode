# Advent of Code 2016, Day 24: Air Duct Spelunking
from collections import deque
from itertools import pairwise, permutations
from aocd import get_data

NEIGHBORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def parse_maze(text: str) -> tuple[set[tuple[int, int]], dict[int, tuple[int, int]]]:
    """Return (open_tiles, poi_coords) where poi_coords maps digit -> (x, y)."""
    open_tiles: set[tuple[int, int]] = set()
    pois: dict[int, tuple[int, int]] = {}
    for y, line in enumerate(text.splitlines()):
        for x, ch in enumerate(line.strip()):
            if ch == "#":
                continue
            open_tiles.add((x, y))
            if ch.isdigit():
                pois[int(ch)] = (x, y)
    return open_tiles, pois


def bfs_distances(
    open_tiles: set[tuple[int, int]],
    start: tuple[int, int],
    targets: dict[int, tuple[int, int]],
) -> dict[int, int]:
    """Shortest step count from start to every checkpoint it can reach."""
    target_by_pos = {pos: poi for poi, pos in targets.items()}
    found = {target_by_pos[start]: 0} if start in target_by_pos else {}

    queue = deque([(start, 0)])
    seen = {start}
    while queue and len(found) < len(targets):   # Stop once every checkpoint is found
        (x, y), dist = queue.popleft()
        for dx, dy in NEIGHBORS:
            nxt = (x + dx, y + dy)
            if nxt in open_tiles and nxt not in seen:
                seen.add(nxt)
                if nxt in target_by_pos:
                    found[target_by_pos[nxt]] = dist + 1
                queue.append((nxt, dist + 1))
    return found


def distance_table(
    open_tiles: set[tuple[int, int]], pois: dict[int, tuple[int, int]]
) -> dict[int, dict[int, int]]:
    """{a: {b: steps}} between every pair of checkpoints, keyed by their digits."""
    table = {src: bfs_distances(open_tiles, pos, pois) for src, pos in pois.items()}
    for src, dists in table.items():
        if len(dists) < len(pois):               # Fail loudly instead of using 0
            missing = sorted(set(pois) - set(dists))
            raise ValueError(f"Checkpoint(s) {missing} can't be reached from {src}")
    return table


def shortest_tour(dist: dict[int, dict[int, int]], *, return_to_start: bool) -> int:
    """Fewest steps starting at 0 and visiting every checkpoint, optionally
    ending back at 0. Tries every order of the other checkpoints."""
    others = [p for p in dist if p != 0]
    end = (0,) if return_to_start else ()
    # pairwise gives each leg of the route: (0, a), (a, b), ..., and (z, 0) for part 2
    return min(
        sum(dist[a][b] for a, b in pairwise((0, *order, *end)))
        for order in permutations(others)
    )


open_tiles, pois = parse_maze(get_data(day=24, year=2016))
dist = distance_table(open_tiles, pois)

print(f"Part 1: {shortest_tour(dist, return_to_start=False)}")
print(f"Part 2: {shortest_tour(dist, return_to_start=True)}")
