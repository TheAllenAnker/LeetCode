# Author: Allen Anker
# Created by Allen Anker on 19/07/2018
class Solution:
    def roman_to_integer(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        res = 0
        while i < len(s):
            if s[i] == 'M':
                res += 1000
            elif s[i] == 'D':
                res += 500
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'V':
                res += 5
            elif s[i] == 'C':
                if i + 1 < len(s) and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    i += 1
                    res += 900 if s[i] == 'M' else 400
                else:
                    res += 100
            elif s[i] == 'X':
                if i + 1 < len(s) and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    i += 1
                    res += 90 if s[i] == 'C' else 40
                else:
                    res += 10
            elif s[i] == 'I':
                if i + 1 < len(s) and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    i += 1
                    res += 9 if s[i] == 'X' else 4
                else:
                    res += 1
            i += 1
        return res


solution = Solution()
s = 'IX'
print(solution.roman_to_integer(s))