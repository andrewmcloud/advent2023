import re

with open("../input/day1.txt", "r") as f:
    input_ = f.read()

# part 1
total_p1 = 0
for line in input_.split("\n"):
    numbers = re.findall(r"\d", line)
    total_p1 += int(numbers[0] + numbers[-1])

# part 2
pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))"
lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

total_p2 = 0
for line in input_.split("\n"):
    numbers = re.findall(re.compile(pattern), line)
    total_p2 += int(lookup.get(numbers[0], numbers[0]) + lookup.get(numbers[-1], numbers[-1]))

print(f"day1:\npart 1: {total_p1}\npart 2: {total_p2}")
