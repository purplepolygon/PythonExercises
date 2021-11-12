#!usr/bin/env python3
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?

def collatz_generator(ceiling):
    longest_chain = []
    magical_number = 0
    counter = 13
    while counter < ceiling:
        starting_number = counter
        collatz_list = [counter, ]
        while starting_number != 1:
            if starting_number % 2 == 1:
                starting_number = (starting_number * 3) + 1
                collatz_list.append(starting_number)
            else:
                starting_number = starting_number / 2
                collatz_list.append(starting_number)
        if len(collatz_list) > len(longest_chain):
            longest_chain = collatz_list
            magical_number = counter
        counter += 1
    return magical_number


if __name__ == '__main__':
    print(collatz_generator(1000000))
    # 837799
