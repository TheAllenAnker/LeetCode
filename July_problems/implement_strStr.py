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
        # solution one, using regular expression
        '''
        if not needle:
            return 0
        return re.search(needle, haystack).start() if re.search(needle, haystack) else -1
        '''
        # solution two
        if not (needle or haystack):
            return 0
        if needle not in haystack:
            return -1
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i+n] == needle:
                return i


solution = Solution()
haystack = 'hello'
needle = 'll'
print(solution.strStr(haystack, needle))