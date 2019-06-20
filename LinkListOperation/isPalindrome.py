"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # # beat 8.51%
    # def isPalindrome(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     双指针 + 栈
    #     """
    #     if head is None or head.next is None:
    #         return False
    #
    #     fast = head
    #     slow = head
    #
    #     vals = []
    #
    #     while fast is not None and fast.next is not None:
    #         vals.append(slow.val)
    #         slow = slow.next
    #         fast = fast.next.next
    #
    #     if fast is not None:
    #         slow = slow.next
    #     l = len(vals)
    #     i = 0
    #     while slow is not None:
    #         if slow.val != vals[l-i]:
    #             return False
    #         slow = slow.next
    #         i += 1
    #     return True

    # 45.55%
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        O(1)
        """
        if head is None or head.next is None:
            return True
        fast = head
        slow = head

        vals = []

        while fast is not None and fast.next is not None:
            vals.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast is not None:
            slow = slow.next

        slow = slow.next

        s0 = None
        s1 = slow
        while s1 is not None:
            s2 = s1.next
            s1.next = s0
            s0 = s1
            s1 = s2

        while slow.next is not None:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

















