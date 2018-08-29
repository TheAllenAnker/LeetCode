# Author: Allen Anker
# Created by Allen Anker on 28/08/2018
"""
Given a binary tree, return the inorder traversal of its nodes' values.

Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder_traversal(self, root):
        """
        Find the inorder traversal of a binary tree.
        :type root: TreeNode
        :rtype: List[int]
        """
        res, curr = [], root
        stack = []
        if root:
            while curr or stack:
                while curr:
                    stack.append(curr)
                    curr = curr.left
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res


solution = Solution()
root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node2.left = node3
root.right = node2
print(solution.inorder_traversal(root))
