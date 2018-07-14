# Author: Allen Anker
# Created by Allen Anker on 15/07/2018


"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
"""


class Solution:
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s or num_rows == 1: return s
        rows = [''] * num_rows
        for i in range(len(s)):
            j = i % (2 * num_rows - 2)
            if j < num_rows:
                rows[j] += s[i]
            else:
                # num_rows - 1 - (j - num_rows) = 2 * num_rows - 1 - j
                rows[2 * num_rows - 2 - j] += s[i]

        return self.__compact_str_list(rows)

    @staticmethod
    def __compact_str_list(s):
        result = ''
        for item in s:
            result += item

        return result


solution = Solution()
s = 'PAYPALISHIRING'
print(solution.convert(s, 3))