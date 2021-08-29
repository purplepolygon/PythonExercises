#!/usr/bin/env python3
# If the solution is > size of a 32 bit integer, return 0. We are reversing an integer, x is an integer.


def reverse(x):
    listed = [char for char in str(x)]
    # For negative numbers
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
    print(reverse(1534236469))  # 0 as the reverse is > 2^31
    print(reverse(13489))
    print(reverse(98411111))
