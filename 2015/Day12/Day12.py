# Advent of Code 2015, Day 12: JSAbacusFramework.io
import json

with open('input.txt') as f:
    data = json.load(f)

def total(node, skip_red=False):
    """Add up every number in a JSON structure.
    With skip_red=True, ignore any dictionary that has "red" as a value."""
    if isinstance(node, bool):   # True/False are ints in Python; don't count them
        return 0
    if isinstance(node, int):
        return node
    if isinstance(node, list):
        # A "red" in a list doesn't matter, so add up every item
        return sum(total(item, skip_red) for item in node)
    if isinstance(node, dict):
        if skip_red and 'red' in node.values():
            return 0             # Skip this dictionary and everything inside it
        # Only values can hold numbers; keys are always strings
        return sum(total(v, skip_red) for v in node.values())
    return 0                     # Strings and anything else

print(f"Part 1: {total(data)}")
print(f"Part 2: {total(data, skip_red=True)}")
