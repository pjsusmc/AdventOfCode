# Advent of Code 2015, Day 2: I Was Told There Would Be No Math

# Read each line, skip blank ones, and turn "2x3x4" into a sorted tuple
# such as (2, 3, 4). Sorting puts the two smallest sides first.
with open('input.txt') as f:
    boxes = [tuple(sorted(map(int, line.split('x'))))
             for line in f if line.strip()]

paper = 0
ribbon = 0

for a, b, c in boxes:  # a <= b <= c
    # Part 1: surface area, plus slack equal to the smallest face (a * b)
    paper += 2*a*b + 2*b*c + 2*c*a + a*b

    # Part 2: smallest perimeter (2a + 2b), plus a bow equal to the volume
    ribbon += 2*a + 2*b + a*b*c

print(f"Part 1: {paper}")
print(f"Part 2: {ribbon}")
