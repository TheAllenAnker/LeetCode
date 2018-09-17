# Author: Allen Anker
# Created by Allen Anker on 16/09/2018
"""
Reverse a singly linked list.

Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # iteratively
    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre, curr = None, head
        while curr:
            next = curr.next
            curr.next = pre
            pre = curr
            if next:
                curr = next
            else:
                break
        return curr

    # recursively
    def reverse_list2(self, head):
        if not head or not head.next:
            return head
        # the recursion call ends in the node before the last node
        pre = self.reverse_list2(head.next)
        head.next.next = head
        # change the head.next so the previous recursion ends and reverse the nodes before
        head.next = None
        return pre


solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head = solution.reverse_list(head)
print()
