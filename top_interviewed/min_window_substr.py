# Author: Allen Anker
# Created by Allen Anker on 23/08/2018
"""
Given a string S and a string T, find the minimum window in S
which will contain all the characters in T in complexity O(n).

Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
from collections import Counter


class Solution:
    def min_window(self, s, t):
        """
        Find minimum window substring.
        :type s: str
        :type t: str
        :rtype: str
        """
        need, missing = Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                # remove as much as possible from the window start
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]


solution = Solution()
s = ''
t = ''
print(solution.min_window(s, t))
