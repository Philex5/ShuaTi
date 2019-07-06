# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 下午9:03
# @Author  : Philex
# @File    : numTrees.py
# @Software: PyCharm
"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        思路: 回溯法,其实不是啦,分到左右子结点在重复过程,这样做只能考虑到一边的情况
        忽略了左右两个子树结构的组合
        注意,题目要求是二叉搜索树,左子节点小于根节点,右子节点大于等于根节点
        """
        # if n <= 0:
        #     return 0
        # def countNumTree(count, results):
        #     count -= 1
        #     if count == 0:
        #         results += 1
        #         return results
        #     # 只有左边有子节点
        #     resleft = countNumTree(count, results)
        #     # 只有右边有子节点
        #     resright = countNumTree(count, results)
        #     # 两边都有子节点
        #     twoside = 0
        #     if count >= 2:
        #         for c in range(1, count):
        #             left = countNumTree(c, results)
        #             right = countNumTree(count-c, results)
        #             twoside = left * right
        #     return resleft + resright + twoside
        # res = countNumTree(n, 0)
        # return res

        """
        思路: 动态规划: 神奇的卡特兰数
        假设n个节点存在二叉排序树的个数是G(n)，令f(i)为以i为根的二叉搜索树的个数，则
        G(n) = f(1) + f(2) + f(3) + f(4) + ... + f(n)

        当i为根节点时，其左子树节点个数为i-1个，右子树节点为n-i，则
        f(i) = G(i-1)*G(n-i)
        
        综合两个公式可以得到 卡特兰数 公式
        G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]
        return dp[n]


so = Solution()
print(so.numTrees(4))

