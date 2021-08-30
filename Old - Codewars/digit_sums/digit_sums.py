#!/usr/bin/env python3
# Sum digits until only one remains.
# ex: 9871 = 9 + 8 + 7 + 1 = 25 = 2 + 5 = 7
# 752 = 7 + 5 + 2 = 14 = 1 + 4 = 5


def digital_root(number):
    digital_root_number = number
    while len(str(digital_root_number)) > 1:
        digital_root_number = sum(
            int(x) for x in str(digital_root_number) if x.isdigit()
        )
    print(
        "Original number: "
        + str(number)
        + " Digital root number: "
        + str(digital_root_number)
    )
    return digital_root_number


if __name__ == "__main__":
    digital_root(9871)
    digital_root(752)
    digital_root(8)
    digital_root(10000000001)
