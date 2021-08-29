# Assume you have a method called isSubstring. Using only 1 call to
# isSubstring, find out if s2 is a rotation of s1. water bottle = erbot tlewat s2 is rotation of s1


def substring_rotation(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    long_string = string_two + string_two
    if string_one in long_string:
        return True
    return False


print(substring_rotation("waterbottle", "erbottlewat"))
print(substring_rotation("ab", "abab"))
