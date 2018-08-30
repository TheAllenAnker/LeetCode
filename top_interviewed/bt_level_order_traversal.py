# Author: Allen Anker
# Created by Allen Anker on 30/08/2018
"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def level_order(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes, res = [root, ], [[root.val], ]
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
                curr_vals = [x.val for x in curr_nodes]
                res.append(curr_vals)
        return res


solution = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(2)
node1.left.left = TreeNode(3)
node1.left.right = TreeNode(3)
node1.right.left = TreeNode(3)
node1.right.right = TreeNode(3)
print(solution.level_order(node1))
