# Author: Allen Anker
# Created by Allen Anker on 30/09/2018
"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def odd_even_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy1 = odd = ListNode(0)
        dummy2 = even = ListNode(0)
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
        odd.next = dummy2.next
        return dummy1.next


node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(4)
node1.next.next.next.next = ListNode(5)
solution = Solution()
solution.odd_even_list(node1)
print()
