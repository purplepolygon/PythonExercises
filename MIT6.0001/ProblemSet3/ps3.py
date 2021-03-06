#!/usr/bin/env python3
# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>


import math
import random

VOWELS = "aeiou*"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10,
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """

    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------


#
# Problem #1: Scoring a word
#


def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters,
    or the empty string "". You may not assume that the string will only contain
    lowercase letters, so you will have to handle uppercase and mixed case strings
    appropriately.

    The score for a word is the product of two components:

    The first component is the sum of the points for letters in the word.
    The second component is the larger of:
            1, or
            7*word_len - 3*(n-word_len), where word_len is the length of the word
            and n is the hand length when the word was played

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    first_component = 0
    word_array = [x for x in word]
    i = 0
    second_component = ((7 * len(word_array)) - (3 * (n - len(word_array))))
    if "*" in word_array:
        word_array.remove("*")
    while i < len(word_array):
        for letter in word_array:
            first_component += SCRABBLE_LETTER_VALUES[word_array[i]]
            i += 1
            continue
    if second_component > 1:
        return first_component * second_component
    else:
        return first_component


#
# Make sure you understand how this function works and what it does!
#


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")  # print all on the same line
    print()  # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """

    hand = {"*": 1, }
    num_vowels = int(math.ceil(n / 3)) - 1

    for i in range(num_vowels):
        x = random.choice(VOWELS)
        while x == "*":
            x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured).

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    word = word.lower()
    word_letters = [x for x in word]
    updated_hand = hand.copy()
    i = 0
    while i < len(word_letters):
        for word in word_letters:
            if word_letters[i] in updated_hand:
                updated_hand[word_letters[i]] = updated_hand[word_letters[i]] - 1
            i += 1
    return updated_hand


#
# Problem #3: Test word validity
#


def is_valid_word(word, hand, wordlist):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    word_letters = [x for x in word]
    print(word_letters)
    updated_hand = hand.copy()
    if "*" in word_letters:
        for j in VOWELS:
            new_word_list = [j if i == "*" else i for i in word_letters]
            new_word = "".join(new_word_list)
            if new_word in wordlist:
                k = 0
                while k < len(word_letters):
                    if word_letters[k] in updated_hand and updated_hand[word_letters[k]] != 0:
                        updated_hand[word_letters[k]] = updated_hand[word_letters[k]] - 1
                        k += 1
                    else:
                        return False
                return True
        else:
            return False
    if word in wordlist:
        i = 0
        while i < len(word_letters):
            if word_letters[i] in updated_hand and updated_hand[word_letters[i]] != 0:
                updated_hand[word_letters[i]] = updated_hand[word_letters[i]] - 1
                i += 1
                continue
            else:
                return False
        return True
    else:
        return False


# print(is_valid_word("*t", {'*': 1, 't': 1}, load_words()))

#
# Problem #5: Playing a hand
#


def calculate_handlen(hand):
    """
    Returns the length (number of letters) in the current hand.

    hand: dictionary (string-> int)
    returns: integer
    """
    for letters in hand.copy():
        if hand[letters] == 0:
            hand.pop(letters)
    n = len(hand)
    return n


def play_hand(hand, wordlist):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputting two
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand

    """
    # Keep track of the total score
    score = 0
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        if calculate_handlen(hand) != 0:
            # Display the hand
            print(hand)
        else:
            # Game is over (user entered '!!' or ran out of letters),
            # so tell user the total score
            print("You ran out of letters or entered \"!!\"")
            print("Total score: " + str(score))
        # Ask user for input
        potential_word = input("Enter word, or \"!!\" to indicate that you are finished: ")
        # If the input is two exclamation points:
        if potential_word == "!!":
            # End the game (break out of the loop)
            break
            # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            i = 0
            if is_valid_word(potential_word, hand, wordlist):
                word_score = get_word_score(potential_word, calculate_handlen(hand))
                score += word_score
                # Tell the user how many points the word earned,
                # and the updated total score
                print("You earned " + str(word_score) + " points!")
                print("Current score: " + str(score))
                while i < len(potential_word):
                    if potential_word[i] in hand and hand[potential_word[i]] != 0:
                        hand[potential_word[i]] = hand[potential_word[i]] - 1
                        i += 1
                        continue
            else:
                # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                print("Word is not valid. Please choose another")
                # Update the user's hand by removing the letters of their inputted word
                while i < len(potential_word):
                    if potential_word[i] in hand and hand[potential_word[i]] != 0:
                        hand[potential_word[i]] = hand[potential_word[i]] - 1
                        i += 1
                        continue
    return score


# play_hand({"a": 1, "c": 1, "f": 1, "i": 1, "*": 1, "t": 1, "x": 1}, load_words())

#
# Problem #6: Playing a game
#


#
# Procedure you will use to substitute a letter in a hand
#


def substitute_hand(hand, letter):
    """
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.

    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    sub_letter = letter
    new_letter = random.choice(VOWELS + CONSONANTS)
    substituted_hand = hand.copy()
    while new_letter == sub_letter or new_letter in hand:
        new_letter = random.choice(VOWELS + CONSONANTS)
    if sub_letter in substituted_hand:
        substituted_hand[new_letter] = substituted_hand.pop(sub_letter)
    return substituted_hand


def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the
      entire series

    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitute option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep
      the better of the two scores for that hand.  This can only be done once
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.

    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    number_of_hands = int(input("Enter number of hands: "))
    hands_played = 0
    total_score = 0
    sub_played = False
    replay_played = False
    while hands_played < number_of_hands:
        hand = deal_hand(HAND_SIZE)
        orig_hand = hand.copy()
        print("Current hand: " + str(hand))
        if not sub_played:
            sub_letter_answer = input("Would you like to substituted a letter? yes or no: ")
            if sub_letter_answer == "yes":
                sub_letter = input("Which letter would you like to replace?")
                hand = substitute_hand(hand, sub_letter)
                sub_played = True
        score = play_hand(hand, word_list)
        print("Total score for this hand: " + str(score))
        if not replay_played:
            replay = input("Would you like to replay this hand? yes or no: ")
            if replay == "yes":
                score = play_hand(orig_hand, word_list)
                replay_played = True
        total_score += score
        print("Total score: " + str(total_score))
        hands_played += 1
    return total_score


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement


if __name__ == "__main__":
    word_list = load_words()
    play_game(word_list)
