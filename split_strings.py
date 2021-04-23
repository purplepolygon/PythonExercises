# For a given string, split into a list of two characters. If there are an odd number of characters, append _:
# Ex: Given "bandanas return ["ba", "nd", "an", "as"], given "Hello" return ["He", "ll", "o_"] 


def solution(s):
    s = [x for x in s]
    new_list = []
    m = 0
    n = 1
    if len(s) % 2 == 0:
        while n < len(s):
            new_list.append(s[m] + s[n])
            m += 2
            n += 2
    elif len(s) % 2 == 1:
        while n < len(s) - 1:
            new_list.append(s[m] + s[n])
            m += 2
            n += 2
        new_list.append(s[len(s) - 1] + "_")
    return(new_list)
