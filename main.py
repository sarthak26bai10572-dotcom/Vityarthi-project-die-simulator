from dice import create_dice
from simulator import run_simulation
from display import show_menu, show_results
from input_helper import get_positive_integer


def main():
    print("\nMULTIPLE DIE ROLLING SIMULATOR")
    print("--------------------------------")

    number_of_dice = get_positive_integer("Enter number of dice: ")
    number_of_sides = get_positive_integer("Enter number of sides on each die: ")
    number_of_rolls = get_positive_integer("Enter number of rolls: ")

    dice = create_dice(number_of_dice, number_of_sides)

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            results = run_simulation(dice, number_of_rolls)
            show_results(results, number_of_dice, number_of_sides)
        elif choice == "2":
            print("\nProject: Multiple Die Rolling Simulator")
            print("This program simulates rolling several dice many times.")
        elif choice == "3":
            print("\nProgram ended. Thank you!")
            break
        else:
            print("\nPlease enter 1, 2 or 3.")


if __name__ == "__main__":
    main()
