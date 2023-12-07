import re
from collections import defaultdict

with open("../input/day4.txt") as f:
    input_ = f.read()

points = 0
card_map: dict[int, int] = defaultdict(int)

for i, line in enumerate(input_.split("\n")):
    card_map[i] += 1
    card, mine = line.split("|")
    winning_numbers: set[str] = set(re.findall(r"\d+", card)[1:])
    my_numbers: set[str] = set(re.findall(r"\d+", mine))
    matches = my_numbers & winning_numbers
    # part 1
    points += 2 ** (len(matches) - 1) if matches else 0
    # part 2
    for _ in range(card_map[i]):
        for j in range(len(matches)):
            card_map[i + j + 1] += 1

print(f"day4:\npart 1: {points}\npart 2: {sum(card_map.values())}")
