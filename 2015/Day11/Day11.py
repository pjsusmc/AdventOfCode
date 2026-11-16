# Advent of Code 2015, Day 11: Corporate Policy
import re
from string import ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'

def increment(pw):
    """Increment like an odometer: rightmost letter first, z wraps to a."""
    chars = list(pw)
    for i in reversed(range(len(chars))):
        if chars[i] == 'z':
            chars[i] = 'a'          # Wrap and carry to the next letter left
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            # Jump past i, o and l right away. The next letters
            # (j, p and m) are allowed, so one extra step is enough.
            if chars[i] in 'iol':
                chars[i] = chr(ord(chars[i]) + 1)
            break                   # No carry, so we're done
    return ''.join(chars)

def is_valid(pw):
    # No i, o or l (cheapest check first)
    if any(c in pw for c in 'iol'):
        return False

    # Three letters in a row: any 3-letter slice that appears in the alphabet
    if not any(pw[i:i+3] in ascii_lowercase for i in range(len(pw) - 2)):
        return False

    # Two different, non-overlapping pairs. findall doesn't overlap,
    # so 'aaa' gives one pair; the set ignores repeats of the same letter.
    return len(set(re.findall(r'(.)\1', pw))) >= 2

def next_password(pw):
    pw = increment(pw)
    while not is_valid(pw):
        pw = increment(pw)
    return pw

part1 = next_password('hxbxwxba')
part2 = next_password(part1)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
