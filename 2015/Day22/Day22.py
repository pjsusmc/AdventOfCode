# Advent of Code 2015, Day 22: Wizard Simulator 20XX
import heapq
import re

# Boss stats from the puzzle input: "Hit Points: 55" and "Damage: 8"
with open('input.txt') as f:
    BOSS_HP, BOSS_DAMAGE = map(int, re.findall(r'\d+', f.read()))

PLAYER_HP = 50
PLAYER_MANA = 500

# Spell costs
MISSILE, DRAIN, SHIELD, POISON, RECHARGE = 53, 73, 113, 173, 229


def apply_effects(mana, boss, shield, poison, recharge):
    """Run active effects at the start of a turn.
    Returns updated values plus the armor in force this turn."""
    armor = 7 if shield else 0
    if poison:
        boss -= 3
    if recharge:
        mana += 101
    # Each active timer counts down by one; 0 means the effect has ended.
    return (mana, boss,
            max(shield - 1, 0), max(poison - 1, 0), max(recharge - 1, 0),
            armor)


def least_mana(hard=False):
    """Lowest total mana that wins the fight.

    Dijkstra's algorithm: always expand the cheapest game state so far.
    The first winning state taken off the heap is the cheapest win."""
    # State: (mana spent, player hp, mana, boss hp, shield, poison, recharge)
    heap = [(0, PLAYER_HP, PLAYER_MANA, BOSS_HP, 0, 0, 0)]
    seen = set()

    while heap:
        spent, hp, mana, boss, shield, poison, recharge = heapq.heappop(heap)

        if boss <= 0:              # A winning state: cheapest, since it's first
            return spent

        state = (hp, mana, boss, shield, poison, recharge)
        if state in seen:          # Already reached this state more cheaply
            continue
        seen.add(state)

        # ---- Player's turn ----
        if hard:                   # Part 2: lose 1 HP before anything else
            hp -= 1
            if hp <= 0:
                continue

        mana, boss, shield, poison, recharge, _ = apply_effects(
            mana, boss, shield, poison, recharge)
        if boss <= 0:              # Poison finished the boss: no spell needed
            heapq.heappush(heap, (spent, hp, mana, boss, 0, 0, 0))
            continue

        # Try each spell we can afford. Effect spells can't be cast while
        # that effect is still active (its timer is above 0).
        options = []
        if mana >= MISSILE:
            options.append((MISSILE, hp, boss - 4, shield, poison, recharge))
        if mana >= DRAIN:
            options.append((DRAIN, hp + 2, boss - 2, shield, poison, recharge))
        if mana >= SHIELD and not shield:
            options.append((SHIELD, hp, boss, 6, poison, recharge))
        if mana >= POISON and not poison:
            options.append((POISON, hp, boss, shield, 6, recharge))
        if mana >= RECHARGE and not recharge:
            options.append((RECHARGE, hp, boss, shield, poison, 5))
        # No affordable spell means we lose, so this state adds nothing.

        for cost, p_hp, b_hp, s, p, r in options:
            m = mana - cost
            total = spent + cost

            if b_hp <= 0:          # The spell itself killed the boss
                heapq.heappush(heap, (total, p_hp, m, b_hp, s, p, r))
                continue

            # ---- Boss's turn ----
            m, b_hp, s, p, r, armor = apply_effects(m, b_hp, s, p, r)
            if b_hp <= 0:          # Effects killed the boss
                heapq.heappush(heap, (total, p_hp, m, b_hp, s, p, r))
                continue

            p_hp -= max(1, BOSS_DAMAGE - armor)   # Boss hits, at least 1
            if p_hp > 0:                          # Still alive: keep searching
                heapq.heappush(heap, (total, p_hp, m, b_hp, s, p, r))

    return None                    # No way to win


print(f"Part 1: {least_mana()}")
print(f"Part 2: {least_mana(hard=True)}")
