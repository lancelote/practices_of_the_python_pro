from __future__ import annotations

import random
from enum import Enum


class Option(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def __str__(self):
        return self.name.lower()

    def beats(self, other: Option):
        return any([
            self is Option.ROCK and other is Option.SCISSORS,
            self is Option.PAPER and other is Option.ROCK,
            self is Option.SCISSORS and other is Option.PAPER
        ])


class Game:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None

    def get_human_choice(self):
        user_input = input('Enter the number of your choice: ')
        self.human_choice = Option(int(user_input))

    def get_computer_choice(self):
        self.computer_choice = random.choice(list(Option))

    def print_options(self):
        print('\n'.join(f'({opt.value}) {opt.name.title()}' for opt in Option))

    def print_choices(self):
        print(f'You chose {self.human_choice}')
        print(f'The computer chose {self.computer_choice}')

    def print_winner(self):
        if self.human_choice.beats(self.computer_choice):
            print(f'Yes, {self.human_choice} beat {self.computer_choice}!')
        elif self.computer_choice.beats(self.human_choice):
            print(f'Sorry, {self.computer_choice} beat {self.human_choice}')
        else:
            print('Draw!')

    def play(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.print_choices()
        self.print_winner()


if __name__ == '__main__':
    game = Game()
    game.play()
