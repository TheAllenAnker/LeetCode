# Author: Allen Anker
# Created by Allen Anker on 01/10/2018
"""
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
"""


class Solution:
    dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def longest_increasing_path(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        cached = [[0] * len(matrix[0])] * len(matrix)
        rows, cols = len(matrix), len(matrix[0])
        max_l = 1
        for i in range(rows):
            for j in range(cols):
                length = self.dfs(matrix, i, j, rows, cols, cached)
                max_l = max(max_l, length)

        return max_l

    def dfs(self, matrix, x, y, rows, cols, cached):
        if cached[x][y] != 0:
            return cached[x][y]
        max_l = 1
        for dir in self.dirs:
            i, j = dir[0] + x, dir[1] + y
            if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] <= matrix[x][y]:
                continue
            length = self.dfs(matrix, i, j, rows, cols, cached) + 1
            max_l = max(max_l, length)

        cached[x][y] = max_l

        return max_l


solution = Solution()
print(
    solution.longest_increasing_path([
        [9, 9, 4], [6, 6, 8], [2, 1, 1]
    ]))
