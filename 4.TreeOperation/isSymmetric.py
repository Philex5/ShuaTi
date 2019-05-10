"""
对称二叉树
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
说明:

如果你可以运用递归和迭代两种方法解决这个问题，会很加分。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
import copy
class Solution:
    # beat 99.88%
    # def isSymmetric(self, root):
    #     """递归解法"""
    #     if root is None:
    #         return False
    #     return self.judge(root.left, root.right)
    #
    # def judge(self, root1, root2):
    #     if root1 is None and root2 is None:
    #         return True
    #     if root1 is None or root2 is None or root1.val != root2.val:
    #         return False
    #     return self.judge(root1.right, root2.left) and self.judge(root1.left, root2.right)
    # beat 36.22，纳尼，比我的还慢，可能是循环次数多吧，时间慢，空间少，我的时间少，空间多
    def isSymmetric(self, root):
        """迭代解法
        和我之前的做法很相似，成对放入栈成对取出比较，而我是每次比较一个层的节点值组成的列表
        """
        if root is None:
            return True
        rleft = root.left
        rright = root.right
        deque = collections.deque()
        deque.append(rleft)
        deque.append(rright)
        while len(deque) != 0:
            p = deque.pop()
            q = deque.pop()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            if p.val == q.val:
                deque.append(p.right)
                deque.append(q.left)
                deque.append(p.left)
                deque.append(q.right)
        return True


    ## beat 71.88%
    # def isSymmetric(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     迭代解法,很笨的方法，层次遍历，再取出每层的节点的值，看是否对称
    #     这么费时费空间的做法还能战胜70%+。。。
    #     """
    #     if root is None:
    #         return True
    #     deque = collections.deque()
    #     deque.append(root)
    #     while len(deque) != 0:
    #         n = len(deque)
    #         deque2 = copy.copy(deque)
    #         for i in range(n):
    #             node = deque.popleft()
    #             deque2.popleft()
    #             print(node.val)
    #             if node.left is not None:
    #                 deque.append(node.left)
    #                 deque2.append(node.left)
    #             else:
    #                 # 不存在补上值为0的节点
    #                 deque2.append(TreeNode(0))
    #             if node.right is not None:
    #                 deque.append(node.right)
    #                 deque2.append(node.right)
    #             else:
    #                 deque2.append(TreeNode(0))
    #         while len(deque2) != 0:
    #             head = deque2.popleft()
    #             print(head.val)
    #             if len(deque2) == 0:
    #                 return False
    #             tail = deque2.pop()
    #             if head.val != tail.val:
    #                 return False
    #     return True

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7
    node5.right = node8
    so = Solution()
    print(so.isSymmetric(node1))