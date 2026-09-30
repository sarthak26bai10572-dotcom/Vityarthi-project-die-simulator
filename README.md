# Multiple Die Rolling Simulator

## Overview

The Multiple Die Rolling Simulator is a beginner-level Python command-line project. It allows a user to choose the number of dice, the number of sides on each die, and the number of times the dice should be rolled.

After the simulation, the program displays basic statistics such as minimum total, maximum total, average total, standard deviation, and frequency of each total.

The project is intentionally written using simple Python concepts such as functions, a small class, lists, loops, dictionaries, input validation, and the `random` and `math` modules.

## Features

1. Select the number of dice.
2. Select the number of sides on each die.
3. Select the number of rolls.
4. Generate random dice results.
5. Calculate the total for every roll.
6. Find minimum, maximum and average values.
7. Calculate standard deviation.
8. Show how often each total occurred.
9. Handle invalid user input.

## Technologies Used

- Python 3
- `random` module
- `math` module
- Command Line Interface
- Git and GitHub

No JSON or external packages are used.

## Project Structure

```text
Multiple_Die_Rolling_Simulator/
│
├── main.py
├── dice.py
├── simulator.py
├── statistics.py
├── display.py
├── input_helper.py
├── statement.md
├── README.md
├── results.txt
└── tests/
    └── test_project.py
```

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal inside the project folder.
4. Run:

```bash
python main.py
```

5. Enter the number of dice, number of sides and number of rolls.

## How to Test

Run:

```bash
python -m unittest discover -s tests
```

The test file checks important parts of the program such as mean calculation, minimum/maximum calculation, frequency counting and input-related logic.

## Example

```text
MULTIPLE DIE ROLLING SIMULATOR
--------------------------------
Enter number of dice: 2
Enter number of sides on each die: 6
Enter number of rolls: 20

1. Run simulation
2. About project
3. Exit
Enter your choice: 1

SIMULATION RESULTS
------------------
Total rolls: 20
Minimum total: 2
Maximum total: 12
Average total: 7.10
Standard deviation: 2.65

Frequency of totals:
2 -> 1 time(s)
3 -> 2 time(s)
...
12 -> 1 time(s)
```

Because dice are random, actual results will be different each time.

## Notes

This is a basic educational project. It focuses on understanding Python functions, classes, loops, lists, dictionaries, modules and simple error handling.
