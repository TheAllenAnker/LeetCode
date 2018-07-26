# Author: Allen Anker
# Created by Allen Anker on 25/07/2018
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""
import re


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        return re.search(needle, haystack).start() if re.search(needle, haystack) else -1


solution = Solution()
haystack = 'helllo'
needle = 'o'
print(solution.strStr(haystack, needle))
