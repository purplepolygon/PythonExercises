#!usr/bin/python3


# Given two strings, check if one is a permutation of the other.


def permutation_check(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    string_one_list = [char for char in string_one]
    string_two_list = [char for char in string_two]
    j = 0
    i = 0
    for i in range(len(string_one_list)):
        if len(string_two_list) == 0:
            return True
        for j in range(len(string_two_list)):
            if string_one_list[i] == string_two_list[j]:
                del string_two_list[j]
                if len(string_two_list) == 1:
                    break
                if len(string_two_list) == 0:
                    return True
                i += 1
                break
            elif len(string_two_list) == 1:
                break
            else:
                j += 1
                continue
    return False


print(permutation_check("bbaw", "wabb"))
