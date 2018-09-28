# Author: Allen Anker
# Created by Allen Anker on 28/09/2018
"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
"""


class Solution:
    def count_smaller(self, nums):
        """
        My first instinct: dynamic programming?
        :type nums: List[int]
        :rtype: List[int]
        """
        # mergesort, count the number that jump from right to left
        def sort(enum):
            half = int(len(enum) / 2)
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    # merging from the end, merged array in ascending order
                    if not right or left and left[-1][1] > right[-1][1]:
                        # both left and right half are sorted
                        # when the largest on the right is smaller than left[-1][1], all the right half are smaller
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller


solution = Solution()
nums = [2, 0, 1]
print(solution.count_smaller(nums))
print(list(enumerate(nums)))
