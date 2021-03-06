# Author: Allen Anker
# Created by Allen Anker on 21/07/2018
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def merge_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :param l1: Head of linked list one
        :param l2: Head of linked list two
        :rtype: ListNode
        """
        head = list = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                list.next = l1
                l1 = l1.next
            else:
                list.next = l2
                l2 = l2.next
            list = list.next
        list.next = l1 or l2
        return head.next


solution = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
merged = solution.merge_two_lists(l1, l2)
while merged:
    print(merged.val, end='->')
    merged = merged.next
