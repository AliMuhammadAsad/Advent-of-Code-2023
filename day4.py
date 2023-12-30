import re

def load(file):
  with open(file) as f:
    return [row.strip()[row.index(':') + 1:].split('|') for row in f]

def solve(p):
  part1 = 0
  cards = [1] * len(p)
  for card, (winning, have) in enumerate(p):
    winning = set(map(int, re.findall('\d+', winning)))
    have = set(map(int, re.findall('\d+', have)))
    winner = len(have & winning)
    if winner:
      part1 += 2**(winner - 1)
      for n in range(1, winner + 1):
        cards[card + n] += cards[card]
  return part1, sum(cards)

p1, tot = solve(load("inp4.txt"))
print(f'Part 1: {p1}')
print(f'Part 2: {tot}')