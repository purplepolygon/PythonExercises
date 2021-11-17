#!usr/bin/env python3
# Problem Set 4A
# Name: Purple Polygon


def get_permutations(sequence, i, j):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # if len(sequence) == 0:
    #     return [""]
    sequence = [x for x in sequence]
    list_of_permutations = []
    for i in range(i, len(sequence)):
        for j in range(i, len(sequence)):
            sequence[i], sequence[j] = sequence[j], sequence[i]
            list_of_permutations.append("".join(sequence))
            j += 1
        i += 1
        get_permutations(sequence, i, j)
    return list_of_permutations


if __name__ == '__main__':
    print('Input: \"abc\"')
    print('Expected Output:', ['abc', 'bac', 'cab', 'cab', 'cba', 'cba'])
    print('Actual Output:', get_permutations("abc", 0, 0))
    print('Input: \"yup\"')
    print('Expected Output:', ['yup', 'uyp', 'pyu', 'pyu', 'puy', 'puy'])
    print('Actual Output:', get_permutations("yup", 0, 0))
    print('Input: \"dog\"')
    print('Expected Output:', ['dog', 'odg', 'gdo', 'gdo', 'god', 'god'])
    print('Actual Output:', get_permutations("dog", 0, 0))
    get_permutations("abc", 0, 0)
