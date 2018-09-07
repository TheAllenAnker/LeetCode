# Author: Allen Anker
# Created by Allen Anker on 06/09/2018
"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node
to any node in the tree along the parent-child connections.

The path must contain at least one node and does not need to go through the root.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def max_path_sum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.msum = float('-inf')
        self.get_sum(root)
        return self.msum

    def get_sum(self, node):
        if not node:
            return 0

        ls, rs = self.get_sum(node.left), self.get_sum(node.right)
        max_single_path = max(node.val + max(ls, rs), node.val)
        self.msum = max(self.msum, max_single_path, node.val + ls + rs)
        return max_single_path


solution = Solution()
tree1 = TreeNode(-10)
tree1.left = TreeNode(9)
tree1.right = TreeNode(20)
tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)
print(solution.max_path_sum(tree1))
