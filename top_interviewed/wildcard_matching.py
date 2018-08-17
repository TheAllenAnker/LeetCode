# Author: Allen Anker
# Created by Allen Anker on 17/08/2018
"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
"""


class Solution:
    def is_match(self, s, p):
        """
        A pattern matching method that implements wildcard matching.
        :param s: Input string
        :type s: str
        :param p: Input pattern
        :type p: str
        :return: True if matched, or false
        :rtype bool
        """
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        # until previous one matched or not
        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                # keep returning false until the current i is met
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                # '*' can match all the remaining characters
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
