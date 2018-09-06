# Author: Allen Anker
# Created by Allen Anker on 06/09/2018
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
"""


class Solution:
    def generate(self, numRows):
        """
        Each row's first and last element is 1.
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if numRows == 0:
            return []
        i = 1
        while i <= numRows:
            curr_row = [1, ]
            need_to_fill = i - 2
            if need_to_fill > 0:
                start, end = 1, need_to_fill
                for j in range(start, end + 1):
                    curr_row += [res[-1][j - 1] + res[-1][j]]
            if i > 1:
                curr_row += [1]
            res.append(curr_row)
            i += 1
        return res


solution = Solution()
print(solution.generate(5))
