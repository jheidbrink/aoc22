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

def parse_hand(character: str) -> Hand:
    assert character in ("A", "B", "C")
    return {"A": Hand.ROCK, "B": Hand.PAPER, "C": Hand.SCISSORS, "X": Hand.ROCK, "Y": Hand.PAPER, "Z": Hand.SCISSORS}[character]

def parse_result(character: str) -> GameResult:
    assert character in ("X", "Y", "Z")
    return {"X": GameResult.LOSE, "Y": GameResult.DRAW, "Z": GameResult.WIN}[character]

def parse_line(line: str) -> tuple[Hand, GameResult]:
    encoded_hand, encoded_result = line.split(' ')
    return (parse_hand(encoded_hand), parse_result(encoded_result))

def parse_input(contents: str) -> list[tuple[Hand, GameResult]]:
    return [parse_line(line) for line in contents.splitlines()]

def player_hand(opponent_hand: Hand, result: GameResult) -> Hand:
    if result == GameResult.DRAW:
        return opponent_hand
    if result == GameResult.WIN:
        return Hand((opponent_hand.value + 1) % 3)
    return Hand((opponent_hand.value + 2) % 3)

def score(opponent_hand: Hand, result: GameResult) -> int:
    p_hand = player_hand(opponent_hand, result)
    return {GameResult.WIN: 6, GameResult.DRAW: 3, GameResult.LOSE: 0}[result] + {Hand.ROCK: 1, Hand.PAPER: 2, Hand.SCISSORS: 3}[p_hand]

def main():
    games: list[tuple[Hand, GameResult]] = parse_input(readfile('day2_input'))
    result = sum([score(game[0], game[1]) for game in games])
    print(result)

if __name__ == "__main__":
    main()
