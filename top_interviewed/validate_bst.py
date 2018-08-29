# Author: Allen Anker
# Created by Allen Anker on 29/08/2018
"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_valid_bst(self, root, smaller_than=float('inf'), larger_than=float('-inf')):
        """
        Check if the tree given is a valid binary search tree.
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.val <= larger_than or root.val >= smaller_than:
            return False
        return self.is_valid_bst(root.left, min(smaller_than, root.val), larger_than) and \
               self.is_valid_bst(root.right, smaller_than, max(root.val, larger_than))


solution = Solution()
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node3.left = TreeNode(1)
node2.left = node1
node2.right = node3
print(solution.is_valid_bst(node2))
