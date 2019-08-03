"""
编写一个程序，找到两个单链表相交的起始节点。
leetcode 160
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        剑指offer相似题目，思路：
        先遍历一遍，比较一下两个链表的长度差，
        因为有重叠的话，重叠部分长度是一样的，假设长的比短的长k，可以先遍历长的链表k个结点，
        之后长链表和短链表一起遍历，第一个值相同的节点就是相交的起始节点
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l_a = 0
        l_b = 0
        nodeA = headA
        nodeB = headB
        while nodeA:
            nodeA = nodeA.next
            l_a += 1
        while nodeB:
            nodeB = nodeB.next
            l_b += 1
        if l_a > l_b:
            nodeLong = headA
            nodeShort = headB
            dis = l_a - l_b
        else:
            nodeLong = headB
            nodeShort = headA
            dis = l_b - l_a
        while dis > 0:
            nodeLong = nodeLong.next
            dis -= 1
        while nodeLong and nodeShort:
            if nodeLong.val == nodeShort.val:
                return nodeLong.val
            nodeLong = nodeLong.next
            nodeShort = nodeShort.next
        return None

node11 = ListNode(4)
node12 = ListNode(1)
node13 = ListNode(8)
node14 = ListNode(4)
node15 = ListNode(5)
node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node15

node21 = ListNode(5)
node22 = ListNode(0)
node23 = ListNode(1)
node24 = ListNode(8)
node25 = ListNode(4)
node26 = ListNode(5)
node21.next = node22
node22.next = node23
node23.next = node24
node24.next = node25
node25.next = node26

so = Solution()
print(so.getIntersectionNode(node11, node21))

