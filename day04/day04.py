#!/usr/bin/env python

def read_input() -> str:
    with open('input', encoding='utf8') as fh:
        return fh.read()

class Section:
    def __init__(self, lower: int, upper: int):
        assert upper >= lower
        self.lower = lower
        self.upper = upper

    def __contains__(self, other: "Section"):
        return other.lower >= self.lower and other.upper <= self.upper

    @staticmethod
    def parse(input_: str) -> "Section":
        lower, upper = input_.split('-')
        return Section(int(lower), int(upper))

def count_overlaps(input_lines: list[str]) -> int:
    return len([1 for line in input_lines if sections_overlap(line)])

def sections_overlap(line: str) -> bool:
    left, right = parse_line(line)
    return (left in right) or (right in left)

def parse_line(line: str) -> tuple[Section, Section]:
    left, right = line.split(',')
    return (Section.parse(left), Section.parse(right))

def main():
    input_lines = read_input().splitlines()
    data = {
        'part 1': count_overlaps(input_lines),
        'part 2': None,
    }
    print(data)

if __name__ == "__main__":
    main()
