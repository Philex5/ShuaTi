# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 下午8:24
# @Author  : Philex
# @File    : uniquePaths2.py
# @Software: PyCharm

"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。

说明：m 和 n 的值均不超过 100。

示例 1:

输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        和第一题相似的思路,使用动态规划
        dp[x, y] = dp[x-1, y] + dp[x, y-1]
        障碍物所在的格子不予考虑
        """
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        # 第一行和第一列的路径数
        # 没有障碍物的情况下,因为只有下移和右移两种操作,都是1
        # 有障碍物的话,第一行障碍物之后的格子,第一列障碍物之下的格子均为0
        # 当前格子的路径数为1的情况只有之前一个格子路径数为1且当前格子上没有障碍物
        obstacleGrid[0][0] = 1
        dp = [[0] * m for i in range(n)]
        dp[0][0] = 1
        obstacleGrid[0][0] = 1

        for i in range(1, m):
            dp[0][i] = int(dp[0][i-1] == 1 and obstacleGrid[0][i] == 0)
        for j in range(1, n):
            dp[j][0] = int(dp[j-1][0] == 1 and obstacleGrid[j][0] == 0)

        # 然后利用状态方程计算dp数组其他的值
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[n-1][m-1]

    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        改进,不适用额外的数组
        """
        if not obstacleGrid:
            return 0
        if obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            obstacleGrid[0][i] = int(obstacleGrid[0][i-1] == 1 and obstacleGrid[0][i] == 0)
        for j in range(1, n):
            obstacleGrid[j][0] = int(obstacleGrid[j-1][0] == 1 and obstacleGrid[j][0] == 0)

        # 然后利用状态方程计算dp数组其他的值
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[n-1][m-1]



so = Solution()
print(so.uniquePathsWithObstacles([
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]))
print(so.uniquePathsWithObstacles([[1]]))

print(so.uniquePathsWithObstacles([[0, 1]]))





