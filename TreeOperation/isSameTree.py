from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        思路： 深度优先搜索,递归解法
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        if not q or not p:
            return False
        if q.val != p.val:
            return False
        return self.isSameTree(q.left, p.left) and \
               self.isSameTree(q.right, p.right)


    def isSameTree(self, p, q):
        """
        思路，深度优先搜索，非递归解法，层次遍历
        :param p:
        :param q:
        :return:
        """
        # 层次遍历的非递归实现就是使用队列
        deq1 = deque()
        deq2 = deque()
        deq1.append(p)
        deq2.append(q)
        while len(deq1) > 0 and len(deq2) > 0:
            node1 = deq1.popleft()
            node2 = deq2.popleft()
            if not self.check(node1, node2):
                return False
            if node1:
                deq1.append(node1.left)
                deq1.append(node1.right)
                deq2.append(node2.left)
                deq2.append(node2.right)
        return True

    def check(node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False






