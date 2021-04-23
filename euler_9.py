# Pythagorean Triplet:
# a^2 + b^2 = c^2, find a*b*c if a<b<c and a + b + c = 1000
# 21^2 + 28^2 = 35^2
import math


def triplet_finder():
    for x in range(1, 999):
        for y in range(1, 999):
            test = x**2 + y**2
            if math.sqrt(test) + x + y == 1000:
                return x * y * math.sqrt(test)


print(triplet_finder())
