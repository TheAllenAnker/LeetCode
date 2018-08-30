# Author: Allen Anker
# Created by Allen Anker on 29/08/2018
"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def is_symmetric(self, root):
        """
        Check if the binary tree is symmetric.
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left and root.right and (root.left.val == root.right.val):
            left, right = [root.left, ], [root.right, ]
            for x, y in zip(left, right):
                if not x and not y:
                    continue
                if not x or not y: return False
                if x.val != y.val: return False
                left.append(x.right)
                right.append(y.left)
                left.append(x.left)
                right.append(y.right)
            return True
        return False


solution = Solution()
node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(2)
node1.left.right = TreeNode(3)
node1.right.right = TreeNode(3)
print(solution.is_symmetric(node1))
node2 = TreeNode(1)
node2.left = TreeNode(2)
node2.right = TreeNode(2)
node2.left.left = TreeNode(3)
node2.left.right = TreeNode(4)
node2.right.left = TreeNode(4)
node2.right.right = TreeNode(3)
print(solution.is_symmetric(node2))
node3 = TreeNode(1)
print(solution.is_symmetric(node3))
node4 = TreeNode(1)
node4.left = TreeNode(2)
node4.right = TreeNode(2)
node4.left.right = TreeNode(3)
node4.right.left = TreeNode(3)
node4.right.left.right = TreeNode(3)
print(solution.is_symmetric(node4))
