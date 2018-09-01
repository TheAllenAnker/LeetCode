# Author: Allen Anker
# Created by Allen Anker on 31/08/2018
"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_depth(self, root, d=0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            d += 1
            d = max(self.max_depth(root.left, d), self.max_depth(root.right, d))
        return d


solution = Solution()
node1 = TreeNode(1)
# node1.left = TreeNode(2)
# node1.right = TreeNode(2)
# node1.left.left = TreeNode(3)
# node1.left.right = TreeNode(3)
# node1.right.left = TreeNode(3)
# node1.right.right = TreeNode(3)
print(solution.max_depth(node1))
