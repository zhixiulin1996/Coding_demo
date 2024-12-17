"""
File: anagram.py
Name: Zhi-Xiu Lin
----------------------------------
This program finds all permutation and combination first,
then check in the dictionary.
The word is input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time  # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'  # This is the filename of an English dictionary
EXIT = '-1'  # Controls when to stop the loop


def main():
    print(f"Welcome to stanCode \"Anagram Generator\" (or {EXIT} to quit)")
    while True:
        s = str(input("Find anagrams for: "))
        if s == EXIT:
            break
        n_dict = read_dictionary(s)
        start = time.time()
        ####################
        print("Searching...")  # to avoid obob
        lst = find_anagrams(s, len(s), '', n_dict, [])
        ####################
        end = time.time()
        print(f"{len(lst)} anagrams: {lst}")
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary(s):
    """
    Use a dict with structure of {'a': {}, 'b': {} ....} to store data
    Will only store words with the same length of input int
    Also, will store only the alphabet show in the word

    :param s: string, need-to-check word
    :return: python dict
    """
    # alpha_set used to record type of alphabet in the input s
    alpha_set = set()
    for char in s:
        alpha_set.add(char)
    # Read file
    with open(FILE, 'r') as f:
        new_dict = {}
        for line in f:
            if line[0] in alpha_set and len(line.strip()) == len(s):
                if line[0] not in new_dict:  # to avoid key error
                    new_dict[line[0]] = set()  # initialize a python set to each alphabet
                new_dict[line[0]].add(line.strip())
    return new_dict


def find_anagrams(s, len_s, curr_s, n_dict, ans_lst):
    """
    :param s: input string for permutation and combination
    :param len_s: int, length of input string
    :param curr_s: str, current string
    :param n_dict: python dict, the filtered content in the file
    :return ans_lst: list, used to store anagrams
    """
    if len(curr_s) == len_s:
        if curr_s in n_dict[curr_s[0]]:
            print(f"Found: {curr_s}")
            print("Searching...")
            ans_lst.append(curr_s)
            n_dict[curr_s[0]].remove(curr_s)
    for i in range(len(s)):
        # choose
        curr_s += s[i]
        # explore
        find_anagrams(s[:i] + s[i + 1:], len_s, curr_s, n_dict, ans_lst)
        # un-choose
        curr_s = curr_s[:-1]
    return ans_lst


if __name__ == '__main__':
    main()
