import re

with open("../input/day9.txt") as f:
    input_ = f.read()


def solve(line: list[int], part1: bool) -> int:
    if set(line) == {0}:
        return 0
    differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    if part1:
        return line[-1] + solve(differences, True)
    return line[0] - solve(differences, False)


cleaned = [[int(x) for x in re.findall(r"-?\d+", line)] for line in input_.split("\n")]
part1 = sum(solve(row, True) for row in cleaned)
part2 = sum(solve(row, False) for row in cleaned)

print(f"day9:\npart 1: {part1}\npart 2: {part2}")
