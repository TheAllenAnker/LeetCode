# Author: Allen Anker
# Created by Allen Anker on 09/09/2018
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # This solution was written by someone else, it's a really elegant and brilliant solution.
        return [[s[:i]] + rest
                for i in range(1, len(s) + 1)
                # check if substring s[:i] is a palindrome
                if s[:i] == s[i - 1::-1]
                for rest in self.partition(s[i:])] or [[]]


solution = Solution()
s = 'aaba'
print(solution.partition(s))
