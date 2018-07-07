# Author: Allen Anker
# Created by Allen Anker on 01/07/2018


"""
We are given a binary tree (with root node root), a target node, and an integer value `K`.
Return a list of the values of all nodes that have a distance K from the target node.
The answer can be returned in any order.

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distance_k(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        def dfs(node, par=None):
            if node:
                node.par = par  # find the parent of each node, using a new node to store the parents
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])  # a tuple list
        seen = {target}  # store iterated nodes
        while queue:
            #  the current nodes in queue have the same distances to the target node
            if queue[0][1] == k:  # if the distance to the target is k
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            # iterate through all its neighbors,
            # starting from the target node
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return []