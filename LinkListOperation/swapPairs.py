"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。



示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        second = head.next
        head.next = second.next
        second.next = head
        first = second
        second = head
        third = head.next
        print(third.val)
        while third is not None:
            node = third.next
            if node is None:
                return first
            third.next = node.next
            second.next = node
            node.next = third
            second = third
            third = third.next

        return first


node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(6)
node6 = ListNode(2)
node7 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

so = Solution()
first = so.swapPairs(node1)
while first is not None:
    print(first.val)
    first = first.next



