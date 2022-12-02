#!/usr/bin/env python

from enum import Enum

class Hand(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class GameResult(Enum):
    LOSE = 0
    DRAW = 1
    WIN = 2

def readfile(filename: str) -> str:
    with open(filename, encoding='utf8') as fh:
        return fh.read()

def parse_character(character: str) -> Hand:
    assert character in "ABCXYZ"
    return {"A": Hand.ROCK, "B": Hand.PAPER, "C": Hand.SCISSORS, "X": Hand.ROCK, "Y": Hand.PAPER, "Z": Hand.SCISSORS}[character]

def parse_line(line: str) -> tuple[Hand, Hand]:
    opponent_hand, my_hand = (parse_character(c) for c in line.split(' '))
    return (opponent_hand, my_hand)

def parse_input(contents: str) -> list[tuple[Hand, Hand]]:
    return [parse_line(line) for line in contents.splitlines()]

def play(opponent_hand, player_hand) -> GameResult:
    if opponent_hand == player_hand:
        return GameResult.DRAW
    if (opponent_hand, player_hand) in [(Hand.ROCK, Hand.PAPER), (Hand.PAPER, Hand.SCISSORS), (Hand.SCISSORS, Hand.ROCK)]:
        return GameResult.WIN
    return GameResult.LOSE

def score(opponent_hand, player_hand) -> int:
    return {GameResult.WIN: 6, GameResult.DRAW: 3, GameResult.LOSE: 0}[play(opponent_hand, player_hand)] + {Hand.ROCK: 1, Hand.PAPER: 2, Hand.SCISSORS: 3}[player_hand]

def main():
    games: list[tuple[Hand, Hand]] = parse_input(readfile('day2_input'))
    result = sum([score(game[0], game[1]) for game in games])
    print(result)

if __name__ == "__main__":
    main()
