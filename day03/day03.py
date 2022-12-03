#!/usr/bin/env python

def readfile(filename) -> str:
    with open(filename, encoding='utf8') as fh:
        return fh.read()

def split_string_in_two(input_: str) -> tuple[str, str]:
    assert len(input_) % 2 == 0
    middle = int(len(input_) / 2)
    return input_[:middle], input_[middle:]

#def items_in_compartment(compartment: str) -> set:
#    """
#    >>> parse_compartment("abcbdd")
#    {'a', 'b', 'c', 'd'}
#    """
#    return set(compartment)

def sum_of_priorities(input_lines: list[str]) -> int:
    return sum([priority(common_item(line)) for line in input_lines])

def common_item(line: str) -> str:
    compartment1, compartment2 = split_string_in_two(line)
    intersection = set(compartment1).intersection(set(compartment2))
    assert len(intersection) == 1
    return next(iter(intersection))

def chunks_of_three(lines: list):
    for i in range(0, len(lines), 3):
        yield lines[i:i+3]

def sum_of_group_badge_priorities(input_lines: list[str]) -> int:
    return sum([priority(badge(group)) for group in chunks_of_three(input_lines)])

def badge(group: list[str]) -> str:
    assert len(group) == 3
    intersection = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
    assert len(intersection) == 1
    badge = next(iter(intersection))
    assert len(badge) == 1
    return badge

def priority(item: str) -> int:
    assert len(item) == 1
    if ord('a') <= ord(item) <= ord('z'):
        return ord(item) - ord('a') + 1
    if ord('A') <= ord(item) <= ord('Z'):
        return ord(item) - ord('A') + 27
    raise ValueError("item should be a-z or A-Z")

def main():
    input_lines = readfile("day03_input").splitlines()
    data = {
        'part 1': sum_of_priorities(input_lines),
        'part 2': sum_of_group_badge_priorities(input_lines),
    }
    print(data)

if __name__ == "__main__":
    main()
