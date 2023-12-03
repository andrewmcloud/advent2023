import re
import math


def is_num_touching_symbol(index: int, m: list[list[str]], row_len: int) -> bool:
    row = index // row_len
    col = index % row_len
    neighbors = ""
    neighbors += m[row - 1][col] if row > 0 else "_"  # up
    neighbors += m[row + 1][col] if row + 1 < len(m) else "_"  # down
    neighbors += m[row][col - 1] if col > 0 else "_"  # left
    neighbors += m[row][col + 1] if col + 1 < row_len else "_"  # right
    neighbors += m[row - 1][col - 1] if (row > 0 and col > 0) else "_"  # up left
    neighbors += m[row + 1][col - 1] if (row + 1 < len(m) and col > 0) else "_"  # down left
    neighbors += m[row - 1][col + 1] if (row > 0 and col + 1 < row_len) else "_"  # up right
    neighbors += m[row + 1][col + 1] if (row + 1 < len(m) and col + 1 < row_len) else "_"  # down right
    return True if re.findall(r"[\*\+\$\#\!\@()%^&\-+=\/]", neighbors) else False


def is_gear(index: int, num_map: dict[int, str], row_len: int) -> int:
    row = index // row_len
    col = index % row_len
    seen = set()
    if row > 0:
        seen.add(num_map.get((row - 1) * row_len + col, None))  # up
    if row + 1 < len(m):
        seen.add(num_map.get((row + 1) * row_len + col, None))  # down
    if col > 0:
        seen.add(num_map.get(row * row_len + col - 1, None))  # left
    if col + 1 < row_len:
        seen.add(num_map.get(row * row_len + col + 1, None))  # right
    if row > 0 and col > 0:
        seen.add(num_map.get((row - 1) * row_len + col - 1, None))  # up left
    if row + 1 < len(m) and col > 0:
        seen.add(num_map.get((row + 1) * row_len + col - 1, None))  # down left
    if row > 0 and col + 1 < row_len:
        seen.add(num_map.get((row - 1) * row_len + col + 1, None))  # up right
    if row + 1 < len(m) and col + 1 < row_len:
        seen.add(num_map.get((row + 1) * row_len + col + 1, None))  # down right
    touching = [int(x) for x in seen if x is not None]
    return math.prod(touching) if len(touching) == 2 else 0


def build_number_map(tup_list: list[tuple[int, str]]) -> dict[int, str]:
    index_map = {}
    for t in tup_list:
        for j in range(len(t[1])):
            index_map[t[0] + j] = t[1]
    return index_map


def any_touching_symbol(index_tuple: tuple[int, str], matrix: list[list[str]], row_len: int) -> bool:
    return any(is_num_touching_symbol(index_tuple[0] + i, matrix, row_len) for i in range(len(index_tuple[1])))


with open("../input/day3.txt", "r") as f:
    input_ = f.read()

matrix = [[i for i in line] for line in input_.split("\n")]
row_len = len(matrix[0])
cleaned_input = input_.replace("\n", "")
index_num_tuple = [(match.start(), match.group(0)) for match in re.finditer(r"\d+", cleaned_input)]
index_gear_tuple = [(match.start(), match.group(0)) for match in re.finditer(r"\*", cleaned_input)]

# part 1
part1 = sum(int(num[1]) for num in index_num_tuple if any_touching_symbol(num, matrix, row_len))

# part 2
m = build_number_map(index_num_tuple)
part2 = sum(is_gear(gear[0], m, row_len) for gear in index_gear_tuple)

print(f"day2:\npart 1: {part1}\npart 2: {part2}")
