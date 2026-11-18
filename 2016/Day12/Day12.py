# Advent of Code 2016, Day 12: Leonardo's Monorail
from aocd import get_data

def parse(line):
    """'cpy 41 a' -> ('cpy', 41, 'a'). Numbers become ints once, up front."""
    op, *args = line.split()
    return (op, *(a if a.isalpha() else int(a) for a in args))

program = [parse(line) for line in get_data(day=12, year=2016).strip().splitlines()]

def run(program, c=0):
    regs = {'a': 0, 'b': 0, 'c': c, 'd': 0}

    def val(x):
        """A register's value, or the number itself."""
        return regs[x] if isinstance(x, str) else x

    pc = 0
    while 0 <= pc < len(program):           # Halt if pc leaves the program either way
        # Shortcut: "inc x / dec y / jnz y -2" just adds y to x and clears y.
        # Do it in one step instead of looping y times.
        match program[pc:pc + 3]:
            case [('inc', x), ('dec', y), ('jnz', y2, -2)] if y == y2 and regs[y] > 0:
                regs[x] += regs[y]
                regs[y] = 0
                pc += 3
                continue

        match program[pc]:
            case ('cpy', src, dst):
                regs[dst] = val(src)
            case ('inc', r):
                regs[r] += 1
            case ('dec', r):
                regs[r] -= 1
            case ('jnz', test, offset):
                if val(test) != 0:
                    pc += val(offset)
                    continue                 # Jumped: skip the pc += 1 below
            case other:
                raise ValueError(f"Unknown instruction: {other}")
        pc += 1
    return regs['a']

print(f"Part 1: {run(program)}")
print(f"Part 2: {run(program, c=1)}")
