"""
  将有序数组转换为二叉搜索树
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

示例:

给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # beat 99.7% wwwwwwwwwwwwwwwwwww
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        想得有点复杂，考虑了堆的构造，但未尝不可
        其实这里的考查的是二分查找，不断把数组对半分，相当于以中心值作为子树根节点值构造二叉树。
        """
        if len(nums) == 0:
            return []
        return self.halfSearch(nums, 0, len(nums)-1)


    def halfSearch(self, nums, low, high):
        if low > high:
            return
        if low == high:
            return TreeNode(nums[low])
        mid = (high + low) // 2
        node = TreeNode(nums[mid])
        node.left = self.halfSearch(nums, low, mid - 1)
        node.right = self.halfSearch(nums, mid + 1, high)
        return node


so = Solution()
print(so.sortedArrayToBST([-10, -3, 0, 5, 9]).val)





