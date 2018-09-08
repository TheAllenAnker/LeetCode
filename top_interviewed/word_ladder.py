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
import string


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
        queue = collections.deque([(begin_word, 1)])
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == end_word:
                return dist
            for i in range(len(word)):
                for j in ls:
                    if j != word[i]:
                        new_word = word[:i] + j + word[i + 1:]
                        if new_word not in visited and new_word in word_list:
                            queue.append((new_word, dist + 1))
                            visited.add(new_word)
        return 0


solution = Solution()
begin_word, end_word = 'hit', 'cog'
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution.ladder_length(begin_word, end_word, word_list))
