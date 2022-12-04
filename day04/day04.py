#!/usr/bin/env python

def read_input() -> str:
    with open('input', encoding='utf8') as fh:
        return fh.read()

class Section:
    def __init__(self, lower: int, upper: int):
        assert upper >= lower
        self.lower = lower
        self.upper = upper

    def __contains__(self, other: "Section") -> bool:
        return other.lower >= self.lower and other.upper <= self.upper

    def partially_in(self, other: "Section") -> bool:
        return (other.lower <= self.lower <= other.upper) or (other.lower <= self.upper <= other.upper)

    @staticmethod
    def parse(input_: str) -> "Section":
        lower, upper = input_.split('-')
        return Section(int(lower), int(upper))

def count_complete_overlaps(input_lines: list[str]) -> int:
    return len([1 for line in input_lines if sections_overlap_completely(line)])

def count_partial_overlaps(input_lines: list[str]) -> int:
    return len([1 for line in input_lines if sections_overlap_partially(line)])

def sections_overlap_completely(line: str) -> bool:
    left, right = parse_line(line)
    return (left in right) or (right in left)

def sections_overlap_partially(line: str) -> bool:
    left, right = parse_line(line)
    return left.partially_in(right) or right.partially_in(left)

def parse_line(line: str) -> tuple[Section, Section]:
    left, right = line.split(',')
    return (Section.parse(left), Section.parse(right))

def main():
    input_lines = read_input().splitlines()
    data = {
        'part 1': count_complete_overlaps(input_lines),
        'part 2': count_partial_overlaps(input_lines),
    }
    print(data)

if __name__ == "__main__":
    main()
