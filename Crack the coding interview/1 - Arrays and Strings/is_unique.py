#!usr/bin/python3


# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?


def is_unique(unique_string):
    """O(n) where n = len of string solution"""
    string_list = [x.lower() for x in unique_string]
    string_dict = {}
    for x in string_list:
        if x in string_dict:
            return False
        else:
            string_dict[x] = "1"
            continue
    return True


def is_unique_one_space(unique_string):
    """O(n^2) time, O(1) space"""
    for i in range(0, len(unique_string) - 1):
        for j in range(i + 1, len(unique_string)):
            print(i)
            print(j)
            print(unique_string[i])
            print(unique_string[j])
            if unique_string[i].lower() == unique_string[j].lower():
                print("same")
                return False


print(is_unique_one_space("paCCnmolm"))
