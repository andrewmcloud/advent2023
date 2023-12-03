import re

with open("../input/day2.txt", "r") as f:
    input_ = f.read()

games = {}
for i, game in enumerate(input_.split("\n"), 1):
    games[i] = {
        "red": [int(x) for x in re.findall(r"(\d+) red", game)],
        "green": [int(x) for x in re.findall(r"(\d+) green", game)],
        "blue": [int(x) for x in re.findall(r"(\d+) blue", game)],
    }

part1 = sum(
    game
    for game in games
    if (
        max(games[game]["red"], default=0) <= 12
        and max(games[game]["green"], default=0) <= 13
        and max(games[game]["blue"], default=0) <= 14
    )
)

part2 = sum(
    max(games[game]["red"], default=0) * max(games[game]["green"], default=0) * max(games[game]["blue"], default=0)
    for game in games
)

print(f"day2:\npart 1: {part1}\npart 2: {part2}")
