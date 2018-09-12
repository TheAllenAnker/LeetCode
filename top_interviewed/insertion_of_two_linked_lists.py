# Author: Allen Anker
# Created by Allen Anker on 12/09/2018
"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def get_intersection_node(self, head1, head2):
        """
        :type head1: ListNode
        :type head2: ListNode
        :rtype: ListNode
        """
        if not head1 or not head2:
            return None
        h1, h2 = head1, head2
        while h1 or h2:
            # if a linked list is shorter
            if h1 == h2:
                return h1
            if h1 and h2:
                h1 = h1.next
                h2 = h2.next
            # if two linked lists has the same node but is not found in the first iteration,
            # then the number of nodes before the first overlapped node must be different
            # so, by doing the following, we can balance the number of nodes the two pointers traverse
            # when h1 reaches the end, redirect it to the head of head2
            elif not h1:
                h1 = head2
                h2 = h2.next
            # similarly...
            elif not h2:
                h2 = head1
                h1 = h1.next
        return None

solution = Solution()
head1 = ListNode(0)
head1.next = ListNode(1)
same = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = same
head2 = ListNode(0)
head2.next = ListNode(1)
head2.next.next = same
print(solution.get_intersection_node(head1, head2).val)
print(same.val)
