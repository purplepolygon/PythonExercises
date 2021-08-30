# Check two strings and determine if they are 1 edit away via replacement, insertion, or deletion
# pale -> ple = True, pale -> male = True, jug -> jugs = True
# NOT DONE

from collections import Counter


def one_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False

    if len(string1) - len(string2) == 1:  # Insertion case
        ins_check = 0
        m = 0
        n = 0
        while ins_check < 2:
            if n == len(string2):
                return True
            if string1[m] != string2[n]:
                ins_check += 1
                m += 2
                n += 1
                continue
            else:
                m += 1
                n += 1
                continue
        return False

    if len(string1) - len(string2) == -1:  # Deletion case
        ins_check = 0
        m = 0
        n = 0
        while ins_check < 2:
            print("nexx")
            print(len(string1))
            if n == len(string1) and m <= len(string1) + 1:
                print(n)
                print("what")
                return True
            if string2[m] != string1[n]:
                print("shu")
                ins_check += 1
                m += 2
                n += 1
                continue
            else:
                print("Shi")
                print(m)
                print(n)
                m += 1
                n += 1
                continue
        return False

    """Replacement of character check"""
    if len(string1) == len(string2):
        replace_check = 0
        for i in range(0, len(string1)):
            if string1[i] != string2[i]:
                replace_check += 1
                if replace_check == 2:
                    return False
            else:
                continue
        return True


# print(one_away("china", "chin"))
# print(one_away("chimmn", "chimmna"))
# print(one_away("china", "chona"))
# print(one_away("lllmmm", "lllmm"))
# print(one_away("llmmmm", "llmmmm"))
# print(one_away("lzpp", "lzdd"))
print(one_away("fruit", "fruity"))
