# Author: Allen Anker
# Created by Allen Anker on 07/09/2018
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
import re


class Solution:
    def is_palindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub('[^a-zA-Z0-9]+', '', s)
        s = s.upper()
        return s[::-1] == s


solution = Solution()
s = '32Aalaa ;?23'
print(solution.is_palindrome(s))
