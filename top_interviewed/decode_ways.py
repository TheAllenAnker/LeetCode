# Author: Allen Anker
# Created by Allen Anker on 28/08/2018
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.
"""


class Solution:
    def num_decodings(self, s):
        """
        Decoding number of ways possible.
        :param s: str
        :rtype: int
        """
        # w tells the number of ways, which equals to the previous number of ways
        #   times the number of sequences formed by remaining numbers
        # v tells the previous number of ways (before meeting p)
        # d is the current digit
        # p is the previous digit
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w


solution = Solution()
s = '226'
print(solution.num_decodings(s))
