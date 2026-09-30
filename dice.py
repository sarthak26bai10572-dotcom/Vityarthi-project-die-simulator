import random


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


def create_dice(number_of_dice, sides):
    dice = []

    for i in range(number_of_dice):
        dice.append(Die(sides))

    return dice
