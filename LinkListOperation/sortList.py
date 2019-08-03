"""
在 O(nlogn) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

leetcode 148
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList0(self, head):
        """
        思路1: 把链表所有节点的数值保存进一个列表，排序后，
               在按照排序好的值依次给链表的节点赋值
        :type head: ListNode
        :rtype: ListNode
        时间复杂度： O(n)
        空间复杂度： O(n)
        不满足题目要求
        """
        if not head:
            return None
        node = head
        vals = []
        while node:
            vals.append(node.val)
            node = node.next
        vals = sorted(vals)
        node = head
        for val in vals:
            node.val = val
            node = node.next
        return head
    def sortList(self, head):
        """
        为了满足题目的要求，需要使用归并排序
        1. 自顶向下的归并排序
        :param head:
        :return:
        """
        if not head:
            return None
        # 快慢指针找出中点
        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None
        # 迭代排序
        left, right = self.sortList(head), self.sortList(mid)
        # 合并排序结果
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next = left
                left = left.next
            else:
                h.next = right
                right = right.next
            h = h.next
        h.next = left if left else right
        return res.next

    def sortList1(self, head):
        """
        为了满足题目的要求，需要使用归并排序
        2. 自底向上的归并排序
        :param head:
        :return:
        """
        if not head:
            return None
        h, length, intv = head, 0, 1
        while h:
            h, length = h.next, length + 1
            res = ListNode(0)
            res.next = head
            # 合并不同间隔的节点
            while intv < length:
                pre, h = res, res.next
                while h:
                    # get the two merge head 'h1', 'h2':
                    h1, i = h, intv
                    while i and h:
                        h, i = h.next, i-1
                    h2, i = h, intv
                    while i and h:
                        h, i = h.next, i-1
                    c1, c2 = intv, intv-i  # the `c2`: length of `h2` can be small than the `intv`.
                    while c1 and c2:
                        if h1.val < h2.val:
                            pre.next, h1, c1 = h1, h1.next, c1 - 1
                        else:
                            pre.next, h2, c2 = h2, h2.next, c2 - 1
                        pre = pre.next
                    pre.next = h1 if h1 else h2
                    # 再走几步
                    while c1 > 0 or c2 > 0:
                        pre, c1, c2 = pre.next, c1-1, c2-1
                        pre.next = h
                intv *= 2















