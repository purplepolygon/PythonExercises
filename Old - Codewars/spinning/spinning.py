#!/usr/bin/env python3
# Reverse all words with length of 6 or more in a sentence.


def spin_words():
    new_strings = []
    sentence = input("Please type a sentence: ")
    for i in sentence.split():
        if len(i) >= 6:
            new_string = i.replace(i, i[::-1])
            new_strings.append(new_string)
        elif len(i) < 6:
            new_string = i
            new_strings.append(new_string)
    spun_sentence = " ".join(new_strings)
    print(spun_sentence)
    return spun_sentence


if __name__ == "__main__":
    spin_words()
