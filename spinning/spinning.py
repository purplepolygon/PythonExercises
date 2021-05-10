#!/usr/bin/env python3
# Reverse all words with length of 6 or more in a sentence.


sentence_input = input("Please type a sentence: ")
new_strings = []


def spin_words(sentence):
    for i in sentence.split():
        if len(i) >= 6:
            new_string = i.replace(i, i[::-1])
            new_strings.append(new_string)
        elif len(i) < 6:
            new_string = i
            new_strings.append(new_string)


spin_words(sentence_input)
print(" ".join(new_strings))
