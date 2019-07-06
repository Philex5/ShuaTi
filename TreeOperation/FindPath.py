# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 下午5:26
# @Author  : Philex
# @File    : FindPath.py
# @Software: PyCharm
"""
剑指offer 面试题34: 二叉树中和为某一值的路径
找出一条路径,上面的树节点的值和为给定的值
"""
class Solution():
    def findPath(self, root, target):
        if root is None:
            return
        cur = 0
        res = []

        def calPathSum(root, cur, target, temp):
            if cur == target and not root.left and not root.right:
                res.append(temp)
                return

            if root.left:
                calPathSum(root.left, cur + root.left.val, target,
                                temp+[root.left.val])
            if root.right:
                calPathSum(root.right, cur + root.right.val, target,
                                temp+[root.right.val])

        calPathSum(root, cur+root.val, target, [root.val])
        return res

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8

so = Solution()
print(so.findPath(node1, 7))