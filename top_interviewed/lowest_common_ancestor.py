# Author: Allen Anker
# Created by Allen Anker on 22/09/2018
"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q
as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowest_common_ancestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # the recursion call reaches the end or one of the two nodes is found
        if root in (None, p, q): return root
        left, right = (self.lowest_common_ancestor(kid, p, q)
                       for kid in (root.left, root.right))
        # one or both the nodes are founded
        return root if left and right else left or right
