from dataclasses import dataclass


@dataclass
class Map:
    source: int
    destination: int
    range: int


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


def solve1(input: list[str]) -> int:
    seeds = [int(x) for x in input[0].split(":")[1].split()]

    map_list = mappings_to_maplist(get_mappings(input))
    res_seeds = get_final_seeds(map_list, seeds)

    return min(res_seeds)


def solve2(input: list[str]) -> int:
    raw_seeds = [int(x) for x in input[0].split(":")[1].split()]
    seed_ranges = [
        range(raw_seeds[i], raw_seeds[i] + raw_seeds[i+1])
        for i in range(0, len(raw_seeds), 2)
    ]
    seeds = []

    for r in seed_ranges:
        for seed in r:
            seeds.append(seed)

    res_seeds = get_final_seeds(mappings_to_maplist(get_mappings(input)), seeds)

    return min(res_seeds)