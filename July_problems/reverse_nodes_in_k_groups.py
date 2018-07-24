# Author: Allen Anker
# Created by Allen Anker on 23/07/2018
"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverse_k_group(self, head, k):
        """
        :param head: head node of linked list
        :param k: reverse in k groups
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0
            # use r to locate the range
            while r and count < k:
                r = r.next
                count += 1
            # if size k satisfied, reverse the inner linked list
            if count == k:
                pre, cur = r, l
                # standard reversing of k nodes, the key of this algorithm
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                # connect two k-groups
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next


solution = Solution()
l1 = ListNode(0)
l1.next = ListNode(1)
l1.next.next = ListNode(2)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(4)
new_head = solution.reverse_k_group(l1, 2)
while new_head:
    print(new_head.val)
    new_head = new_head.next
