import math


def find_mean(values):
    total = 0

    for value in values:
        total = total + value

    return total / len(values)


def find_minimum(values):
    smallest = values[0]

    for value in values:
        if value < smallest:
            smallest = value

    return smallest


def find_maximum(values):
    largest = values[0]

    for value in values:
        if value > largest:
            largest = value

    return largest


def find_standard_deviation(values):
    mean = find_mean(values)
    total = 0

    for value in values:
        difference = value - mean
        total = total + difference * difference

    variance = total / len(values)
    return math.sqrt(variance)


def count_totals(values):
    counts = {}

    for value in values:
        if value in counts:
            counts[value] = counts[value] + 1
        else:
            counts[value] = 1

    return counts
