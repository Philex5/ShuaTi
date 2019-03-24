"""

给定一个链表，判断链表中是否有环。

进阶：
你能否不使用额外空间解决此题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # beat 99.1% wowwww
    # def hasCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: bool
    #     使用双指针, 判断快指针是否能够指到慢指针即可判定是否有环
    #     快指针要不断与慢指针拉开距离,这样才能使得有环的时候总能指到慢指针
    #     """
    #     if head is None or head.next is None:
    #         return False
    #     fast = head
    #     slow = head
    #     while fast.next is not None:
    #         fast = fast.next.next
    #         slow = slow.next
    #         if fast == slow:
    #             return True
    #         if fast is None:
    #             return False
    #     return False

    # beat 11.7 虽巧妙但是慢呀,需要遍历一遍,而方法一不一定,快指针走得飞快可能刚过环边上的点就指到了
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        递归法,里面很巧妙的让每个节点的next指向自己，当一遍遍历结束之后，我们会遇到自己指向自己的节点，那说明有环。
        有环的话指向那个之前的点,它的next被改造了指向自己,所以判断有环
        """
        if head is None or head.next is None:
            return False
        if head.next == head:
            return True
        nextNode = head.next
        head.next = head
        iscycle = self.hasCycle(nextNode)

        return iscycle





