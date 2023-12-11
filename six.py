def compute(time: list[int], distance: list[int]) -> int:
    res = 1
    for t, d in zip(time, distance):
        dist = [i * (t - i) for i in range(t)]
        res *= len([x for x in dist if x > d])
    return res


def solve1(input: list[str]) -> int:
    time = [int(x) for x in input[0].split(":")[1].split()]
    distance = [int(x) for x in input[1].split(":")[1].split()]

    return compute(time, distance)


def solve2(input: list[str]) -> int:
    time = [int(input[0].replace(" ", "").split(":")[1])]
    distance = [int(input[1].replace(" ", "").split(":")[1])]

    return compute(time, distance)
