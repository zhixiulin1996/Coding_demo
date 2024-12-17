"""
File: boggle_trie.py
Name: Zhi-Xiu Lin
----------------------------------------
There are 3 parts in my code:
1. User input and judge legal or not
2. Read dictionary (implement of trie)
3. DFS search
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


class TrieNode:
    def __init__(self):
        self.children = {}  # store up to 26 alphabets as key and new TrieNode as value
        self.is_end = False  # record the information of word end

    def insert(self, word):
        # To insert a new word into the trie structure
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]  # to next node
        # cur will stop at the end of word in final state
        cur.is_end = True


def main():
    # Part 1. User Input
    boggle = [[] for i in range(4)]
    is_illegal = False  # to check the input and if illegal, will not start searching
    for i in range(4):  # row index
        lst = input(f"{i + 1} row of letters: ").split(' ')
        for j in range(4):  # column index
            if len(lst[j]) == 1 and lst[j].isalpha():
                boggle[i].append(lst[j].lower())
            else:
                print("Illegal input")
                is_illegal = True
                break
        if is_illegal:  # if illegal, will not have any chance to key in next row
            break

    # Part 2.Read dictionary
    root = TrieNode()
    with open(FILE, 'r') as f:
        for word in f:
            if 4 <= len(word.strip()) <= 16:
                root.insert(word.strip())

    # Part3. DFS search
    ans_set, path = set(), set()  # to record the answer and the path to avoid repeatedly run the same point

    # Define search function
    def search(cur_s, node, r, c):
        """
        I solve the problem by recursion + backtracking
        This function will check the point is make sense or not
        If yes, then recursively check the 8 corners
        If no, return

        :param cur_s: string, current string
        :param node: TrieNode, current node
        :param r: int, row index
        :param c: int, column index
        :return: none
        """
        # Base case: 1.Out of range 2.TrieNode children check 3.repeat point
        if r < 0 or c < 0 or r == 4 or c == 4 or boggle[r][c] not in node.children or (r, c) in path:
            return
        # choose
        path.add((r, c))
        cur_s += boggle[r][c]
        node = node.children[boggle[r][c]]
        if node.is_end:
            print(f"Found: \"{cur_s}\"")
            ans_set.add(cur_s)
        # explore next points
        search(cur_s, node, r - 1, c + 1)  # upper left
        search(cur_s, node, r - 1, c)  # upper middle
        search(cur_s, node, r - 1, c - 1)  # upper right
        search(cur_s, node, r, c + 1)  # right
        search(cur_s, node, r, c - 1)  # left
        search(cur_s, node, r + 1, c + 1)  # lower right
        search(cur_s, node, r + 1, c)  # lower middle
        search(cur_s, node, r + 1, c - 1)  # lower left
        # un-choose
        path.remove((r, c))

    start = time.time()
    ####################
    if not is_illegal:
        for i in range(4):
            for j in range(4):
                search('', root, i, j)  # search for each start point on the boggle
    ####################
    end = time.time()
    print(f"There are {len(ans_set)} words in total.")
    print('----------------------------------')
    print(f'The speed of your boggle algorithm with trie implement: {end - start} seconds.')


if __name__ == '__main__':
    main()
