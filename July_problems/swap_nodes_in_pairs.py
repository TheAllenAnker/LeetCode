# Author: Allen Anker
# Created by Allen Anker on 23/07/2018
"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.

Note:
Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :param head: head of the Linked list
        :rtype: ListNode
        """
        if head:
            head_copy = head.next if head.next else head
            pre = None
            while head:
                next = head.next
                if not next:
                    break
                if pre:
                    pre.next = next
                head.next = next.next
                next.next = head
                pre, head = head, head.next
            return head_copy


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
# l1.next.next.next = ListNode(5)
new_head = solution.swap_pairs(l1)
while new_head:
    print(new_head.val)
    new_head = new_head.next
