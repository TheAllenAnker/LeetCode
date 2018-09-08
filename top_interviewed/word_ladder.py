# Author: Allen Anker
# Created by Allen Anker on 07/09/2018
"""
Given two words (beginWord and endWord), and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
import collections
from collections import defaultdict


class Solution:
    def ladder_length(self, begin_word, end_word, word_list):
        """
        :type begin_word: str
        :type end_word: str
        :type word_list: List[str]
        :rtype: int
        """

        # The point is to find if there is a possible sequence in the list.
        # If there is a possible sequence starting from an index, the result if always the same?
        def construct_dict(word_list):
            d = defaultdict()
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = collections.deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        # change one character
                        s = word[:i] + "_" + word[i + 1:]
                        # get all possible ways of change
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                # iterate through each possible way
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(word_list or set([begin_word, end_word]))
        return bfs_words(begin_word, end_word, d)


solution = Solution()
begin_word, end_word = 'hit', 'cog'
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution.ladder_length(begin_word, end_word, word_list))
