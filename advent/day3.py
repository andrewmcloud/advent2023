import re
import math


def get_adjacent_numbers(index: int, num_map: dict[int, str], row_len: int) -> list[int]:
    row = index // row_len
    col = index % row_len
    seen = set()
    seen.add(num_map.get((row - 1) * row_len + col, None))  # up
    seen.add(num_map.get((row + 1) * row_len + col, None))  # down
    seen.add(num_map.get(row * row_len + col - 1, None))  # left
    seen.add(num_map.get(row * row_len + col + 1, None))  # right
    seen.add(num_map.get((row - 1) * row_len + col - 1, None))  # up left
    seen.add(num_map.get((row + 1) * row_len + col - 1, None))  # down left
    seen.add(num_map.get((row - 1) * row_len + col + 1, None))  # up right
    seen.add(num_map.get((row + 1) * row_len + col + 1, None))  # down right
    return [int(x) for x in seen if x is not None]


with open("../input/day3.txt", "r") as f:
    input_ = f.read()

matrix = [[i for i in line] for line in input_.split("\n")]
row_len = len(matrix[0])
cleaned_input = input_.replace("\n", "")
index_num_tuple = [(m.start(), m.group(0)) for m in re.finditer(r"\d+", cleaned_input)]
index_gear_tuple = [(m.start(), m.group(0)) for m in re.finditer(r"\*", cleaned_input)]
index_symbol_tuple = [(m.start(), m.group(0)) for m in re.finditer(r"[\*\+\$\#\!\@()%^&\-+=\/]", cleaned_input)]

index_map = {t[0] + j: t[1] for t in index_num_tuple for j in range(len(t[1]))}
part1 = sum(sum(get_adjacent_numbers(symbol[0], index_map, row_len)) for symbol in index_symbol_tuple)
part2 = 0
for gear in index_gear_tuple:
    nums = get_adjacent_numbers(gear[0], index_map, row_len)
    part2 += math.prod(nums) if len(nums) == 2 else 0


print(f"day2:\npart 1: {part1}\npart 2: {part2}")
