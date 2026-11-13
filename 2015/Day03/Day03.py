# Advent of Code 2015, Day 3: Perfectly Spherical Houses in a Vacuum

# How each arrow changes the (x, y) position
moves = {'^': (0, 1), '>': (1, 0), 'v': (0, -1), '<': (-1, 0)}

with open('input.txt') as f:
    directions = f.read().strip()

x, y = 0, 0          # Santa starts at the origin
visited = {(x, y)}   # A set: each house appears once, however many visits

for char in directions:
    dx, dy = moves[char]
    x, y = x + dx, y + dy   # Move first...
    visited.add((x, y))     # ...then record the house he arrives at

print(f"Part 1: {len(visited)}")

# --- Part 2 ---
santa = (0, 0)
robo = (0, 0)
visited = {(0, 0)}   # Both start at the origin

for i, char in enumerate(directions):
    dx, dy = moves[char]
    if i % 2 == 0:   # Even moves are Santa's
        santa = (santa[0] + dx, santa[1] + dy)
        visited.add(santa)
    else:            # Odd moves are Robo-Santa's
        robo = (robo[0] + dx, robo[1] + dy)
        visited.add(robo)

print(f"Part 2: {len(visited)}")
