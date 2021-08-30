#!/usr/bin/env python3


import random


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, "r")
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    is_true = True
    for x in secret_word:
        if x not in letters_guessed:
            is_true = False
    return is_true


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word = []
    for x in secret_word:
        if x not in letters_guessed:
            guessed_word.append("_ ")
        else:
            guessed_word.append(x)
    return "".join(guessed_word)


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    available_letters = [y for y in "abcdefghijklmnopqrstuvwxyz"]
    for x in letters_guessed:
        if x in available_letters:
            available_letters.remove(x)
    return "".join(available_letters)


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False

    while True:
        counter = 0
        is_true = True
        for x in my_word:
            if x != other_word[counter] and x != "_":
                is_true = False
                return is_true
            else:
                counter += 1
        return is_true


def possible_check(my_word, test_word):
    """
        my_word: string with _ characters, current guess of secret word
        returns: Boolean
        Makes sure that test_word does not contain additional characters from
        my_word. Ex: t____d, t_st_d returns False since t has already been guessed
    """
    is_true = True
    my_word = my_word.replace(" ", "")
    for x in my_word:
        if x == "_":
            continue
        elif my_word.count(x, 0, len(my_word)) != test_word.count(x, 0, len(test_word)):
            is_true = False
            break
    return is_true


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    possible_words = []
    for test_word in wordlist:
        if match_with_gaps(my_word, test_word):
            if possible_check(my_word, test_word):
                print(test_word)
                possible_words.append(test_word)


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    guesses = 6
    warnings = 3
    letters_guessed = []
    secret_word_unique_chars = len(set(secret_word))
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that has: " + str(len(secret_word)) + " letters")
    while guesses > 0:
        print("----------------")
        print("You have " + str(warnings) + " warnings left")
        print("You have " + str(guesses) + " guesses left")
        print("Available letters: " + get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        if guess == "*":
            print(get_guessed_word(secret_word, letters_guessed))
            my_word = get_guessed_word(secret_word, letters_guessed)
            show_possible_matches(my_word)
            continue
        if not guess.isalpha():
            warnings -= 1
            if warnings == 0:
                guesses -= 1
            print(
                "Oops! That is not a valid character. \
                 You have "
                + str(warnings)
                + " left: "
                + get_guessed_word(secret_word, letters_guessed)
            )
            continue
        elif guess not in get_available_letters(letters_guessed):
            warnings -= 1
            if warnings == 0:
                guesses -= 1
            print(
                "Oops! You already guessed that character. You have\
                 "
                + str(warnings)
                + " left: "
                + get_guessed_word(secret_word, letters_guessed)
            )
            continue

        letters_guessed.append(guess)

        if is_word_guessed(secret_word, letters_guessed):
            print("Congratulations, you won!")
            print(
                "Your total score for this game is: "
                + str(guesses * secret_word_unique_chars)
            )
            exit()
        elif guess in secret_word:
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            continue
        elif guess not in secret_word:
            if guess in "aeiou":
                guesses -= 1
            guesses -= 1
            print(
                "Oops! That letter is not in my word: "
                + get_guessed_word(secret_word, letters_guessed)
            )
            if guesses == 0:
                print("Sorry, you ran out of guesses. The word was: " + secret_word)
                exit()
            continue


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
