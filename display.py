from statistics import (
    find_mean,
    find_minimum,
    find_maximum,
    find_standard_deviation,
    count_totals
)


def show_menu():
    print("\n1. Run simulation")
    print("2. About project")
    print("3. Exit")


def show_results(results, number_of_dice, number_of_sides):
    print("\nSIMULATION RESULTS")
    print("------------------")

    print("Total rolls:", len(results))
    print("Minimum total:", find_minimum(results))
    print("Maximum total:", find_maximum(results))
    print("Average total:", round(find_mean(results), 2))
    print("Standard deviation:", round(find_standard_deviation(results), 2))

    print("\nFrequency of totals:")
    counts = count_totals(results)

    keys = list(counts.keys())
    keys.sort()

    for total in keys:
        print(str(total) + " -> " + str(counts[total]) + " time(s)")

    print("\nPossible total range:")
    print(str(number_of_dice) + " to " + str(number_of_dice * number_of_sides))
