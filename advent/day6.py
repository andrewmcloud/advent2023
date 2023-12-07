import re
import math

with open("../input/day6.txt") as f:
    input_ = f.read().split("\n")

times = [int(x) for x in re.findall(r"\d+", input_[0])]
distances = [int(x) for x in re.findall(r"\d+", input_[1])]

combined_time = int("".join(re.findall(r"\d+", input_[0])))
combined_distance = int("".join(re.findall(r"\d+", input_[1])))


def find_winning_holds(time: int, distance: int) -> int:
    travel = [i * (time - i) for i in range(time)]
    return sum(t > distance for t in travel)


def solve_quadratic(a: int, b: int, c: int) -> int:
    # ax²+bx + c = 0
    # b±√(b²-4ac))/(2a)
    d = b**2 - (4 * a * c)
    lower_bounds = math.ceil(-b + (math.sqrt(d) / (2 * a)))
    upper_bounds = math.floor(-b - (math.sqrt(d) / (2 * a)))

    return abs(upper_bounds - lower_bounds)


part1 = math.prod(find_winning_holds(times[i], distances[i]) for i in range(len(times)))
part2 = solve_quadratic(1, combined_time, combined_distance)

print(f"day6:\npart 1: {part1}\npart 2: {part2}")
