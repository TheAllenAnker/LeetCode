# Author: Allen Anker
# Created by Allen Anker on 22/09/2018
"""
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Note:
The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def delete_node(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node = node.next.val
        node.next = node.next.next