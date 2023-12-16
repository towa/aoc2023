def next_value(hist: list[int]) -> int:
    if [x for x in hist if x != 0]:
        diff = [b - a for a, b in zip(hist[0:-1], hist[1:])]
        return next_value(diff) + hist[-1]
    else:
        return 0


def prev_value(hist: list[int]) -> int:
    if [x for x in hist if x != 0]:
        diff = [b - a for a, b in zip(hist[0:-1], hist[1:])]
        return hist[0] - prev_value(diff)
    else:
        return 0


def solve1(input: list[str]) -> int:
    res = 0
    for line in input:
        hist = [int(x) for x in line.split()]
        res += next_value(hist)
    return res


def solve2(input: list[str]) -> int:
    res = 0
    for line in input:
        hist = [int(x) for x in line.split()]
        res += prev_value(hist)
    return res
