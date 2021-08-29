#!/usr/bin/env python3
# Take all even valued terms under 1,000,000 in a Fibonacci sequence, and sum them.


first = 1
second = 2
third = 0
count = 0


while third < 1000000:
    if second % 2 == 0:
        count = count + second
    third = first + second
    first = second
    second = third

print(count)
