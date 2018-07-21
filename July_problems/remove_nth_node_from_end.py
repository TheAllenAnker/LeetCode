# Author: Allen Anker
# Created by Allen Anker on 20/07/2018


"""
Given a linked list, remove the n-th node from the end of list and return its head.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def remove_nth_from_end(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :param head: head node of a linked list
        :param n: the target node for removing
        :rtype: ListNode
        """
        node_left = self.nth_from_end(head, n + 1)
        if not node_left:
            head = head.next
        else:
            node_left.next = node_left.next.next
        return head


    def nth_from_end(self, head, n):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        while n > 1:
            nodes.pop()
            n -= 1

        return nodes.pop() if nodes else None


solution = Solution()
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)
print(solution.remove_nth_from_end(head, 1))