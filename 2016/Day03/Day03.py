# Advent of Code 2016, Day 3: Squares With Three Sides
from aocd import get_data

# Every number in the input, read row by row
numbers = [int(x) for x in get_data(day=3, year=2016).split()]

def chunks(seq, n=3):
    """Split a list into consecutive groups of n."""
    return [seq[i:i + n] for i in range(0, len(seq), n)]

def count_valid(triangles):
    # After sorting, it's a triangle if the two shorter sides are
    # longer together than the longest side. Each True counts as 1.
    return sum(a + b > c for a, b, c in map(sorted, triangles))

# Part 1: each row is a triangle
print(f"Part 1: {count_valid(chunks(numbers))}")

# Part 2: triangles run down the columns. numbers[k::3] is column k, so
# putting the three columns end to end lists the numbers in column order,
# and grouping in threes works just like part 1.
by_column = numbers[0::3] + numbers[1::3] + numbers[2::3]
print(f"Part 2: {count_valid(chunks(by_column))}")
