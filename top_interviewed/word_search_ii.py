# Author: Allen Anker
# Created by Allen Anker on 18/09/2018
"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
"""


class TrieNode:
    def __init__(self):
        self.next = [None] * 26
        self.word = None


class Solution:
    def find_words(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        root = self.build_trie(words)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, root, res)
        return res

    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            p = root
            for i in range(len(word)):
                index = ord(word[i]) - ord('a')
                if not p.next[index]:
                    p.next[index] = TrieNode()
                p = p.next[index]
            p.word = word
        return root

    def dfs(self, board, i, j, root, res):
        c = board[i][j]
        if c == '#' or not root.next[ord(c) - ord('a')]:
            return
        root = root.next[ord(c) - ord('a')]
        if root.word:
            res.append(root.word)
            # remove duplicates
            root.word = None

        board[i][j] = '#'
        if i > 0: self.dfs(board, i - 1, j, root, res)
        if j < len(board[0]) - 1: self.dfs(board, i, j + 1, root, res)
        if i < len(board) - 1: self.dfs(board, i + 1, j, root, res)
        if j > 0: self.dfs(board, i, j - 1, root, res)
        board[i][j] = c


solution = Solution()
# words = ["oath", "pea", "eat", "rain"]
# board = [
#     ['o', 'a', 'a', 'n'],
#     ['e', 't', 'a', 'e'],
#     ['i', 'h', 'k', 'r'],
#     ['i', 'f', 'l', 'v']
# ]
board2 = [['a', 'a']]
words2 = ['a']

board3 = [["a","b"],["c","d"]]
words3 = ["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
print(solution.find_words(board3, words3))
# b = [1, 2, 3]
# a = b[:]
# a[0] = 0
# print(a, b)
