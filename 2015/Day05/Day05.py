# Advent of Code 2015, Day 5: Doesn't He Have Intern-Elves For This?
import re

with open('input.txt') as f:
    words = [line.strip() for line in f if line.strip()]

def nice1(s):
    """Part 1 rules."""
    vowels = sum(c in 'aeiou' for c in s) >= 3            # At least 3 vowels
    double = re.search(r'(.)\1', s)                        # A letter twice in a row
    bad = any(b in s for b in ('ab', 'cd', 'pq', 'xy'))    # None of these allowed
    return vowels and double and not bad

def nice2(s):
    """Part 2 rules."""
    pair = re.search(r'(..).*\1', s)      # A pair that appears twice, no overlap
    sandwich = re.search(r'(.).\1', s)    # A letter repeated with one in between
    return pair and sandwich

# Each True counts as 1, so sum() gives the number of nice words.
print(f"Part 1: {sum(bool(nice1(w)) for w in words)}")
print(f"Part 2: {sum(bool(nice2(w)) for w in words)}")
