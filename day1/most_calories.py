#!/usr/bin/env python

calory = int
foods = list[calory]


def read_elves() -> list[foods]:
    with open('day1_input', encoding='utf-8') as fh:
        contents = fh.read()
    elves: list[foods] = []
    current_elf: foods = []
    for line in contents.splitlines():
        if not line.strip():
            elves.append(current_elf)
            current_elf = []
        else:
            current_elf.append(int(line.strip()))
    return elves


def elf_with_most_calories(elves: list[foods]) -> int:
    return max([sum(all_foods) for all_foods in elves])

def calories_carried_by_top_three_elves(elves: list[foods]) -> int:
    total_calories = sorted([sum(foods) for foods in elves], reverse=True)
    return sum(total_calories[:3])


def main():
    elves = read_elves()
    most_calories = elf_with_most_calories(elves)
    print(most_calories)
    print(calories_carried_by_top_three_elves(elves))


if __name__ == "__main__":
    main()
