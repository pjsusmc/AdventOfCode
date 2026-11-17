# Advent of Code 2015, Day 19: Medicine for Rudolph
import random
import re

with open('input.txt') as f:
    raw_rules, molecule = f.read().strip().split('\n\n')

rules = [tuple(line.split(' => ')) for line in raw_rules.splitlines()]

# --- Part 1: distinct molecules after one replacement ---
results = set()
for i in range(len(molecule)):
    for src, dst in rules:
        if molecule.startswith(src, i):       # Does src match at position i?
            results.add(molecule[:i] + dst + molecule[i + len(src):])

print(f"Part 1: {len(results)}")

# --- Part 2 (search): reduce the molecule back to 'e' ---
def reduce_to_e(molecule, rules):
    rules = list(rules)          # Shuffle a copy, not the caller's list
    while True:                  # Retry with a new rule order until one works
        random.shuffle(rules)
        curr, steps = molecule, 0
        while curr != 'e':
            for src, dst in rules:
                if dst in curr:
                    curr = curr.replace(dst, src, 1)   # Undo one replacement
                    steps += 1
                    break
            else:
                break            # No rule matched: dead end, so reshuffle
        if curr == 'e':
            # The input guarantees every successful path has the same length.
            return steps

print(f"Part 2 (search):  {reduce_to_e(molecule, rules)}")

# --- Part 2 (formula): count elements directly ---
# An element is a capital letter, optionally followed by a lowercase one.
elements = re.findall(r'[A-Z][a-z]?', molecule)
steps = (len(elements)
         - elements.count('Rn') - elements.count('Ar')
         - 2 * elements.count('Y') - 1)

print(f"Part 2 (formula): {steps}")
