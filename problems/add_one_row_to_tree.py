# Author: Allen Anker
# Created by Allen Anker on 26/06/2018


"""
Given the root of a binary tree, then value v and depth d,
you need to add a row of nodes with value v at the given depth d.
The root node is at depth 1.

The adding rule is: given a positive integer depth d,
for each NOT null tree nodes N in depth d-1,
create two tree nodes with value v as N's left subtree root and right subtree root.
And N's original left subtree should be the left subtree of the new left subtree root,
its original right subtree should be the right subtree of the new right subtree root.
If depth d is 1 that means there is no depth d-1 at all,
then create a tree node with value v as the new root of the whole original tree,
and the original tree is the new root's left subtree.
"""


class TreeNode:
    pass


class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        # get the nodes at depth (d-1)
        for _ in range(d - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        # add new nodes at depth (d-1)
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left



solution = Solution()
