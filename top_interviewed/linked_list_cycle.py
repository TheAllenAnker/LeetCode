# Author: Allen Anker
# Created by Allen Anker on 10/09/2018
"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # This was my first instinct.
        # And there is a fast-slow two pointers solution.
        '''
        if not head:
            return False
        while head:
            if head.val == 'a':
                return True
            head.val = 'a'
            head = head.next
        return False
        '''
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
