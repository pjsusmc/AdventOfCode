# Advent of Code 2015, Day 23: Opening the Turing Lock

def parse(line):
    """'jio a, +19' -> ('jio', 'a', 19). Offsets become ints, registers stay strings."""
    op, *args = line.replace(',', '').split()
    return (op, *(a if a in ('a', 'b') else int(a) for a in args))

with open('input.txt') as f:
    program = [parse(line) for line in f if line.strip()]   # Parse once, up front

def run(program, a=0):
    regs = {'a': a, 'b': 0}
    ip = 0                                   # Instruction pointer
    while 0 <= ip < len(program):            # Halt when ip leaves the program
        match program[ip]:
            case ('hlf', r):
                regs[r] //= 2
                ip += 1
            case ('tpl', r):
                regs[r] *= 3
                ip += 1
            case ('inc', r):
                regs[r] += 1
                ip += 1
            case ('jmp', offset):
                ip += offset
            case ('jie', r, offset):         # Jump if even
                ip += offset if regs[r] % 2 == 0 else 1
            case ('jio', r, offset):         # Jump if ONE (not odd!)
                ip += offset if regs[r] == 1 else 1
            case other:                      # Fail loudly instead of looping forever
                raise ValueError(f"Unknown instruction: {other}")
    return regs['b']

print(f"Part 1: {run(program)}")
print(f"Part 2: {run(program, a=1)}")
