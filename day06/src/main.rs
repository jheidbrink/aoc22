use core::panic;
use std::collections::HashSet;
use std::fs;

fn main() {
    let input = read_input();
    println!("Solution for part 1: {}", detect_start_of_packet(&input));
}

fn read_input() -> String {
    fs::read_to_string("input").unwrap()
}


fn detect_start_of_packet(input: &str) -> usize {
    // finds the first character position where the four previous characters are all different
    for i in 4..input.len() {
        let characters: HashSet<char> = HashSet::from_iter(input[i - 4..i].chars());
        if characters.len() == 4 {
            //println!("Characters are all different: {}", input[i-4..i].chars().as_str());
            return i;
        } else {
            //println!("Characters are not all different: {}", input[i-4..i].chars().as_str());
        }
    };
    panic!("Could not find start of packet");
}

mod tests {
    use super::*;

    #[test]
    fn test_detect_start_of_packet() {
        assert_eq!(detect_start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5);
        assert_eq!(detect_start_of_packet("nppdvjthqldpwncqszvftbrmjlhg"), 6);
        assert_eq!(detect_start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10);
        assert_eq!(detect_start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11);
    }
}