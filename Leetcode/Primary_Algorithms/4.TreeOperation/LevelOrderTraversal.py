"""
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    # beat 91.98%
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        deque = collections.deque()
        deque.append(root)
        results = []
        while len(deque) != 0:
            result = []
            n = len(deque)
            for i in range(n):
                node = deque.popleft()
                result.append(node.val)
                if node.left is not None:
                    deque.append(node.left)
                if node.right is not None:
                    deque.append(node.right)
            results.append(result)
        return results
