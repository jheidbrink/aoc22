#!/usr/bin/env python

from itertools import groupby
from typing import Optional

calory = int
foods = list[calory]

def parse_line(line: str) -> Optional[calory]:
    try:
        return int(line.strip())
    except ValueError:
        return None

def readfile(filename: str) -> str:
    with open(filename, encoding='utf8') as fh:
        return fh.read()

def parse_input(contents: str) -> list[foods]:
    """
    >>> parse_input('10\\n20\\n\\n100')
    [[10, 20], [100]]
    """
    values: list[Optional[int]] = [parse_line(line) for line in contents.splitlines()]
    return [list(group) for key, group in groupby(values, lambda value: value is None) if not key]

def elf_with_most_calories(elves: list[foods]) -> int:
    return max([sum(all_foods) for all_foods in elves])

def calories_carried_by_top_three_elves(elves: list[foods]) -> int:
    total_calories = sorted([sum(foods) for foods in elves], reverse=True)
    return sum(total_calories[:3])


def main():
    elves: list[foods] = parse_input(readfile('day1_input'))
    print(f"most calories: {elf_with_most_calories(elves)}")
    print(f"calories carried by top 3 elves: {calories_carried_by_top_three_elves(elves)}")


if __name__ == "__main__":
    main()
