# Author: Allen Anker
# Created by Allen Anker on 20/08/2018
"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


class Solution:
    def rotate(self, matrix):
        """
        First reverse up to down, then swap the symmetry ones
        :type matrix: List[List[int]]
        """
        for i in range(len(matrix)//2):
            j = len(matrix) - i - 1
            row = matrix[i]
            matrix[i] = matrix[j]
            matrix[j] = row
        for i in range(len(matrix)):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        pass


solution = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solution.rotate(matrix)