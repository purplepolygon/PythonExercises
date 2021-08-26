#!usr/bin/python3


# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def is_unique(unique_string):
    string_list = [x.lower() for x in unique_string]
    string_dict = {}
    for x in string_list:
        if x in string_dict:
            return False
        else:
            string_dict[x] = "1"
            continue
    return True


print(is_unique("comp3wtn"))
