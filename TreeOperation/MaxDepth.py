"""
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

说明: 叶子节点是指没有子节点的节点。

示例：
给定二叉树 [3,9,20,null,null,15,7]，

    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution(object):
    # def maxDepth(self, root):
    #     """
    #     递归计算深度，每个节点的深度等于左右子节点深度较大的那个加一
    #     遇到叶节点返回0，深度不增加
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 超出时间限制
    def maxDepth(self, root):
        """
        广度遍历计数
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        deque = collections.deque()
        deque.append(root)
        depth = 0
        while deque is not None:
            depth += 1
            size = len(deque)
            # 弹出这一层的节点
            for i in range(size):
                node = deque.pop()
                if node.left is not None:
                    deque.append(node.left)
                if node.right is not None:
                    deque.append(node.right)
        return depth









