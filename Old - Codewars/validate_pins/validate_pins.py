#!/usr/bin/env python3
# Validate 4 and 6 digit pin numbers


import re


def validate_pin(test_pin):
    if re.match(
        r"^[0-9]{4}\n|^[0-9]{6}\n", test_pin
    ):  # Obscure use case when str contains new line
        print("False")
        return False

    if re.match(r"^[0-9]{4}$|^[0-9]{6}$", test_pin):
        print("True")
        return True

    else:
        print("False")
        return False


if __name__ == "__main__":
    test_pin = input("Input a string to see if it is a 4 or 6 digit pin: ")
    validate_pin(test_pin)
