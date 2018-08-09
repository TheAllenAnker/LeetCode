# Author: Allen Anker
# Created by Allen Anker on 08/08/2018
"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""


class Solution:
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def is_valid_list(nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            checked = []
            values = [str(i) for i in range(1, 10)] + ['.']
            for num in nums:
                if num not in values:
                    return False
                if num in checked and num != '.':
                    return False
                checked += num
            return True

        for row in range(9):
            if not is_valid_list(board[row]):
                return False
        for col in range(9):
            to_check = []
            for row in range(9):
                to_check += board[row][col]
            if not is_valid_list(to_check):
                return False

        for row in range(0, 9, 3):
            to_check = []
            for i in range(row, row + 3):
                for col in range(3):
                    to_check += board[i][col]
            if not is_valid_list(to_check):
                return False
            to_check = []
            for i in range(row, row + 3):
                for col in range(3, 6):
                    to_check += board[i][col]
            if not is_valid_list(to_check):
                return False
            to_check = []
            for i in range(row, row + 3):
                for col in range(6, 9):
                    to_check += board[i][col]
            if not is_valid_list(to_check):
                return False

        return True


solution = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

print(solution.is_valid_sudoku(board))
