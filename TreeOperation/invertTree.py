# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 下午2:26
# @Author  : Philex
# @File    : invertTree.py
# @Software: PyCharm

"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        """
        把每个节点的左子节点和右子节点互换即可
        """
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

import sys
sys.path.append('/media/philex/File/Learning/codingPractice/TreeOperation')
from TreeSearch import BreadthFirstSearch

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
print(so.invertTree(node1))
print(node1.val)
_ = BreadthFirstSearch(node1)