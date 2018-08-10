# Author: Allen Anker
# Created by Allen Anker on 09/08/2018
"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.
"""


class Solution:
    def solve_sudoku(self, board):
        """
        Fill the board in-place to solve the sudoku.
        :type board: List[List[int]]
        :rtype: void
        """

        def dfs(board, stack1, stack2):
            if not stack1:
                return
            x, y = stack1.pop()
            stack2.append((x, y))
            box = [board[x // 3 * 3 + i][y // 3 * 3 + j] for i in range(3) for j in range(3)]
            row = [board[x][j] for j in range(9)]
            col = [board[i][y] for i in range(9)]
            for i in "123456789":
                if not any([i in box, i in col, i in row]):
                    board[x][y] = i
                    dfs(board, stack1, stack2)
                    if not stack1:
                        return
            board[x][y] = "."
            pos = stack2.pop()
            stack1.append(pos)

        stack1 = [(i, j) for i in range(9) for j in range(9) if board[i][j] == "."]
        stack2 = []
        dfs(board, stack1, stack2)
