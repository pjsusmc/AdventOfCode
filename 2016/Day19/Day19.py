# Advent of Code 2016, Day 19: An Elephant Named Joseph
from aocd import get_data

def winner_left_steal(n: int) -> int:
    """Classic Josephus problem: write n as 2**m + L; the winner is 2L + 1.

    In binary, that's rotating the highest set bit of n to the lowest bit:
    drop the top bit (giving L), shift left and set the lowest bit (2L + 1).
    """
    high_bit = 1 << (n.bit_length() - 1)   # 2**m, the largest power of 2 <= n
    remainder = n ^ high_bit               # L
    return (remainder << 1) | 1            # 2L + 1

def winner_across_steal(n: int) -> int:
    """Stealing from across the circle follows a base-3 pattern.

    With p the largest power of 3 that's at most n, the winner climbs by 1
    per extra elf up to 2p, then by 2 per extra elf after that.
    O(log3 n) to find p, then O(1).
    """
    power = 1
    while power * 3 <= n:
        power *= 3

    if n == power:              # n is an exact power of 3: the last elf wins.
        return n                # (The next formula would give 0 here.)
    if n <= 2 * power:          # Up to 2*power: winner climbs by 1 per extra elf
        return n - power
    return 2 * n - 3 * power    # Beyond that: winner climbs by 2 per extra elf

elves = int(get_data(day=19, year=2016).strip())

print(f"Part 1: {winner_left_steal(elves)}")
print(f"Part 2: {winner_across_steal(elves)}")
