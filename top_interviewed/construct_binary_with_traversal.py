# Author: Allen Anker
# Created by Allen Anker on 01/09/2018
"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, preorder, inorder, node=None):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder:
            if not node:
                node = TreeNode(preorder[0])
            head = node
            h_i = inorder.index(preorder[0])
            if h_i != 0:
                if len(preorder) > 1:
                    node.left = TreeNode(preorder[1])
                    self.build_tree(preorder[1:h_i + 1], inorder[0:h_i], node.left)
            if h_i != len(inorder) - 1:
                if len(preorder) > h_i + 1:
                    node.right = TreeNode(preorder[h_i + 1])
                    self.build_tree(preorder[h_i + 1:], inorder[h_i + 1:], node.right)
            return head


preorder = [1, 2, 3]
inorder = [3, 2, 1]
solution = Solution()
head = solution.build_tree(preorder, inorder)
