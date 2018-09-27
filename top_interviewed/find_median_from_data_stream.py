# Author: Allen Anker
# Created by Allen Anker on 27/09/2018
"""
Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
"""
from heapq import *


class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def add_num(self, num):
        small, large = self.heaps
        # the small heap must have the smaller half and have the largest in the half at the top of small heap
        # this can be done by reversing the sign of the num
        # find the current smallest in large after pushing num into large, negative, so it becomes largest in small
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def find_median(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0


obj = MedianFinder()
obj.add_num(1)
obj.add_num(2)
print(obj.find_median())
obj.add_num(3)
obj.add_num(1)
obj.add_num(0)
print(obj.find_median())
