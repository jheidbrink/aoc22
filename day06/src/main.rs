use core::panic;
use std::collections::HashSet;
use std::fs;

fn main() {
    let input = read_input();
    println!("Solution for part 1: {}", detect_start_of_packet(&input));
    println!("Solution for part 2: {}", detect_start_of_message(&input));
}

fn read_input() -> String {
    fs::read_to_string("input").unwrap()
}

fn detect_start_of_packet(input: &str) -> usize {
    detect_n_different_characters(input, 4)
}

fn detect_start_of_message(input: &str) -> usize {
    detect_n_different_characters(input, 14)
}

fn detect_n_different_characters(input: &str, n: usize) -> usize {
    // finds the first character position where the n previous characters are all different
    for i in n..input.len() {
        let characters: HashSet<char> = HashSet::from_iter(input[i - n..i].chars());
        if characters.len() == n {
            return i;
        }    };
    panic!("Could not find {} different characters in {}", n, input);
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

    #[test]
    fn test_detect_start_of_message() {
        assert_eq!(detect_start_of_message("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19);
        assert_eq!(detect_start_of_message("bvwbjplbgvbhsrlpgdmjqwftvncz"), 23);
        assert_eq!(detect_start_of_message("nppdvjthqldpwncqszvftbrmjlhg"), 23);
        assert_eq!(detect_start_of_message("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29);
        assert_eq!(detect_start_of_message("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 26);
    }
}