# Advent of Code 2016, Day 4: Security Through Obscurity
import re
from collections import Counter
from string import ascii_lowercase   # 'abcdefghijklmnopqrstuvwxyz'
from aocd import get_data

def checksum(name):
    """Five most common letters, ties broken alphabetically."""
    # Sorting first means equal counts were "first seen" in alphabetical
    # order, and most_common keeps that order for ties.
    letters = sorted(name.replace('-', ''))
    return ''.join(letter for letter, _ in Counter(letters).most_common(5))

def decrypt(name, sector):
    """Shift each letter forward by sector places; dashes become spaces."""
    shift = sector % 26
    # Map a-z to the alphabet rotated by `shift`, and '-' to ' '.
    table = str.maketrans(ascii_lowercase + '-',
                          ascii_lowercase[shift:] + ascii_lowercase[:shift] + ' ')
    return name.translate(table)

part1 = 0
part2 = None

for line in get_data(day=4, year=2016).strip().splitlines():
    # "aaaaa-bbb-z-y-x-123[abxyz]" -> name, sector ID, checksum
    name, sector, check = re.match(r'([a-z-]+)-(\d+)\[([a-z]+)\]', line).groups()
    sector = int(sector)

    if checksum(name) == check:        # Only real rooms count
        part1 += sector
        if 'northpole' in decrypt(name, sector):
            part2 = sector

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
