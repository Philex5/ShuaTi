"""
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        """
        难点： 起点不一定是根节点，终点也不一定是叶节点，可以是任意树节点， 感觉很复杂
        可以递归呀，对每个子树的根节点计算开始计算+ 从根节点的左右子节点计算
        """
        if not root:
            return 0
        def findPath(node, sum):
            if not node:
                return 0
            sum -= node.val
            temp = 1 if sum == 0 else 0
            # 计算以node为起点的sum， 利用node的值更新sum
            return temp + findPath(node.left, sum) + findPath(node.right, sum)
        # 以当前节点为根节点算的路径和 + 左右子节点为根节点算的路径和
        res = findPath(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return res


so = Solution()
node1 = TreeNode(10)
node2 = TreeNode(5)
node3 = TreeNode(-3)
node4 = TreeNode(3)
node5 = TreeNode(2)
node6 = TreeNode(11)
node7 = TreeNode(3)
node8 = TreeNode(-2)
node9 = TreeNode(1)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node4.left = node7
node4.right = node8
node5.right = node9
print(so.pathSum(node1, 8))




