use std::fs;

fn read_input() -> String {
    fs::read_to_string("input").unwrap()
}

#[derive(Debug,PartialEq,Eq)]
struct Move {
    amount: usize,
    from: usize,
    to: usize
}

fn part1(input: String) -> String {
    let input_parts: Vec<&str> = input.split("\n\n").collect();
    assert!(input_parts.len() == 2);
    let input_start = input_parts[0];
    let mut stacks = parse_start(input_start);
    let input_moves = input_parts[1];
    let moves = parse_moves(input_moves);
    for m in moves {
        apply_move(&mut stacks, m)
    }
    return stacks.iter().map(|s| s.last().unwrap()).collect()
}

fn apply_move(configuration: &mut Vec<Vec<char>>, m: Move) {
    for _ in 0..m.amount {
        let c = configuration[m.from - 1].pop().unwrap();
        configuration[m.to - 1].push(c);
    }
}

fn parse_start(input: &str) -> Vec<Vec<char>> {
    let lines: Vec<&str> = input.lines().collect();
    let mut stacks: Vec<Vec<char>> = vec![];
    assert_eq!((lines[0].len() + 1) % 4, 0);
    let amount_stacks = (lines[0].len() + 1) / 4;
    for _ in 0..amount_stacks {
        stacks.push(vec![]);
    };
    for line in lines[0..lines.len() - 1].iter().rev() {
        for i in 0..amount_stacks {
            let crate_mark = match line.chars().nth((i+1) * 4 - 3) {
                Some(c) => c,
                None => panic!("Could not parse line {} of length {}, character position {}", line, line.len(), (i+1) * 4 - 3)
            };
            if crate_mark >= 'A' && crate_mark <= 'Z' {
                stacks[i].push(crate_mark);
            } else {
                assert_eq!(crate_mark, ' ');
            }
        }
    }
    return stacks;
}

fn parse_moves(input: &str) -> Vec<Move> {
    input.lines().map(parse_move).collect()
}

fn parse_move(line: &str) -> Move {
    let split: Vec<&str> = line.split(' ').collect();
    Move {amount: split[1].parse().unwrap(), from: split[3].parse().unwrap(), to: split[5].parse().unwrap()}
}

fn main() {
    let input = read_input();
    println!("Part 1: Top of the Stacks: {}", part1(input));
}

mod tests {
    use super::*;
    #[test]
    fn test_part1() {
        let input_lines: Vec<&str> = vec![
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
            ];
        let input = input_lines.join("\n");
        assert_eq!(part1(input), "CMZ")
    }

    #[test]
    fn test_parse_start() {
        let input_lines: Vec<&str> = vec![
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            ];
        let input = input_lines.join("\n");
        let parsed_lines = parse_start(&input);
        assert_eq!(parsed_lines[0], vec!['Z', 'N']);
        assert_eq!(parsed_lines[1], vec!['M', 'C', 'D']);
        assert_eq!(parsed_lines[2], vec!['P']);
    }
    
    #[test]
    fn test_parse_moves() {
        let input_lines: Vec<&str> = vec![
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2",
            ];
        let input = input_lines.join("\n");
        let parsed_lines = parse_moves(&input);
        assert_eq!(parsed_lines, vec![
            Move { amount: 1, from: 2, to: 1 },
            Move { amount: 3, from: 1, to: 3 },
            Move { amount: 2, from: 2, to: 1 },
            Move { amount: 1, from: 1, to: 2 },
            ]);
    }

    #[test]
    fn test_apply_move() {
        let mut stacks = vec![vec!['A', 'B', 'C'], vec!['D', 'E', 'F'], vec!['G', 'H', 'I']];
        apply_move(&mut stacks, Move { amount: 2, from: 1, to: 2 });
        assert_eq!(stacks, vec![vec!['A'], vec!['D', 'E', 'F', 'C', 'B'], vec!['G', 'H', 'I']]);
    }
}