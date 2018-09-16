# Author: Allen Anker
# Created by Allen Anker on 15/09/2018
"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def num_islands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def flip(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                # flip all '1's adjacent to this one
                list(map(flip, [i - 1, i + 1, i, i], [j, j, j + 1, j - 1]))
                return 1
            return 0

        return sum(flip(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
