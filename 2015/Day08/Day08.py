# Advent of Code 2015, Day 8: Matchsticks
import ast

with open('input.txt') as f:
    lines = [line.strip() for line in f if line.strip()]

# Part 1: characters of code minus characters in memory.
# literal_eval decodes the string literal (\\, \", \xHH) without
# running code, unlike eval.
part1 = sum(len(line) - len(ast.literal_eval(line)) for line in lines)

# Part 2: encoding adds 2 surrounding quotes, plus one escaping
# backslash for every existing backslash and double quote.
part2 = sum(2 + line.count('\\') + line.count('"') for line in lines)

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
