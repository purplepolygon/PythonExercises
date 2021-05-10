#!/usr/bin/env python3
# Sum digits until only one remains.
# ex: 9871 = 9 + 8 + 7 + 1 = 25 = 2 + 5 = 7
# 752 = 7 + 5 + 2 = 14 = 1 + 4 = 5


def digital_root(n):
    while len(str(n)) > 1:
        n = sum(int(x) for x in str(n) if x.isdigit())
    print(n)

digital_root()
