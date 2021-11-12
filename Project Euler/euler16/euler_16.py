#!usr/bin/env python3
# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
# Looks like we have another freebie since python has big integers built in


def exponential_digit_summer(number, exponent):
    number_to_be_summed = number ** exponent
    digit_sum = sum([int(x) for x in str(number_to_be_summed)])
    return digit_sum


if __name__ == '__main__':
    print(exponential_digit_summer(2, 1000))
    # 1366
