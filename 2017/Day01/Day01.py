# Advent of Code 2017, Day 1: Inverse Captcha
from aocd import get_data


def captcha_sum(digits: str, step: int) -> int:
    """Sum digits matching the digit `step` positions ahead in a circular string."""
    rotated = digits[step:] + digits[:step]    # Each digit's partner, lined up
    return sum(int(a) for a, b in zip(digits, rotated) if a == b)

captcha = get_data(day=1, year=2017).strip()

print(f"Part 1: {captcha_sum(captcha, 1)}")
print(f"Part 2: {captcha_sum(captcha, len(captcha) // 2)}")
