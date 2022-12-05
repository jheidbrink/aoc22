use std::fs;
use std::fmt;
use std::str::Lines;
use std::cmp::Reverse;

struct SliceDisplay<'a, T: 'a>(&'a [T]);

impl<'a, T: fmt::Display + 'a> fmt::Display for SliceDisplay<'a, T> {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut first = true;
        for item in self.0 {
            if !first {
                write!(f, ", {}", item)?;
            } else {
                write!(f, "{}", item)?;
            }
            first = false;
        }
        Ok(())
    }
}

fn read_input() -> String {
    fs::read_to_string("day1_input").unwrap()
}

fn parse_input(input: String) -> Vec<Vec<i32>> {
    let elves_str: Vec<String> = input.split("\n\n").map(|x| x.to_string()).collect();
    let elf_str = elves_str.iter().map(|elf_lines| elf_lines.lines());
    elf_str.map(parse_elf).collect()
}

fn parse_elf(input: Lines) -> Vec<i32> {
    input.map(|x| x.parse().unwrap()).collect()
}

fn sum(elves: Vec<Vec<i32>>) -> Vec<i32> {
    elves.iter().map(|calories| calories.iter().sum()).collect()
}

fn main() {
    let contents = read_input();
    let elves = parse_input(contents);
    let mut calories_per_elf: Vec<i32> = sum(elves);
    calories_per_elf.sort_by_key(|w| Reverse(*w));
    println!("Top three elves: {}", SliceDisplay(&calories_per_elf[0..3]));
    let top_three_sum : i32 = calories_per_elf[0..3].iter().sum();
    println!("Sum of top three elves: {}", top_three_sum);
}