# Advent of Code 2017, Day 2: Corruption Checksum
from itertools import combinations
from aocd import get_data


def parse_rows(text: str) -> list[list[int]]:
    """Parse whitespace-delimited integer rows from puzzle input."""
    return [
        [int(tok) for tok in line.split()]
        for line in text.splitlines()
        if line.strip()
    ]


def min_max_checksum(rows: list[list[int]]) -> int:
    """Sum (max - min) for every row."""
    return sum(max(row) - min(row) for row in rows if row)


def row_even_quotient(row: list[int]) -> int:
    """Return a // b for the unique pair in row where one evenly divides the other."""
    # Sorted largest first, so in each pair a >= b: only a % b can be 0.
    for a, b in combinations(sorted(row, reverse=True), 2):
        if b != 0 and a % b == 0:
            return a // b
    raise ValueError(f"No evenly divisible pair found in row: {row!r}")


def divisible_checksum(rows: list[list[int]]) -> int:
    """Sum the evenly divisible quotient for every row."""
    return sum(row_even_quotient(row) for row in rows if row)


spreadsheet = parse_rows(get_data(day=2, year=2017))

print(f"Part 1: {min_max_checksum(spreadsheet)}")
print(f"Part 2: {divisible_checksum(spreadsheet)}")
