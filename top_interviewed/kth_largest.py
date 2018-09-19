# Author: Allen Anker
# Created by Allen Anker on 19/09/2018
"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution:
    def find_kth_largest(self, nums, k):
        """
        Using the quicksort. The pivot might happen to be kth largest number, cause it divides the list into
        the two parts (the left part is smaller and the right part is larger)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # A little problem with this solution
        '''
        # nums[p] is the (p+1)th largest number
        l, r = 0, len(nums) - 1
        while True:
            # the partition method return the pivot's index
            p = self.partition(nums, l, r)
            if p + 1 < k:
                l = p
            elif p + 1 > k:
                r = p
            else:
                break
        return nums[p]

    def partition(self, nums, l, r):
        # the pivot is nums[i]
        l, r = i + 1, j
        while l < r:
            while l < r and nums[l] >= nums[i]:
                l += 1
            while l < r and nums[r] <= nums[i]:
                r -= 1
            if l == r:
                l = l - 1 if nums[l] < nums[i] else l
                break
            nums[l], nums[r] = nums[r], nums[l]
        nums[i], nums[l] = nums[l], nums[i]
        return l
        '''
        return sorted(nums, reverse=True)[k-1]




solution = Solution()
nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(solution.find_kth_largest(nums, k))
