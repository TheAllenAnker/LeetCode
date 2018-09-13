# Author: Allen Anker
# Created by Allen Anker on 13/09/2018
"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""


class Solution:
    def title_to_number(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solving this problem is like counting how many combinations you can get before getting the final s
        if not s:
            return
        res, l = 0, len(s)
        for i in range(l - 1):
            res += 26**(l - i - 1) * (ord(s[i]) - 64)
        res += ord(s[-1]) - 64
        return res


solution = Solution()
s = 'AAA'
print(solution.title_to_number(s))
