def get_positive_integer(message):
    while True:
        value = input(message)

        try:
            number = int(value)

            if number > 0:
                return number

            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")
