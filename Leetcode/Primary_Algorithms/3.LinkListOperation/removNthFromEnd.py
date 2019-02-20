"""

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # beat 49.95%
    # def removeNthFromEnd(self, head, n):
    #     """
    #     :type head: ListNode
    #     :type n: int
    #     :rtype: ListNode
    #     先计数再遍历的蛮办法,需要遍历链表两次,时间复杂度2N
    #     """
    #     # 链表为空的情况
    #     if head is None:
    #         return
    #     # 统计节点个数
    #     count = 1
    #     node = head.next
    #     while node is not None:
    #         count += 1
    #         node = node.next
    #
    #     # 从头开始遍历
    #     iters = count - n
    #
    #     node = head
    #     if iters == 0:
    #         head.val = head.next.val
    #         head.next = head.next.next
    #         return head
    #     for i in range(iters-1):
    #         node = node.next
    #
    #     node.val = node.next.val
    #     node.next = node.next.next
    #     return head

    # beat 87.26%
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        如何通过一次扫描解决?
        使用双指针,指针之间的举例为N,当一个指针指向最后一个元素时,前一个指针指向待删除的节点的前一个节点

        """
        # 链表为空的情况
        if head is None:
            return

        pre = head
        post = head
        while n > 0:
            pre = pre.next
            n -= 1
        if pre is None: # n=len(head)
            return head.next
        while pre.next is not None:
            pre = pre.next
            post = post.next

        post.next = post.next.next

        return head













