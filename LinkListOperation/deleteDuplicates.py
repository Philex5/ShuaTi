# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 下午2:56
# @Author  : Philex
# @File    : deleteDuplicates.py
# @Software: PyCharm

"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        思路:  构造一个list保存已有的数值,遍历链表,节点数值已存在则删除节点
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not head:
            return
        unique = []
        prev, node = None, head
        while node:
            if node.val not in unique:
                unique.append(node.val)
                prev, node = node, node.next
            else:
                prev.next = node.next
                node = node.next

        return head

lnode1 = ListNode(1)
lnode2 = ListNode(1)
lnode3 = ListNode(1)
# lnode4 = ListNode(3)
# lnode5 = ListNode(3)
lnode1.next = lnode2
lnode2.next = lnode3
# lnode3.next = lnode4
# lnode4.next = lnode5
so = Solution()
node = so.deleteDuplicates(lnode1)
while node:
    print(node.val)
    node = node.next





