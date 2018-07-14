# Author: Allen Anker
# Created by Allen Anker on 13/07/2018


"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
"""


class Solution:
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # by selecting the center of the palindromic, we can find all the palindromic
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand_around_center(s, i, i)
            len2 = self.expand_around_center(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - int((max_len - 1) / 2)
                end = i + int(max_len / 2)

        return s[start:end+1]

    @staticmethod
    def expand_around_center(s, left, right):
        l, r = left, right
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return r - l - 1


solution = Solution()
s = 'cbbd'
print(solution.longest_palindrome(s))