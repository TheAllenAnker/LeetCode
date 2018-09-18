# Author: Allen Anker
# Created by Allen Anker on 17/09/2018
"""
Implement a trie with insert, search, and starts_with methods.
"""


class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False

    def contains_key(self, c):
        return self.links[ord(c) - ord('a')] != None

    def get(self, key):
        return self.links[ord(key) - ord('a')]

    def put(self, k, node):
        self.links[ord(k) - ord('a')] = node

    def set_end(self):
        self.end = True

    def is_end(self):
        return self.end


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in range(len(word)):
            if not node.contains_key(word[i]):
                node.put(word[i], TrieNode())
            node = node.get(word[i])
        node.set_end()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for i in range(len(word)):
            if node.contains_key(word[i]):
                node = node.get(word[i])
            else:
                return False
        return True if node.is_end() else False

    def starts_with(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        # return self.search(prefix)
        node = self.root
        for i in range(len(prefix)):
            if node.contains_key(prefix[i]):
                node = node.get(prefix[i])
            else:
                return False
        return True


obj = Trie()
word = 'apple'
prefix = 'app'
obj.insert(prefix)
param_2 = obj.search('app')
param_3 = obj.starts_with(prefix)
param_4 = obj.starts_with('a')
print(param_2, param_3, param_4)
