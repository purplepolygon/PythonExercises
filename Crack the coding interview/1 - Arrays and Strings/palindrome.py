#!usr/bin/python3


# Palindrome check, round 2, assumes no whitespace and only mixed case alphabet.


from collections import Counter


def palindrome_check(test_string):
    palindrome_dict = Counter([x.lower() for x in test_string])
    print(sum([x % 2 for x in palindrome_dict.values()]))
    print(len([palindrome_dict.values()]))
    if (
        sum([x % 2 for x in palindrome_dict.values()]) == 0
        and len(test_string) % 2 == 0
    ):
        return True
    elif (
        sum([x % 2 for x in palindrome_dict.values()]) == 1
        and len(test_string) % 2 == 1
    ):
        return True
    else:
        return False


print(palindrome_check("RaceFastSafeCar"))
