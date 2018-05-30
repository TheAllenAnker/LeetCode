# Author: Allen Anker
# Created by Allen Anker on 26/05/2018

'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1:
Input:

0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0
'''


class Solution:
    def updateMatrix(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        # first pass, from top to bottom, left to right
        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == 0:
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = rows + cols - 2
                    if i > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i-1][j] + 1)
                    if j > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j-1] + 1)
        # second pass: from bottom to top, right to left
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i < rows - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i+1][j] + 1)
                if j < cols - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j+1] + 1)

        return matrix




solution = Solution()
lists = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
solution.updateMatrix(lists)