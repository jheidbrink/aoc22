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
        'part 1': sum_of_priorities(input_lines)
    }
    print(data)

if __name__ == "__main__":
    main()
