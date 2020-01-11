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


def get_human_choice() -> Option:
    return Option(int(input('Enter the number of your choice: ')))


def get_computer_choice():
    return random.choice(list(Option))


def print_options():
    print('\n'.join(f'({opt.value}) {opt.name.title()}' for opt in Option))


def play():
    print_options()

    human_choice = get_human_choice()
    print(f'You chose {human_choice}')

    computer_choice = get_computer_choice()
    print(f'The computer chose {computer_choice}')

    if human_choice.beats(computer_choice):
        print(f'Yes, {human_choice} beat {computer_choice}!')
    elif computer_choice.beats(human_choice):
        print(f'Sorry, {computer_choice} beat {human_choice}')
    else:
        print('Draw!')


if __name__ == '__main__':
    play()
