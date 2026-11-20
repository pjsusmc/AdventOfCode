# Advent of Code 2016, Day 25: Clock Signal
from itertools import count
from aocd import get_data

REGISTERS = ("a", "b", "c", "d")


def parse_program(text: str) -> list[list[str]]:
    """Parse non-empty assembunny lines into instruction token lists."""
    return [line.split() for line in text.splitlines() if line.strip()]


def _resolve(regs: dict[str, int], operand: str) -> int:
    """Return register value if operand is a register name, else parse as int."""
    return regs[operand] if operand in regs else int(operand)


def emits_clock_signal(prog: list[list[str]], initial_a: int) -> bool:
    """True if starting with a = initial_a outputs 0, 1, 0, 1, ... forever.

    The machine is deterministic, so if it reaches an `out` in exactly the
    same state twice, it will repeat that cycle forever, and every output
    in the cycle has already been checked. That proves the signal is correct.
    """
    regs = dict.fromkeys(REGISTERS, 0)
    regs["a"] = initial_a
    ip = 0
    expected = 0                              # The next bit the signal must send
    seen: set[tuple[int, ...]] = set()

    while 0 <= ip < len(prog):
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
                    continue                  # Jumped: skip the ip += 1 below
            case ["out", x]:
                if _resolve(regs, x) != expected:
                    return False              # Wrong bit: not a clock signal
                # Same instruction, registers and expected bit as before: a cycle
                state = (ip, *regs.values(), expected)
                if state in seen:
                    return True
                seen.add(state)
                expected ^= 1                 # Alternate 0 <-> 1
            case _:
                pass                          # Invalid instruction: skip it
        ip += 1

    return False                              # Program halted: not an endless signal


def find_clock_seed(prog: list[list[str]]) -> int:
    """Lowest positive value for register a that produces 0, 1, 0, 1, ..."""
    return next(a for a in count(1) if emits_clock_signal(prog, a))


program = parse_program(get_data(day=25, year=2016))
print(f"Part 1: {find_clock_seed(program)}")
