#!usr/bin/python3


# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures? O(n^2) Brute Force Solution


def is_unique(unique_string):
    string_list = [x for x in unique_string]
    i = 0
    j = 0
    while j <= len(string_list):
        for i in range(len(string_list) - 1):
            j = i + 1
            print(len(string_list))
            print(str(i) + "step2")
            print(str(j) + "step1")
            for j in range(1, len(string_list)):
                print("check")
                print(i)
                print(j)
                if string_list[i] == string_list[j]:
                    print(string_list[i], string_list[j])
                    print(i, j)
                    return False
                else:
                    j += 1
                    continue
                i += 1
        return True


print(is_unique("comptn"))

# (Get rid of J loop, just use while loop + for loop to solve this )
