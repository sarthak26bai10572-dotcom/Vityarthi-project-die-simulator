def roll_all_dice(dice):
    roll_values = []

    for die in dice:
        roll_values.append(die.roll())

    return roll_values


def run_simulation(dice, number_of_rolls):
    results = []

    for i in range(number_of_rolls):
        one_roll = roll_all_dice(dice)
        total = sum(one_roll)
        results.append(total)

    return results
