# Advent of Code 2016, Day 20: Firewall Rules
from aocd import get_data

MAX_IP = (1 << 32) - 1  # 4294967295


def parse_ranges(text: str) -> list[tuple[int, int]]:
    """Parse 'lo-hi' lines into sorted inclusive (lo, hi) pairs."""
    return sorted(tuple(map(int, line.split("-")))
                  for line in text.splitlines() if line.strip())


def scan(ranges: list[tuple[int, int]], max_ip: int = MAX_IP) -> tuple[int | None, int]:
    """Return (lowest allowed address, number of allowed addresses).

    Sweep the sorted ranges, tracking the lowest address not yet known to be
    blocked. Whenever a range starts past it, the addresses in between are allowed.
    """
    lowest = None
    allowed = 0
    next_free = 0

    for lo, hi in ranges:
        if lo > next_free:                    # A gap before this range
            if lowest is None:
                lowest = next_free
            allowed += lo - next_free
        # max() handles overlapping and nested ranges; hi + 1 merges adjacent ones.
        next_free = max(next_free, hi + 1)

    if next_free <= max_ip:                   # A gap after the last range
        if lowest is None:
            lowest = next_free
        allowed += max_ip + 1 - next_free

    return lowest, allowed


part1, part2 = scan(parse_ranges(get_data(day=20, year=2016)))

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
