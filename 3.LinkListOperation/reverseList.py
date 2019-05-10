"""
反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # # beat 63.6
    # def reverseList(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     递归解法:
    #     """
    #     if head is None:
    #         return head
    #     if head.next is None:
    #         return head
    #     return self.reverse(None, head)
    #
    # def reverse(self, node, nodeNext):
    #     if node is None:
    #         self.reverse(nodeNext, nodeNext.next)
    #     if nodeNext == None:
    #         return node
    #     nodeNextN = nodeNext.next
    #     nodeNext.next = node
    #     return self.reverse(nodeNext, nodeNextN)

    # beat 99.41 wowwwwwwwwww!
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        迭代解法: 从递归的思路而来
        """
        if head is None or head.next is None:
            return head
        node1 = None
        node2 = head
        node3 = head.next
        while node3 is not None:
            node2.next = node1
            node1 = node2
            node2 = node3
            node3 = node2.next
        node2.next = node1
        return node2


