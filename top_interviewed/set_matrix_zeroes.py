# Author: Allen Anker
# Created by Allen Anker on 21/08/2018
"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
"""


class Solution:
    def set_zeroes(self, matrix):
        """
        Set zeroes in matrix.
        :type matrix: List[List[int]]
        """
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            zero_rows = set([])
            zero_cols = set([])
            for i in range(rows):
                for j in range(cols):
                    if matrix[i][j] == 0:
                        zero_rows.add(i)
                        zero_cols.add(j)

            for i in zero_rows:
                for j in range(cols):
                    matrix[i][j] = 0
            for j in zero_cols:
                for i in range(rows):
                    matrix[i][j] = 0


solution = Solution()
matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
solution.set_zeroes(matrix)
