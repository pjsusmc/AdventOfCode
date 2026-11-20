# Advent of Code 2016, Day 23: Safe Cracking
from aocd import get_data

REGISTERS = ("a", "b", "c", "d")


def parse_program(text: str) -> list[list[str]]:
    """Parse non-empty assembunny lines into mutable token lists (tgl edits them)."""
    return [line.split() for line in text.splitlines() if line.strip()]


def _resolve(regs: dict[str, int], operand: str) -> int:
    """A register's value, or the number written in the operand."""
    return regs[operand] if operand in regs else int(operand)


def _toggle(inst: list[str]) -> None:
    """Apply tgl's rules to an instruction, in place."""
    if len(inst) == 2:                       # One argument: inc <-> everything else
        inst[0] = "dec" if inst[0] == "inc" else "inc"
    else:                                    # Two arguments: jnz <-> everything else
        inst[0] = "cpy" if inst[0] == "jnz" else "jnz"


def _try_multiply(prog: list[list[str]], ip: int, regs: dict[str, int]) -> bool:
    """Fold the nested loop that multiplies, if it starts at ip:

        cpy src c   / inc a / dec c / jnz c -2 / dec d / jnz d -5

    The inner three lines add c to a; the outer loop repeats that d times.
    So the whole block is a += src * d, then c = d = 0.
    Checked fresh each time, so a block that tgl has changed won't match.
    """
    match prog[ip:ip + 6]:                   # A shorter slice near the end just won't match
        case [
            ["cpy", src, c], ["inc", a], ["dec", c2], ["jnz", c3, "-2"],
            ["dec", d], ["jnz", d2, "-5"],
        ] if (
            c == c2 == c3 and d == d2                # Same counters throughout
            and {a, c, d} <= set(REGISTERS)          # All real registers...
            and len({a, c, d}) == 3                  # ...and all different
            and src not in (a, d)                    # src isn't changed by the loop
            and _resolve(regs, src) > 0 and regs[d] > 0   # Loops actually count down
        ):
            regs[a] += _resolve(regs, src) * regs[d]
            regs[c] = regs[d] = 0
            return True
    return False


def run_program(raw_prog: list[list[str]], initial_a: int) -> int:
    """Run an assembunny program with tgl, returning register a."""
    prog = [inst[:] for inst in raw_prog]    # tgl edits the program, so use a copy
    regs = dict.fromkeys(REGISTERS, 0)
    regs["a"] = initial_a
    ip = 0

    while 0 <= ip < len(prog):
        if _try_multiply(prog, ip, regs):
            ip += 6
            continue

        match prog[ip]:
            case ["cpy", x, y] if y in regs:
                regs[y] = _resolve(regs, x)
            case ["inc", x] if x in regs:
                regs[x] += 1
            case ["dec", x] if x in regs:
                regs[x] -= 1
            case ["jnz", x, y]:
                if _resolve(regs, x) != 0:
                    ip += _resolve(regs, y)
                    continue                 # Jumped: skip the ip += 1 below
            case ["tgl", x]:
                target = ip + _resolve(regs, x)
                if 0 <= target < len(prog):  # Toggling outside the program does nothing
                    _toggle(prog[target])
            case _:
                pass                         # Invalid after a toggle (e.g. 'cpy 1 2'): skip it
        ip += 1

    return regs["a"]


raw_prog = parse_program(get_data(day=23, year=2016))

print(f"Part 1: {run_program(raw_prog, 7)}")
print(f"Part 2: {run_program(raw_prog, 12)}")
