# Author: Allen Anker
# Created by Allen Anker on 01/09/2018
"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sorted_array_to_bst(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0:
            return None

        return self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.build_tree(nums, start, mid - 1)
        node.right = self.build_tree(nums, mid + 1, end)

        return node
