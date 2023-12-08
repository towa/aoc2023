import re
from advent.solver import Solver


class DaySolver(Solver):
    day = 2

    test_input = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]

    def solve_1(self, input):
        available_cubes = {
            "red": 12,
            "green": 13,
            "blue": 14
        }
        res = 0

        for line in input:
            game_id = int(re.search("(?:)\d+", line).group())
            sets = line.split(":")[-1].split(";")
            valid = True
            for s in sets:
                for clr in ["red", "green", "blue"]:
                    match = re.search(f"\d+(?= {clr})", s)
                    if match and int(match.group()) > available_cubes[clr]:
                        valid = False
            if valid:
                res += game_id
        return res
    
    def solve_2(self, input):
        res = 0
        for line in input:
            sets = line.split(":")[-1].split(";")
            min_clr_game = {
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for s in sets:
                for clr in ["red", "green", "blue"]:
                    match = re.search(f"\d+(?= {clr})", s)
                    if match and int(match.group()) > min_clr_game[clr]:
                        min_clr_game[clr] = int(match.group())
            game_product = 1
            for v in min_clr_game.values():
                game_product *= v
            res += game_product
        return res





