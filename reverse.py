#!/usr/bin/env python3

# Created by: Michael Zagon
# Created on: Oct 2021
# This program reverses the user's inputted integers


def main():
    # This function reverses the user's inputted integers

    # Input
    user_input = input("Enter an integer to be reversed: ")
    print("")

    # Process and Output
    try:
        integer = int(user_input)
        numbers = [int(element) for element in str(integer)]
        numbers.reverse()
        print("".join(map(str, numbers)))
    except Exception:
        print("Invalid Input!")

    print("\nDone.")


if __name__ == "__main__":
    main()
