# Author: Allen Anker
# Created by Allen Anker on 29/07/2018
"""
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.
"""


class Solution:
    def longest_valid_parentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # faster one
        '''
        dp = [0] * (len(s) + 1)
        longest_valid_length = 0

        for i, c in enumerate(s, 1):
            if c == ")":
                possible_opening_index = i - dp[i-1] - 2
                if possible_opening_index >= 0 and s[possible_opening_index] == "(":
                    dp[i] = dp[possible_opening_index] + (i - possible_opening_index)
                    longest_valid_length = dp[i] if longest_valid_length < dp[i] else longest_valid_length

        return longest_valid_length
        '''

        # use 1D DP
        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]
        dp = [0 for x in range(len(s))]
        max_to_now = 0
        for i in range(1, len(s)):
            if s[i] == ')':
                # case 1: ()()
                if s[i - 1] == '(':
                    # add nearest parentheses pairs + 2
                    dp[i] = dp[i - 2] + 2
                # case 2: (())
                # i-dp[i-1]-1 is the index of last "(" not paired until this ")"
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if dp[i - 1] > 0:  # content within current matching pair is valid
                        # add nearest parentheses pairs + 2 + parentheses before last "("
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        # otherwise is 0
                        dp[i] = 0
                max_to_now = max(max_to_now, dp[i])
        return max_to_now


solution = Solution()
s = '(()'
print(solution.longest_valid_parentheses(s))
