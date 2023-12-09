import re
from itertools import cycle
import math
from typing import Callable

with open("../input/day8.txt") as f:
    input_ = f.read()

instructions, input_graph = input_.split("\n\n")
instruction_iter = cycle(instruction for instruction in instructions)

graph = {}
for node in input_graph.split("\n"):
    parent, left, right = re.findall(r"[A-Z]{3}", node)
    graph[parent] = (left, right)


def traverse_graph(graph: dict[str, tuple[str, str]], node: str, terminate_fn: Callable) -> int:
    steps = 0
    while True:
        steps += 1
        instruction = next(instruction_iter)
        match instruction:
            case "L":
                node = graph[node][0]
            case "R":
                node = graph[node][1]
        if terminate_fn(node):
            return steps


# part 1:
part1 = traverse_graph(graph, "AAA", lambda x: x == "ZZZ")

# part 2:
path_lengths = []
for node in graph:
    if node.endswith("A"):
        path_lengths.append(traverse_graph(graph, node, lambda x: x.endswith("Z")))
part2 = math.lcm(*path_lengths)

print(f"day8:\npart 1: {part1}\npart 2: {part2}")
