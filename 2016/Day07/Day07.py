# Advent of Code 2016, Day 7: Internet Protocol Version 7
import re
from aocd import get_data

lines = get_data(day=7, year=2016).strip().splitlines()

def split_ip(line):
    """Split on [ and ]: the pieces alternate outside, inside, outside, ...
    (Brackets are never nested in this input.)"""
    parts = re.split(r'[\[\]]', line)
    return parts[0::2], parts[1::2]       # (supernets, hypernets)

def has_abba(s):
    # (.)  any character, then (?!\1) "next isn't that same character",
    # then (.) a second character, then the pair mirrored: \2\1
    return re.search(r'(.)(?!\1)(.)\2\1', s) is not None

def abas(s):
    """Every ABA in s as an (a, b) pair. zip steps one character at a
    time, so overlapping ABAs like 'zazaz' are all found."""
    return {(x, y) for x, y, z in zip(s, s[1:], s[2:]) if x == z != y}

def supports_tls(line):
    outside, inside = split_ip(line)
    return any(map(has_abba, outside)) and not any(map(has_abba, inside))

def supports_ssl(line):
    outside, inside = split_ip(line)
    aba = set().union(*map(abas, outside))
    # A BAB inside matches an ABA outside when its flipped pair is the same.
    bab = {(b, a) for a, b in set().union(*map(abas, inside))}
    return bool(aba & bab)                # Any pair in common?

print(f"Part 1: {sum(map(supports_tls, lines))}")
print(f"Part 2: {sum(map(supports_ssl, lines))}")
