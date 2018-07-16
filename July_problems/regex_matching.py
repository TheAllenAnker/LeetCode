# Author: Allen Anker
# Created by Allen Anker on 15/07/2018


"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""


class Solution:
    def is_match(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # si, pi = 0, 0
        # for i in range(len(s) - 1):
        #     if s[i] == '.':
        #         if s[i + 1] == '.' or s[i + 1].isalpha():
        #             i += 1
        #         else:
        #             return True
        #     elif s[i] == '*':
        #         pass
        #     else:
        #         if s[i + 1].isalpha() or s[i + 1] == '.':
        #             i += 1
        #         else:
        #             self.is_match(s[i+1:], )
        #
        # return True

        if not p:
            return not s

        first_match = bool(s) and p[0] in {s[0], '.'}
        # '#" can only appear after index 1
        if len(p) >= 2 and p[1] == '*':
            # match 0 character before '*' or match one character at a time and keep matching by recursion
            return (self.is_match(s, p[2:]) or
                    first_match and self.is_match(s[1:], p))
        # if no '*', then continue
        else:
            return first_match and self.is_match(s[1:], p[1:])


solution = Solution()
s = 'aab'
p = 'c*a*b'
print(solution.is_match(s, p))