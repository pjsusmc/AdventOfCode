# Advent of Code 2015, Day 1: Not Quite Lisp

# Read the puzzle input. .strip() removes any trailing newline or spaces
# so they don't get miscounted as instructions.
with open('input.txt') as f:
    data = f.read().strip()

# --- Part 1 ---
# Each '(' goes up one floor and each ')' goes down one floor, so the
# final floor is the number of ups minus the number of downs.
# str.count() runs in C, so it's faster than looping in Python.
print(f"Part 1: {data.count('(') - data.count(')')}")

# --- Part 2 ---
# Find the position of the first character that takes Santa to floor -1.
floor = 0  # Santa starts on floor 0

# enumerate(..., start=1) gives 1-based positions, which is how the
# puzzle numbers them, so no "+ 1" is needed when printing.
for i, ch in enumerate(data, start=1):
    # Up one for '(', down one for anything else.
    # (After .strip(), the only other character is ')'.)
    floor += 1 if ch == '(' else -1

    # Stop as soon as Santa first reaches the basement.
    if floor == -1:
        print(f"Part 2: {i}")
        break
else:
    # A for loop's "else" block runs only if the loop finished
    # without hitting "break", meaning Santa never reached floor -1.
    print("Part 2: Santa never reached the basement")
