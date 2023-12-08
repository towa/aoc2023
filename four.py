import re
from dataclasses import dataclass


def solve1(input: list[str]):
    res = 0
    for line in input:
        split_up = line.split(":")[1].split("|")
        winning_nmbrs = [int(x) for x in split_up[0].split()]
        given_nmbrs = [int(x) for x in split_up[1].split()]
        res_line = 0
        winning = [wn for wn in winning_nmbrs if wn in given_nmbrs]
        if len(winning) == 1:
            res_line = 1
        if len(winning) > 1:
            res_line = 2 ** (len(winning) - 1)
        res += res_line
    return res


@dataclass
class Scratchcard():
    number: int
    n_wins: int
    copies: int = 1


def solve2(input: list[str]):
    cards = []
    for line in input:
        match = re.search("\d+(?:)", line)
        number = int(match.group())
        split_up = line.split(":")[1].split("|")
        winning_nmbrs = [int(x) for x in split_up[0].split()]
        given_nmbrs = [int(x) for x in split_up[1].split()]
        winning = [wn for wn in winning_nmbrs if wn in given_nmbrs]
        cards.append(Scratchcard(number, len(winning)))

    for i, card in enumerate(cards):
        for _ in range(card.copies):
            for j in range(card.n_wins):
                cards[i+1+j].copies += 1

    return sum([c.copies for c in cards])

