# Advent of Code 2016, Day 15: Timing is Everything
import re
from math import lcm
from aocd import get_data

def parse_discs(text: str) -> list[tuple[int, int, int]]:
    """(disc number, positions, start position) for each line."""
    return [
        tuple(map(int, groups))
        for groups in re.findall(
            r"Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+)\.",
            text,
        )
    ]

def first_button_press(discs: list[tuple[int, int, int]]) -> int:
    t = 0
    step = 1
    for disc, positions, start in discs:
        # The capsule reaches disc k at time t + k; it passes if the
        # disc is at position 0 then.
        while (start + t + disc) % positions != 0:
            t += step
        # Stepping by the lcm keeps every disc so far lined up.
        step = lcm(step, positions)
    return t

discs = parse_discs(get_data(day=15, year=2016))

part1 = first_button_press(discs)
# Part 2: a new disc below the others, with 11 positions, starting at 0
part2 = first_button_press([*discs, (len(discs) + 1, 11, 0)])

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
