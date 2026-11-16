with open('input.txt') as f:
    data = [line.strip() for line in f if line.strip()]

# Part 1: Code length minus evaluated memory length
part1_total = sum(len(line) - len(eval(line)) for line in data)

# Part 2: Newly encoded length minus original code length
part2_total = sum(2 + line.count('\\') + line.count('"') for line in data)

print(f"Part 1 Result: {part1_total}")
print(f"Part 2 Result: {part2_total}")
