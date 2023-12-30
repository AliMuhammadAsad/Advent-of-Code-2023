import math
from enum import Enum

class Ordering(Enum):
    normal = "AKQJT98765432"
    jokers = "AKQT98765432J"

def entropy(hcards):
    probabilities = [hcards.count(c) / len(hcards) for c in set(hcards)]
    entropy_val = -sum(p * math.log(p) for p in probabilities)
    return entropy_val

def entropy_with_jokers(hcards):
    try:
        top = sorted(hcards.replace("J", ""), key=lambda c: hcards.count(c))[-1]
        return entropy(hcards.replace("J", top))
    except IndexError:
        return entropy(hcards)

with open("inp7.txt") as src:
    hands = [(hand, int(bid)) for hand, bid in map(str.split, src)]

total_part1 = sum((len(hands) - i) * bid for i, (__, bid) in enumerate(sorted(
    hands, key=lambda h: (entropy(h[0]), *map(Ordering.normal.value.index, h[0]))
)))

total_part2 = sum((len(hands) - i) * bid for i, (__, bid) in enumerate(sorted(
    hands, key=lambda h: (entropy_with_jokers(h[0]), *map(Ordering.jokers.value.index, h[0]))
)))

print("Part 1:", total_part1)
print("Part 2:", total_part2)
