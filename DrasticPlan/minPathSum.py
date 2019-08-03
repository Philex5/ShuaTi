"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""
import sys

class Solution(object):
    def minPathSum(self, grid):
        """
        思路： 可以使用回溯法的标准模板
        但在这里遍历了全部解，与暴力法无异
        所以超出了时间限制
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return None
        m, n = len(grid), len(grid[0])
        def help(i, j, temp, res):
            if i == m-1 and j == n-1:
                return min(temp+grid[i][j], res)
            a = b = sys.maxsize
            if i < m-1:
                a = help(i+1, j, temp + grid[i][j], res)
            if j < n-1:
                b = help(i, j+1, temp + grid[i][j], res)
            return min(a, b)
        return help(0, 0, 0, sys.maxsize)

    def minPathSum1(self, grid):
        """
        思路： 动态规划
        dp[i][j] = grid[i][j] + dp[i+1][j] + dp[i][j+1]
        很常见的一类题目，记住动态规划解法

        :param grid:
        :return:
        """
        if not grid:
            return None
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for i in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m -1 and j != n -1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                elif i != m - 1 and j == n - 1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                elif i != m - 1 and j != n - 1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                else:
                    dp[i][j] = grid[i][j]
        return dp[0][0]

so = Solution()
print(so.minPathSum1([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))


