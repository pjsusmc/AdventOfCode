# Advent of Code 2015, Day 10: Elves Look, Elves Say
from itertools import groupby

def look_and_say(s):
    """Describe each run of identical digits as count + digit.
    groupby splits '1113' into runs ('1', '111') and ('3', '3'),
    giving '3113'."""
    return ''.join(f"{len(list(run))}{digit}" for digit, run in groupby(s))

seq = '1113222113'

for step in range(1, 51):   # Steps 1 to 50
    seq = look_and_say(seq)
    if step == 40:
        print(f"Part 1: {len(seq)}")

print(f"Part 2: {len(seq)}")
