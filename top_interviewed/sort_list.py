# Author: Allen Anker
# Created by Allen Anker on 11/09/2018
"""
Sort a linked list in O(n log n) time using constant space complexity.
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sort_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # split the linked list in half
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None

        h1 = self.sort_list(head)
        h2 = self.sort_list(slow)
        return self.merge(h1, h2)

    def merge(self, h1, h2):
        # Only one of h1 and h2 can be None at the end
        # Use a pen and a sheet of paper to simulate the merge process, then it's easier to understand
        if not h1:
            return h2
        if not h2:
            return h1
        if h1.val < h2.val:
            h1.next = self.merge(h1.next, h2)
            return h1
        else:
            h2.next = self.merge(h2.next, h1)
            return h2
