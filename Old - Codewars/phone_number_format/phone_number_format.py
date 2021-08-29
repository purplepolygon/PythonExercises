#!/usr/bin/env python3
# convert a phone number list to a formatted number


def format_phone_number(phone_number_list):
    strings_of_ints = [str(int) for int in phone_number_list]
    joined_ints = "".join(strings_of_ints)
    formatted_phone_number = "(" + joined_ints[:3] + ")" + " " + joined_ints[3:6] + "-" + joined_ints[6:10]
    print(formatted_phone_number)
    return formatted_phone_number


if __name__ == '__main__':
    format_phone_number([3, 4, 6, 2, 3, 5, 1, 2, 9, 0])  # (346) 235-1290
