#!/usr/bin/env python3
# convert a phone number list to a formatted number


def format_phone_number(s):
    sints = [str(int) for int in s]
    soi = "".join(sints)
    formatted = "(" + soi[:3] + ")" + " " + soi[3:6] + "-" + soi[6:10]
    return formatted


format_phone_number([3, 4, 6, 2, 3, 5, 1, 2, 9, 0])