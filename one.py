import re
from advent.solver import Solver


class DaySolver(Solver):
    day = 1

    def solve_1(self, input):
        def calib_values(line: str):
            res = []
            for char in line:
                try:
                    res.append(int(char))
                except ValueError:
                    continue
            return res[0] * 10 + res[-1]

        lines = input.split()
        res = [calib_values(str(line)) for line in lines]

        return sum(res)

    def solve_2(self, input):
        def find_numbers(line: str):
            numbers = [
                ("one", "1"),
                ("two", "2"),
                ("three", "3"),
                ("four", "4"),
                ("five", "5"),
                ("six", "6"),
                ("seven", "7"),
                ("eight", "8"),
                ("nine", "9"),
            ]
            res = []
            for idx, number in enumerate(numbers):
                occurences = [
                    i.start()
                    for i in re.finditer(f"({number[0]}|{number[1]})", line)]
                for occ in occurences:
                    res.append((occ, idx+1))
            res.sort(key=lambda x: x[0])
            return res[0][1] * 10 + res[-1][1]
            
        return sum([find_numbers(str(line)) for line in input.split()])
