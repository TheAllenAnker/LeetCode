# Author: Allen Anker
# Created by Allen Anker on 03/09/2018
"""
Given a binary tree's root.
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: None
        """
        nodes = [root, ]
        i = 0
        while i < len(nodes):
            curr_nodes = []
            pre_length = len(nodes)
            while i < pre_length:
                if nodes[i]:
                    if nodes[i].left:
                        curr_nodes.append(nodes[i].left)
                    if nodes[i].right:
                        curr_nodes.append(nodes[i].right)
                i += 1
            if curr_nodes:
                nodes += curr_nodes
                for j in range(len(curr_nodes) - 1):
                    curr_nodes[j].next = curr_nodes[j + 1]


solution = Solution()
node1 = TreeLinkNode(1)
node1.left = TreeLinkNode(2)
node1.right = TreeLinkNode(2)
node1.left.left = TreeLinkNode(3)
node1.left.right = TreeLinkNode(3)
node1.right.left = TreeLinkNode(3)
node1.right.right = TreeLinkNode(3)
solution.connect(node1)
print()
