# Author: Allen Anker
# Created by Allen Anker on 27/09/2018
"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules
(taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously.
"""


class Solution:
    def game_of_life(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                count = 0
                # its neighbors
                for a in range(max(0, i - 1), min(i + 2, row)):
                    for b in range(max(0, j - 1), min(j + 2, col)):
                        count += board[a][b] & 1
                # all the conditions that the next state will be "live"
                if count == 3 or count - board[i][j] == 3:
                    board[i][j] |= 2

        for i in range(row):
            for j in range(col):
                board[i][j] >>= 1
