# Author: Allen Anker
# Created by Allen Anker on 28/06/2018


"""
Design a data structure that supports the following two operations:
    void addWord(word)
    bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .. A . means it can represent any one letter.
"""
import collections


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.is_word = True  # end of the word

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res

    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return
        if word[0] == ".":  # matches any character
            for n in node.children.values():
                self.dfs(n, word[1:])  # search the rest of the characters
        else:
            node = node.children.get(word[0])
            if not node:  # if the character does not match the current node
                return
            self.dfs(node, word[1:])