# Author: Allen Anker
# Created by Allen Anker on 10/09/2018
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""


class Solution:
    def word_break(self, s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: List[str]
        """
        # A solution written by a famous one on Leetcode.
        memo = {len(s): ['']}

        # sentences(i) returns a list of all sentences that can be built from the suffix s[i:].
        def sentences(i):
            if i not in memo:
                # (tail and ' ' + tail) return ' ' + tail if tail is not empty, or it return empty ''
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i + 1, len(s) + 1)
                           if s[i:j] in word_dict
                           for tail in sentences(j)]
            return memo[i]
            # if i not in memo:
            #     curr = []
            #     for j in range(i + 1, len(s) + 1):
            #         if s[i:j] in word_dict:
            #             curr.append(s[i:j])
            #             for se in sentences(j):
            #                 if se:
            #                     curr.append(' ' + se)
            #     memo[i] = curr
            # return memo[i]
        return sentences(0)


solution = Solution()
s = "pineapplepenapple"
word_dict = ["apple", "pen", "applepen", "pine", "pineapple"]
print(solution.word_break(s, word_dict))
print('Expected: ' + '["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]')
