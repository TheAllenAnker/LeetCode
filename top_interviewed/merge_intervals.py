# Author: Allen Anker
# Created by Allen Anker on 04/09/2018
"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
"""

from collections import defaultdict


# Definition for Interval
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        Sort the intervals, so that the intervals start positions are in ascending order,
        then merge the overlapped ones.
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        # Sort the intervals by their start values
        intervals.sort(key=lambda x: x.start)
        res = []
        for interval in intervals:
            # Just append it if there is no overlapped part
            if not res or interval.start > res[-1].end:
                res.append(interval)
            else:
                res[-1].end = max(interval.end, res[-1].end)
        return res
