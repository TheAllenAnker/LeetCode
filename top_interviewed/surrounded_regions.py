# Author: Allen Anker
# Created by Allen Anker on 09/09/2018
"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        # border_o saves all the pairs connected with a border 'O'
        border_o = [ij for k in range(m + n) for ij in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
        for i, j in border_o:
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                # add all elements from its four directions
                # add it all first, we will decide whether it should be changed to 'S' in the next loop
                border_o += (i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)
        # change all 'S's to 'O'
        board[:] = [['XO'[c == 'S'] for c in row] for row in board]


solution = Solution()
board = []
print(solution.solve(board))
