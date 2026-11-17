# Advent of Code 2015, Day 16: Aunt Sue
import re
from operator import eq, gt, lt

# What the MFCSAM detected
TARGET = {
    'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
    'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3,
    'cars': 2, 'perfumes': 1,
}

# Part 2: how a Sue's value must compare with the reading.
# gt(val, target) means val > target. Anything not listed uses eq.
PART2_RULES = {'cats': gt, 'trees': gt, 'pomeranians': lt, 'goldfish': lt}

def matches(traits, rules):
    """True if every trait this Sue lists passes its rule.
    Traits she doesn't list are unknown, so they can't rule her out."""
    return all(rules.get(prop, eq)(val, TARGET[prop])
               for prop, val in traits.items())

part1 = part2 = None
with open('input.txt') as f:
    for line in f:
        if not line.strip():
            continue
        sue = int(re.search(r'Sue (\d+):', line).group(1))
        # "Sue 1: cars: 9, akitas: 3" -> {'cars': 9, 'akitas': 3}
        traits = {prop: int(val) for prop, val in re.findall(r'([a-z]+): (\d+)', line)}

        if matches(traits, {}):            # Part 1: every trait must be equal
            part1 = sue
        if matches(traits, PART2_RULES):   # Part 2: ranges for four traits
            part2 = sue

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
