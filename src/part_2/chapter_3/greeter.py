import datetime


def day():
    """Returns the current day, e.g. Sunday."""
    return datetime.datetime.now().strftime('%A')


def part_of_day():
    """Return current part of the day, e.g. morning."""
    current_hour = datetime.datetime.now().hour
    if current_hour < 12:
        part_of_the_day = 'morning'
    elif current_hour == 12:
        part_of_the_day = 'afternoon'
    else:
        part_of_the_day = 'evening'
    return part_of_the_day


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store: str):
        print(f'Hi, my name is {self.name}, and welcome to {store}!')
        print(f'How’s your {day()} {part_of_day()} going?')
        print('Here’s a coupon for 20% off!')


if __name__ == '__main__':
    greeter = Greeter('Pavel')
    greeter.greet('Awesome-Store')
