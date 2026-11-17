# Advent of Code 2015, Day 20: Infinite Elves and Infinite Houses
TARGET = 33_100_000

# Search houses below this number. House n always gets at least 10*n
# presents from elf n alone, so TARGET // 10 is guaranteed to be enough,
# but that's slow in pure Python. Start smaller and raise it if needed.
LIMIT = 1_000_000

def first_house(per_visit, max_visits=None):
    """Lowest house that gets at least TARGET presents, or None if none
    below LIMIT does. Each elf leaves per_visit * elf presents per house,
    and stops after max_visits houses if a cap is given."""
    houses = [0] * LIMIT
    for elf in range(1, LIMIT):
        gift = elf * per_visit                    # Same for every house this elf visits
        stop = LIMIT if max_visits is None else min(LIMIT, elf * max_visits + 1)
        for house in range(elf, stop, elf):       # elf, 2*elf, 3*elf, ...
            houses[house] += gift
    # Default of None instead of a StopIteration crash
    return next((i for i, presents in enumerate(houses) if presents >= TARGET), None)

for part, args in ((1, (10,)), (2, (11, 50))):
    answer = first_house(*args)
    if answer is None:
        print(f"Part {part}: not found below {LIMIT:,}. Raise LIMIT.")
    else:
        print(f"Part {part}: {answer}")
