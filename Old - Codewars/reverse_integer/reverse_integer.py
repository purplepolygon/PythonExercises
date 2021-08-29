#!/usr/bin/env python3
# If the solution is > size of a 32 bit integer, return 0


def reverse(x):
    listed = [char for char in str(x)]
    if listed[0] == "-":
        listed.remove(listed[0])
        listed.reverse()
        sol = int("".join(listed)) * -1
        if abs(sol) > 2**31:
            return 0
        else:
            return sol
    else:
        listed.reverse()
        sol = int("".join(listed))
        if sol > 2**31:
            return 0
        else:
            return sol


if __name__ == "__main__":
    print(reverse(1534236469))
