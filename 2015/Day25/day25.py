# Advent of Code 2015, Day 25: Let It Snow
import re

with open('input.txt') as f:
    text = f.read()

# Pull out the row and column by name, so it's clear which number is which
row, col = map(int, re.search(r'row (\d+), column (\d+)', text).groups())

# Calculate the 1-based position of row r, column c in the fill order.
# Diagonal number d = r + c - 1
# Cells in the diagonals before d = (d - 1) * d // 2
# Position within diagonal d = col (each diagonal starts in column 1)
d = row + col - 1
index = (d - 1) * d // 2 + col

# Constants given in the puzzle description
seed = 20151125
multiplier = 252533
modulus = 33554393

# The code at position `index` takes (index - 1) multiply-and-mod steps from the seed.
# pow(base, exp, mod) computes (base ** exp) % mod in O(log exp) time.
code = (seed * pow(multiplier, index - 1, modulus)) % modulus

print(f"Part 1 (code at row {row}, col {col}): {code}")
