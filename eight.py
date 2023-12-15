from dataclasses import dataclass
from rich import print
from math import lcm


@dataclass
class Element():
    left: str
    right: str


def populate_dict(input: list[str]) -> dict:
    ele_dict = {}
    for line in input[2:]:
        element_name = line.split("=")[0].strip()
        elements = line.replace(" ", "").replace("(", "").replace(
            ")", "").split("=")[1].split(",")
        ele_dict.update({
            element_name: Element(elements[0], elements[1])
        })
    return ele_dict


def solve1(input: list[str]) -> int:
    instructions = input[0]

    ele_dict = populate_dict(input)
    current_element = "AAA"
    i = 0

    while current_element != "ZZZ":
        instr = instructions[i % len(instructions)]
        if instr == "L":
            current_element = ele_dict[current_element].left
        else:
            current_element = ele_dict[current_element].right
        i += 1

    return i


def solve2(input: list[str]) -> int:
    instructions = input[0]
    ele_dict = populate_dict(input)

    current_elements = [e for e in ele_dict.keys() if e.endswith("A")]

    diffs = []
    for e in current_elements:
        current_element = e
        i = 0
        last_i = 0
        diff = None
        while True:
            instr = instructions[i % len(instructions)]
            if instr == "L":
                current_element = ele_dict[current_element].left
            else:
                current_element = ele_dict[current_element].right
            i += 1
            if current_element.endswith("Z"):
                if diff and diff == i - last_i:
                    diffs.append(diff)
                    print(e, current_element, diff)
                    break
                else:
                    diff = i - last_i
                    last_i = i

    return lcm(*diffs)
