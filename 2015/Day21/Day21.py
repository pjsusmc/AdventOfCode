# Advent of Code 2015, Day 21: RPG Simulator 20XX
from itertools import combinations, product

# Shop items: (cost, damage, armor)
WEAPONS = [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]

# Armor is optional, so include a zero-cost "none" option.
ARMOR = [(0, 0, 0), (13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5)]

# Rings: 0, 1 or 2, all different. Two zero-cost placeholders let
# combinations(RINGS, 2) cover every case, including no rings.
RINGS = [(0, 0, 0), (0, 0, 0),
         (25, 1, 0), (50, 2, 0), (100, 3, 0),
         (20, 0, 1), (40, 0, 2), (80, 0, 3)]

PLAYER_HP = 100
BOSS_HP, BOSS_DAMAGE, BOSS_ARMOR = 100, 8, 2   # From the puzzle input

def turns_to_kill(hp, damage):
    """Turns needed to bring hp to 0: hp / damage, rounded up."""
    return -(-hp // damage)

def player_wins(damage, armor):
    # Every hit does at least 1 damage.
    player_turns = turns_to_kill(BOSS_HP, max(1, damage - BOSS_ARMOR))
    boss_turns = turns_to_kill(PLAYER_HP, max(1, BOSS_DAMAGE - armor))
    return player_turns <= boss_turns   # Player hits first, so a tie is a win

wins, losses = [], []
for weapon, armor, (ring1, ring2) in product(WEAPONS, ARMOR, combinations(RINGS, 2)):
    # Add up each column: total cost, total damage, total armor
    cost, damage, defense = map(sum, zip(weapon, armor, ring1, ring2))
    if player_wins(damage, defense):
        wins.append(cost)
    else:
        losses.append(cost)

print(f"Part 1: {min(wins)}")
print(f"Part 2: {max(losses)}")
