# Find the largest palindrome made from 2x 3-digit numbers
# 91 x 99 = 9009

def palindrome_check(number):
    if str(number)[::1] == str(number)[::-1]:
        return True


def palindrome(number):
    largest_palindrome = [0]
    for x in range(number, number - 100, -1):
        for y in range(number, number - 100, -1):
            curr_num = x * y
            if palindrome_check(curr_num):
                if curr_num > largest_palindrome[0]:
                    largest_palindrome = [curr_num]
    return largest_palindrome[0]


print(palindrome(999))
