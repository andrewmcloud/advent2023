import re

with open("../input/day5.txt", "r") as file:
    input_ = file.read()

seed_inputs, *almanac = input_.split("\n\n")
seeds = [int(x) for x in re.findall(r"\d+", seed_inputs)]
seed_pairs = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]


def build_range_lists(almanac: list[str]) -> list[list[list[int]]]:
    range_lists = []
    for entry in almanac:
        r = []
        for line in entry.split("\n"):
            if re.findall(r"[a-z]", line):
                continue
            r.append([int(x) for x in re.findall(r"\d+", line)])
        range_lists.append(r)
    return range_lists


def find_next(seed: int, range_list: list[list[int]]) -> int:
    for dest_start, source_start, rng_length in range_list:
        if seed > source_start + rng_length - 1 or seed < source_start:
            continue
        return seed + dest_start - source_start
    return seed


def part1(seeds: list[int], range_lists: list[list[list[int]]]) -> int:
    locations = []
    for seed in seeds:
        for i in range(len(range_lists)):
            seed = find_next(seed, range_lists[i])
        locations.append(seed)
    return min(locations)


def part2(seed_pairs: list[list[int]], range_lists: list[list[list[int]]]) -> int:
    for range_list in range_lists:
        next_seeds = []

        while seed_pairs:
            seed_start, seed_end = seed_pairs.pop()
            overlap_found = False
            for dest_start, source_start, rng_length in range_list:
                # find overlapping range
                overlap_start = max(seed_start, source_start)
                overlap_end = min(seed_end, source_start + rng_length)

                # add overlapping range, check left and right bounds for splits
                if overlap_start < overlap_end:
                    next_seeds.append(
                        [overlap_start - source_start + dest_start, overlap_end - source_start + dest_start]
                    )
                    # add left range split
                    if seed_start < overlap_start:
                        seed_pairs.append([seed_start, overlap_start])
                    # add right range split
                    if seed_end > overlap_end:
                        seed_pairs.append([overlap_end, seed_end])
                    overlap_found = True
                    break

            # no overlap—not mapped, add seed—same destination.
            if not overlap_found:
                next_seeds.append([seed_start, seed_end])

        seed_pairs = next_seeds

    return min([seed_pair[0] for seed_pair in seed_pairs])


range_lists = build_range_lists(almanac)
print(f"day5:\npart 1: {part1(seeds, range_lists)}\npart 2: {part2(seed_pairs, range_lists)}")
