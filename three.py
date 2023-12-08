import re
from dataclasses import dataclass


def flatten_concatenation(matrix):
    flat_list = []
    for row in matrix:
        flat_list += row
    return flat_list


@dataclass
class Number():
    line: int
    start: int
    end: int
    number: int
    serial: bool = False


@dataclass(eq=True, frozen=True)
class Gear():
    x: int
    y: int


@dataclass
class Number2():
    line: int
    start: int
    end: int
    number: int
    gears: list[Gear]


class Matrix():
    def __init__(self, matrix: list[str]):
        self.matrix = matrix

    def is_valid(self, x: int, y: int) -> bool:
        if x < 0 or x >= len(self.matrix):
            return False
        if y < 0 or y >= len(self.matrix[0]):
            return False
        return self.matrix[x][y] not in "0987654321."

    def is_serial(self, number: Number) -> Number:
        serial = False
        for i in range(number.line - 1, number.line + 2):
            for j in range(number.start - 1, number.end + 1):
                serial = serial or self.is_valid(i, j)
        number.serial = serial
        return number

    def is_gear(self, x: int, y: int) -> bool:
        if x < 0 or x >= len(self.matrix):
            return False
        if y < 0 or y >= len(self.matrix[0]):
            return False
        return self.matrix[x][y] == "*"

    def get_gears(self, number: Number2) -> Number2:
        for i in range(number.line - 1, number.line + 2):
            for j in range(number.start - 1, number.end + 1):
                if self.is_gear(i, j):
                    number.gears.append(Gear(i, j))
        return number


def solve1(input: list[str]):
    nmbrs = [
        Number(idx, m.span()[0], m.span()[1], int(m.group()))
        for idx, line in enumerate(input)
        for m in re.finditer("\d+", line)
    ]

    matrix = Matrix(input)
    nmbrs = [matrix.is_serial(n) for n in nmbrs]
    return sum([n.number for n in nmbrs if n.serial])


def solve2(input: list[str]) -> int:
    nmbrs = [
        Number2(idx, m.span()[0], m.span()[1], int(m.group()), [])
        for idx, line in enumerate(input)
        for m in re.finditer("\d+", line)
    ]
    matrix = Matrix(input)
    nmbrs = [matrix.get_gears(n) for n in nmbrs]
    gears = set(flatten_concatenation([
        n.gears for n in nmbrs
    ]))
    res = 0
    for gear in gears:
        numbers = [n for n in nmbrs if gear in n.gears]
        if len(numbers) == 2:
            res += numbers[0].number * numbers[1].number
    return res
