# Author: Allen Anker
# Created by Allen Anker on 29/10/2018
"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.
"""
from queue import PriorityQueue


class Tuple:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def kth_smallest(self, matrix, k):
        """
        Build a min-heap with the first row elements, then poll out k - 1 times and replace the polled out
        one with the next element in the same column.
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return None
        pq = PriorityQueue()
        rows = len(matrix)
        for i in range(len(matrix[0])):
            pq.put(Tuple(0, i, matrix[0][i]))
        for i in range(k - 1):
            t = pq.get()
            if t.x == rows - 1: continue
            pq.put(Tuple(t.x + 1, t.y, matrix[t.x + 1][t.y]))
        return pq.get().val


solution = Solution()
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(solution.kth_smallest(matrix, k))
