# Advent of Code 2016, Day 11: Radioisotope Thermoelectric Generators
import re
from collections import deque
from itertools import chain, combinations
from aocd import get_data

FLOORS = 4

def parse(text):
    """One frozenset per floor of (element, 'generator' | 'microchip') items."""
    floors = [frozenset(re.findall(r'(\w+)(?:-compatible)? (microchip|generator)', line))
              for line in text.strip().splitlines()]
    floors += [frozenset()] * (FLOORS - len(floors))   # Pad to 4 floors if needed
    return tuple(floors)

def is_safe(floor):
    """Chips are safe if there are no generators, or each chip has its own."""
    gens = {e for e, kind in floor if kind == 'generator'}
    chips = {e for e, kind in floor if kind == 'microchip'}
    return not gens or chips <= gens      # An empty set of chips is always a subset

def signature(elevator, floors):
    """What matters about a state, ignoring element names.

    Swapping which element is which gives an equivalent state, so describe
    each element only by (generator floor, chip floor) and sort the pairs.
    """
    where = {}
    for level, floor in enumerate(floors):
        for element, kind in floor:
            # Index 0 for the generator, 1 for the chip (True counts as 1)
            where.setdefault(element, [0, 0])[kind == 'microchip'] = level
    return elevator, tuple(sorted(map(tuple, where.values())))

def min_steps(floors):
    """Breadth-first search: the first time everything reaches the top
    floor is guaranteed to use the fewest steps."""
    total = sum(map(len, floors))
    queue = deque([(0, 0, floors)])            # (steps, elevator, floors)
    seen = {signature(0, floors)}

    while queue:
        steps, elevator, floors = queue.popleft()
        if len(floors[-1]) == total:           # Everything on the top floor
            return steps

        here = floors[elevator]
        # Never go down if every floor below is empty: nothing to fetch there.
        lowest = next(i for i, f in enumerate(floors) if f)
        directions = [d for d in (1, -1) if lowest <= elevator + d < FLOORS]

        # The elevator carries one or two items.
        for load in chain(combinations(here, 2), combinations(here, 1)):
            for d in directions:
                new = list(floors)
                new[elevator] = here.difference(load)
                new[elevator + d] = floors[elevator + d].union(load)
                if not (is_safe(new[elevator]) and is_safe(new[elevator + d])):
                    continue
                key = signature(elevator + d, new)
                if key not in seen:
                    seen.add(key)
                    queue.append((steps + 1, elevator + d, tuple(new)))
    return None

floors = parse(get_data(day=11, year=2016))
print(f"Part 1: {min_steps(floors)}")

# Part 2: two more generator/chip pairs start on the first floor
extra = {(e, k) for e in ('elerium', 'dilithium') for k in ('generator', 'microchip')}
print(f"Part 2: {min_steps((floors[0] | extra, *floors[1:]))}")
