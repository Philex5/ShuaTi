# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        考虑到二叉搜索树的特性，使用递归方法
        当前节点的值大于等于p小于等于q或者大于等于q小于等于p时满足最近公共祖先
        """
        if root is None:
            return TreeNode(None)
        if ((p.val >= root.val) and (q.val <= root.val)) or ((p.val <= root.val) and (q.val >= root.val)):
            return root
        nodel = self.lowestCommonAncestor(root.left, p, q)
        noder = self.lowestCommonAncestor(root.right, p, q)
        return nodel if noder.val is None else noder

    import collections
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        考虑到二叉搜索树的特性，使用非递归方法
        """
        if ((p.val >= root.val) and (q.val <= root.val)) or ((p.val <= root.val) and (q.val >= root.val)):
            return root

        deq = collections.deque()
        deq.append(root)
        while len(deq) != 0:
            node = deq.pop()
            if ((p.val >= node.val) and (q.val <= node.val)) or ((p.val <= node.val) and (q.val >= node.val)):
                return node
            if node.left is not None and p.val <= node.val and q.val <= node.val:
                deq.append(node.left)
            elif node.right is not None and p.val >= node.val and q.val >= node.val:
                deq.append(node.right)
            else:
                return TreeNode(None)






