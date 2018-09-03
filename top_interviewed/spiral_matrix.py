# Author: Allen Anker
# Created by Allen Anker on 03/09/2018
"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""


class Solution(object):
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        r_seen, l_seen = 0, 0
        rows, cols = [r for r in range(m)], [c for c in range(n)]
        # r_direction is the direction that rows index move to, -1, 0, 1 stands for down, no change, up respectively
        # Initially, the rows index doesn't change while the col's index increments
        r_direction, c_direction = 0, 1
        res = []
        next_r, next_c = 0, n - 1
        while len(rows) > 0 and len(cols) > 0:
            if len(cols) == 0:
                break
            for i in cols:
                res.append(matrix[next_r][i])
            next_r = rows[-1]
            rows = rows[1:]

            if len(rows) == 0:
                break
            for i in rows:
                res.append(matrix[i][next_c])
            next_c = cols[0]
            cols = cols[0:-1]

            if len(cols) == 0:
                break
            cols.reverse()
            for i in cols:
                res.append(matrix[next_r][i])
            next_r = rows[0]
            rows = rows[0:-1]
            cols.reverse()

            if len(rows) == 0:
                break
            rows.reverse()
            for i in rows:
                res.append(matrix[i][next_c])
            next_c = cols[-1]
            cols = cols[1:]
            rows.reverse()

        return res


matrix = [
    [3],
    [2]
]
solution = Solution()
print(solution.spiral_order(matrix))
