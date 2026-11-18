# Advent of Code 2016, Day 14: One-Time Pad
import hashlib
import re
from functools import cache
from itertools import count
from aocd import get_data

SALT = get_data(day=14, year=2016).strip()

@cache  # Each hash is checked against the next 1000, so reuse saves a lot
def get_hash(index, stretch=0):
    """MD5 of salt + index, then rehashed `stretch` more times.
    Part 2's stretch of 2016 means 2017 hashes in total."""
    h = hashlib.md5(f"{SALT}{index}".encode()).hexdigest()
    for _ in range(stretch):
        h = hashlib.md5(h.encode()).hexdigest()
    return h

def index_of_64th_key(stretch=0):
    keys = 0
    for index in count():
        # Only the FIRST character repeated three times in a row counts.
        m = re.search(r'(.)\1\1', get_hash(index, stretch))
        if not m:
            continue

        # It's a key if one of the next 1000 hashes has that character five times.
        five = m.group(1) * 5
        if any(five in get_hash(i, stretch) for i in range(index + 1, index + 1001)):
            keys += 1
            if keys == 64:
                return index

print(f"Part 1: {index_of_64th_key()}")
print(f"Part 2: {index_of_64th_key(stretch=2016)}")
