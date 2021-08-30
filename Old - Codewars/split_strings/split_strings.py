#!/usr/bin/env python3
# For a given string, split into a list of two characters. If there are an odd number of characters, append _:
# Ex: Given "bandanas" return ["ba", "nd", "an", "as"], given "Hello" return ["He", "ll", "o_"]


def split_strings(given_string):
    given_string = [char for char in given_string]
    new_list = []
    pointer_one = 0
    pointer_two = 1
    if len(given_string) % 2 == 0:
        while pointer_two < len(given_string):
            new_list.append(given_string[pointer_one] + given_string[pointer_two])
            pointer_one += 2
            pointer_two += 2
    elif len(given_string) % 2 == 1:
        while pointer_two < len(given_string) - 1:
            new_list.append(given_string[pointer_one] + given_string[pointer_two])
            pointer_one += 2
            pointer_two += 2
        new_list.append(given_string[len(given_string) - 1] + "_")
    print(new_list)
    return new_list


if __name__ == "__main__":
    split_strings("Banana")  # ['Ba', 'na', 'na']
    split_strings("Banananananas")  # ['Ba', 'na', 'na', 'na', 'na', 'na', 's_']
    split_strings("aB")  # ['aB']
    split_strings("a")  # ['a_']
    split_strings(" ")  # [' _']
