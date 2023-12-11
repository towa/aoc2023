from dataclasses import dataclass
from rich import print


@dataclass
class Map:
    source: int
    destination: int
    range: int


@dataclass
class Map2:
    range_from: int
    range_to: int
    diff: int


@dataclass
class Mapping:
    source_name: str
    destination_name: str
    maps: list[Map]


def map_number(maps: list[Map], number: int) -> int:
    for m in maps:
        if number in range(m.source, m.source + m.range):
            return m.destination + number - m.source
    return number


def map_number_reversed(maps: list[Map], number: int) -> int:
    for m in maps:
        if number in range(m.destination, m.destination + m.range):
            return m.source - m.destination + number
    return number


def get_mappings(input: list[str]) -> dict[Mapping]:
    i = 1
    mappings = {}
    while i < len(input):
        line = input[i]
        if ":" in line:
            src_name = line.split()[0].split("-")[0]
            dst_name = line.split()[0].split("-")[2]
            maps = []
            while i + 1 < len(input) and len(input[i+1].split()) == 3:
                i += 1
                line = input[i]
                maps.append(Map(
                    destination=int(line.split()[0]),
                    source=int(line.split()[1]),
                    range=int(line.split()[2]),
                ))
            mappings.update({
                src_name: Mapping(src_name, dst_name, maps),
            })
        i += 1
    return mappings


def mappings_to_maplist(mappings: dict[Mapping]) -> list[list[Map]]:
    map_list = [mappings["seed"].maps]
    dst = mappings["seed"].destination_name
    while mappings.get(dst):
        map_list.append(mappings.get(dst).maps)
        dst = mappings.get(dst).destination_name
    return map_list


def get_final_seeds(map_list: list[list[Map]], seeds: list[int]) -> list[int]:
    res_seeds = []
    for seed in seeds:
        res = seed
        for maps in map_list:
            res = map_number(maps, res)
        res_seeds.append(res)
    return res_seeds


def get_input_seed(map_list: list[list[Map]], output) -> int:
    res = output
    for maps in map_list[::-1]:
        res = map_number_reversed(maps, res)
    return res


def get_min_out(map_list: list[list[Map]]) -> Map:
    return sorted(
        map_list[-1],
        key=lambda x: x.destination)[0]


def in_range_list(range_list, i: int) -> bool:
    for r in range_list:
        if i in r:
            return True
    return False


def solve1(input: list[str]) -> int:
    seeds = [int(x) for x in input[0].split(":")[1].split()]

    map_list = mappings_to_maplist(get_mappings(input))
    res_seeds = get_final_seeds(map_list, seeds)

    return min(res_seeds)


def solve2(input: list[str]) -> int:
    # TODO find faster way
    raw_seeds = [int(x) for x in input[0].split(":")[1].split()]
    seed_ranges = [
        range(raw_seeds[i], raw_seeds[i] + raw_seeds[i+1])
        for i in range(0, len(raw_seeds), 2)
    ]
    map_list = mappings_to_maplist(get_mappings(input))

    i = 0
    input_seed = get_input_seed(map_list, i)
    while not in_range_list(seed_ranges, input_seed):
        i += 1
        if i % 100000 == 0:
            print(i)
        input_seed = get_input_seed(map_list, i)
    return i
