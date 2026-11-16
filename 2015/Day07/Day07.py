# Advent of Code 2015, Day 7: Some Assembly Required
import operator
from functools import cache

# Map each operator name to the function that performs it.
OPS = {
    'AND': operator.and_,
    'OR': operator.or_,
    'LSHIFT': operator.lshift,
    'RSHIFT': operator.rshift,
}

# Build the circuit: target wire -> expression, split into its parts.
# "x AND y -> z" becomes wires['z'] = ['x', 'AND', 'y']
wires = {}
with open('input.txt') as f:
    for line in f:
        if line.strip():
            expr, target = line.strip().split(' -> ')
            wires[target] = expr.split()

@cache  # Remembers each wire's signal after the first calculation
def signal(wire):
    """Return the 16-bit signal on a wire (or the value of a number)."""
    if wire.isdigit():
        return int(wire)

    parts = wires[wire]
    if len(parts) == 1:          # "123 -> x" or "y -> x"
        result = signal(parts[0])
    elif len(parts) == 2:        # "NOT y -> x"
        result = ~signal(parts[1])
    else:                        # "y AND z -> x", etc.
        left, op, right = parts
        result = OPS[op](signal(left), signal(right))  # KeyError if op is unknown

    # Keep only the low 16 bits. This turns ~'s negative numbers into
    # unsigned values and trims LSHIFT results back to 16 bits.
    return result & 0xFFFF

# --- Part 1 ---
part1 = signal('a')
print(f"Part 1: {part1}")

# --- Part 2 ---
# Override wire b with part 1's answer, then clear every cached signal
# so the whole circuit is recalculated.
wires['b'] = [str(part1)]
signal.cache_clear()
print(f"Part 2: {signal('a')}")
