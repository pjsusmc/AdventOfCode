# Advent of Code 2015, Day 4: The Ideal Stocking Stuffer
import hashlib
from itertools import count

key = 'yzbqklnj'

# Hash the key once. Each candidate copies this state and adds only
# the number, instead of rehashing the whole key every time.
base = hashlib.md5(key.encode())

def find(prefix, start=0):
    """Return the lowest number >= start whose hash begins with prefix."""
    for num in count(start):          # start, start+1, start+2, ...
        h = base.copy()
        h.update(str(num).encode())
        if h.hexdigest().startswith(prefix):
            return num

part1 = find('00000')
print(f"Part 1: {part1}")

# Any hash starting with six zeros also starts with five, so part 2's
# answer can't be lower than part 1's. Search from there.
print(f"Part 2: {find('000000', part1)}")
