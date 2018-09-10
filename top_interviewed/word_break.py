# Author: Allen Anker
# Created by Allen Anker on 10/09/2018
"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
"""


class Solution:
    def word_break(self, s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: bool
        """
        # So, I wrote a TLE solution again.
        '''
        if not s:
            return True
        for i in range(1, len(s) + 1):
            if s[:i] in word_dict:
                if self.word_break(s[i:], word_dict):
                    return True
        return False
        '''
        ok = [True]
        for i in range(1, len(s) + 1):
            # ok[j] Use previous information get from previous loops
            # Check once, save the information whether the s[:i] satisfies the condition
            ok += any(ok[j] and s[j:i] in word_dict for j in range(i)),
        return ok[-1]


solution = Solution()
s = 'leetcode'
word_dict = ['aaa', 'aaaa', 'leet', 'code']
print(solution.word_break(s, word_dict))
