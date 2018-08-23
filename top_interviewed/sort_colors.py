# Author: Allen Anker
# Created by Allen Anker on 22/08/2018
"""
Given an array with n objects colored red, white or blue, sort them in-place
 so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.


Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's,
 then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


class Solution:
    def sort_colors(self, nums):
        """
        Sort colors
        :type nums: List[int]
        """
        # three pointers for three categories of colors, indicate head index of each color's position
        red, white, blue = 0, 0, len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                # the index blue is not reached yet, so it could be any color
                # so white index should not increment
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1


solution = Solution()
nums = [2, 0, 2, 0, 1, 0, 1, 0, 1, 2]
solution.sort_colors(nums)
print(nums)
