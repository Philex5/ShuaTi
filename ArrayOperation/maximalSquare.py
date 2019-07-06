# -*- coding: utf-8 -*-
# @Time    : 2019/6/22 上午11:23
# @Author  : Philex
# @File    : maximalSquare.py
# @Software: PyCharm
"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:

输入:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

输出: 4

"""

class Solution:
    def maximalSquare(self, matrix) -> int:
        """
        暴力法: 纪录迄今为止发现的最大正方形的边长
        遍历矩阵,对每个'1'寻找它能找到的最大的正方形
        具体做法是,双指针,一个往右一个往下来遍历,检查该行和列是否全为1
        时间复杂度: O(n^3)
        空间复杂度: O(1)
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        maxSquare = 0
        for i in range(row):
            for j in range(col):

                if matrix[i][j] == '1':
                    tempFlag = True
                    tempSquare = 1
                    while i + tempSquare < row and j + tempSquare < col and tempFlag:
                        for k in range(j, j + tempSquare+1):
                            if matrix[i + tempSquare][k] == '0':
                                tempFlag = False
                                break
                        for k in range(i, i + tempSquare+1):
                            if matrix[k][j + tempSquare] == '0':
                                tempFlag = False
                                break
                        if tempFlag:
                            tempSquare += 1
                    maxSquare = tempSquare if tempSquare > maxSquare else maxSquare
        return maxSquare ** 2

    def maximalSquare1(self, matrix) -> int:
        """
        思路二: 动态规划
        时间复杂度 O(mn)
        空间复杂度 O(mn)
        """
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        # 下一行取决于上一行,所有
        dp = [[0] * (col+1) for i in range(row+1)]
        maxSquare = 0
        for i in range(1, row+1):
            for j in range(1, col+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxSquare = max(maxSquare, dp[i][j])
        return maxSquare ** 2

    def maximalSquare2(self, matrix) -> int:
        """
        思路三: 动态规划优化
        pass
        """




so = Solution()
print(so.maximalSquare1([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))




