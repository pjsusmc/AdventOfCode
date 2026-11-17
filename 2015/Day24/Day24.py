# Advent of Code 2015, Day 24: It Hangs in the Balance
from itertools import combinations
from math import prod

with open('input.txt') as f:
    packages = [int(line) for line in f if line.strip()]

def subsets(items, target, size):
    """Index tuples of `size` items whose weights add up to target.
    Using positions (not values) keeps equal weights distinct."""
    for idx in combinations(range(len(items)), size):
        if sum(items[i] for i in idx) == target:
            yield idx

def without(items, idx):
    """The items left over after taking the positions in idx."""
    return [x for i, x in enumerate(items) if i not in idx]

def can_split(items, target, groups):
    """Can items be divided into `groups` groups that each weigh target?"""
    if groups == 1:
        return sum(items) == target        # Whatever's left is the last group
    for size in range(1, len(items) + 1):
        for idx in subsets(items, target, size):
            if can_split(without(items, idx), target, groups - 1):
                return True
    return False

def best_entanglement(packages, groups):
    total = sum(packages)
    if total % groups:                     # Can't split evenly at all
        return None
    target = total // groups

    # Smallest first group wins, so try sizes in increasing order.
    for size in range(1, len(packages) + 1):
        # Within one size, try the lowest quantum entanglement first.
        candidates = sorted(subsets(packages, target, size),
                            key=lambda idx: prod(packages[i] for i in idx))
        for idx in candidates:
            # Only count it if the rest really can be split evenly.
            if can_split(without(packages, idx), target, groups - 1):
                return prod(packages[i] for i in idx)
    return None

print(f"Part 1: {best_entanglement(packages, 3)}")
print(f"Part 2: {best_entanglement(packages, 4)}")
