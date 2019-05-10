# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
         一般二叉树
         使用递归的方法，递归向下找，找到向上返回节点
         想到了递归的方法，为什么没有做出来？
         返回状态搞错，返回True和False，其实这样无法判断准确的祖先祖先节点的位置，它之上的点都为True
         应该返回节点
        """
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 都不为空，在以root节点为根节点的子树中
        if left is not None and right is not None:
            return root
        # 都为空，不在以root节点为根节点的子树中
        if left is None and right is None:
            return None
        # 一个子节点不为空，说明p或q 或者全部在以该子节点为根节点的子树中
        return left if right is None else right
