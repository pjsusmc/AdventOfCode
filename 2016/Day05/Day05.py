# Advent of Code 2016, Day 5: How About a Nice Game of Chess?
import hashlib
from itertools import count
from aocd import get_data

door_id = get_data(day=5, year=2016).strip()
base = hashlib.md5(door_id.encode())   # Hash the door ID once

password_1 = []
password_2 = [None] * 8

# Both parts use the same hashes, so search once for both.
for index in count():
    h = base.copy()
    h.update(str(index).encode())
    raw = h.digest()                    # 16 raw bytes, no hex string yet

    # Five hex zeros: the first two bytes are 0, and the third byte is
    # below 16 (so its first hex digit is 0). Most hashes fail here,
    # so they never need converting to hex.
    if raw[0] or raw[1] or raw[2] >= 16:
        continue

    digest = h.hexdigest()

    # Part 1: the 6th character, in the order found
    if len(password_1) < 8:
        password_1.append(digest[5])

    # Part 2: the 6th character is a position, the 7th is the value.
    # Only positions 0-7 count, and only the first hash for each one.
    pos = digest[5]
    if pos in '01234567' and password_2[int(pos)] is None:
        password_2[int(pos)] = digest[6]

    if len(password_1) == 8 and None not in password_2:
        break

print(f"Part 1: {''.join(password_1)}")
print(f"Part 2: {''.join(password_2)}")
