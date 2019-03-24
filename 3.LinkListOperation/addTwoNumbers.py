# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2) -> ListNode:
        """
        最直接的方法：遍历两个链表到最后，执行加操作
        Q：l1，l2为空之后，继续执行增加一个节点，导致最后多一位0
        A：加一个判断，都为空直接结束
        Q：其中一个链表对应的数位数多一位 1 8 + 2
        A：有一个不为空则继续加，只不过不加为空的那个链表的值，None.val报错，
           遍历的时候也忽略为空的那个
        Q：还有最后可能也有进位 5 + 5
        A: 判断都为空的时候再判断进位标志位是否为1，是的话一个节点值为1
        """
        head = ListNode(0)
        l3 = head
        addon = 0
        while l1 is not None or l2 is not None:
            if l1 is None:
                tmp = l2.val + addon * 1
            elif l2 is None:
                tmp = l1.val + addon * 1
            else:
                tmp = l1.val + l2.val + addon * 1
            addon = 0
            if tmp >= 10:
                l3.val = tmp - 10
                addon = 1
            else:
                l3.val = tmp
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            # 考虑最后进1的问题
            if l1 is None and l2 is None and addon == 0:
                break
            if l1 is None and l2 is None and addon == 1:
                node = ListNode(1)
                l3.next = node
                break
            node = ListNode(0)
            l3.next = node
            l3 = node
        return head

    def addTwoNumbers1(self, l1, l2) -> ListNode:
        """递归解法， cool"""
        """都是空，返回空，一个为空，返回另外一个，虽然算是我的迭代版本的递归形式，但简洁太多了
        我的做法需要太多的if，容易出错"""
        if not l1 and not l2:
            return None
        elif not (l1 and l2):
            return l1 or l2
        else:
            if l1.val + l2.val < 10:
                l3 = ListNode(l1.val + l2.val)
                l3.next = self.addTwoNumbers(l1.next, l2.next)
            else:
                l3 = ListNode(l1.val + l2.val - 10)
                l3.next = self.addTwoNumbers(l1.next, self.addTwoNumbers(l2.next, ListNode(1)))
        return l3

    def addTwoNumbers2(self, l1, l2) -> ListNode:
        """
        改进版，去除进位标志，大于10，之后的节点值+1
        """
        head = ListNode(0)
        l3 = head
        while l1 is not None or l2 is not None:
            if l1 is None:
                tmp = l2.val
            elif l2 is None:
                tmp = l1.val
            else:
                tmp = l1.val + l2.val
            if tmp >= 10:
                l3.val = tmp - 10
                if l2.next is not None:
                    l2.next.val += 1
                else:
                    l2.next = ListNode(1)
            else:
                l3.val = tmp
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            if l2 is None and l1 is None:
                break
            node = ListNode(0)
            l3.next = node
            l3 = node
        return head
so = Solution()
node11 = ListNode(2)
node21 = ListNode(5)
node12 = ListNode(4)
node13 = ListNode(3)
node11.next = node12
node12.next = node13
node22 = ListNode(6)
node23 = ListNode(4)
node21.next = node22
node22.next = node23

l3 = so.addTwoNumbers(node11, node21)
while l3 is not None:
    print(l3.val)
    l3 = l3.next



