# Advent of Code 2016, Day 21: Scrambled Letters and Hash
from collections import deque
from aocd import get_data


def _letter_rotation(index: int) -> int:
    """Right-rotation steps for 'rotate based on position of letter'."""
    return 1 + index + (index >= 4)          # True counts as 1


def _rotate_by_letter(buf: deque[str], ch: str) -> None:
    buf.rotate(_letter_rotation(buf.index(ch)))


def _unrotate_by_letter(buf: deque[str], ch: str) -> None:
    """Undo _rotate_by_letter: find the starting index that would have moved
    the letter to where it is now, and rotate back by that many steps."""
    n = len(buf)
    now = buf.index(ch)
    starts = [i for i in range(n) if (i + _letter_rotation(i)) % n == now]
    # With 8 letters exactly one start fits. With some lengths (such as the
    # 5-letter example) two starts can land on the same spot, so the
    # operation can't be undone uniquely.
    if len(starts) != 1:
        raise ValueError(f"Can't uniquely undo letter rotation for length {n}")
    buf.rotate(-_letter_rotation(starts[0]))


def apply_line(buf: deque[str], line: str, *, inverse: bool = False) -> None:
    """Apply one instruction to buf in place, or undo it if inverse=True."""
    match line.split():
        case ["swap", "position", x, "with", "position", y]:
            # Swaps undo themselves
            i, j = int(x), int(y)
            buf[i], buf[j] = buf[j], buf[i]

        case ["swap", "letter", a, "with", "letter", b]:
            i, j = buf.index(a), buf.index(b)
            buf[i], buf[j] = buf[j], buf[i]

        case ["rotate", "left" | "right" as direction, x, _]:
            # deque.rotate(n) rotates right; negative n rotates left
            steps = int(x) if direction == "right" else -int(x)
            buf.rotate(-steps if inverse else steps)

        case ["rotate", "based", "on", "position", "of", "letter", ch]:
            (_unrotate_by_letter if inverse else _rotate_by_letter)(buf, ch)

        case ["reverse", "positions", x, "through", y]:
            # Reversing undoes itself
            i, j = int(x), int(y)
            while i < j:
                buf[i], buf[j] = buf[j], buf[i]
                i += 1
                j -= 1

        case ["move", "position", x, "to", "position", y]:
            # Undo a move by moving back the other way
            src, dst = (int(y), int(x)) if inverse else (int(x), int(y))
            ch = buf[src]
            del buf[src]
            buf.insert(dst, ch)

        case _:
            raise ValueError(f"Unrecognized instruction: {line!r}")


def scramble(password: str, instructions: list[str], *, inverse: bool = False) -> str:
    """Scramble password, or unscramble it by undoing each step in reverse order."""
    buf = deque(password)
    for line in reversed(instructions) if inverse else instructions:
        apply_line(buf, line, inverse=inverse)
    return "".join(buf)


instructions = [line for line in get_data(day=21, year=2016).splitlines() if line.strip()]

print(f"Part 1: {scramble('abcdefgh', instructions)}")
print(f"Part 2: {scramble('fbgdceah', instructions, inverse=True)}")
