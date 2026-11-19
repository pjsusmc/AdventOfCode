# Advent of Code 2016, Day 16: Dragon Checksum
from aocd import get_data

INVERT = str.maketrans("01", "10")

def dragon_fill(seed: str, length: int) -> str:
    data = seed
    while len(data) < length:
        # a + "0" + (a reversed, with 0s and 1s swapped)
        data = f"{data}0{data[::-1].translate(INVERT)}"
    return data[:length]

def checksum(data: str) -> str:
    """Same result as pairing repeatedly until the length is odd.

    Each checksum character covers one block whose size is the largest
    power of 2 dividing the length. It's '1' when the block has an even
    number of 1s, and '0' when it's odd.
    """
    size = len(data) & -len(data)      # Lowest set bit = largest power-of-2 factor
    return ''.join('1' if data.count('1', i, i + size) % 2 == 0 else '0'
                   for i in range(0, len(data), size))

def solve_disk(seed: str, length: int) -> str:
    return checksum(dragon_fill(seed, length))

seed = get_data(day=16, year=2016).strip()

print(f"Part 1: {solve_disk(seed, 272)}")
print(f"Part 2: {solve_disk(seed, 35651584)}")
