"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？


例如，上图是一个7 x 3 的网格。有多少可能的路径？

说明：m 和 n 的值均不超过 100。

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
"""


class Solution:
    # def uniquePaths(self, m, n):
    #     """
    #     动态规划:
    #     (0, 0) --> (m-1, n-1)
    #     paths[x][y] = paths[x-1][y] + [x][y-1]
    #     paths[0][1] = 1
    #     paths[1][0] = 1
    #     O(n**2)
    #     :param m: 格子行数
    #     :param n: 格子列数
    #     :return: 路径条数
    #     """
    #     if m <= 0 or n <= 0:
    #         return
    #     if m == 1 or n == 1:
    #         return 1
    #     paths = [[0]*n for i in range(m)]
    #     paths[0][1] = 1
    #     paths[1][0] = 1
    #     for i in range(0, m):
    #         for j in range(0, n):
    #             if (i == 0 and j == 0) or (i == 0 and j == 1) or (i == 1 and j == 0):
    #                 continue
    #             if i == 0:
    #                 paths[0][j] = paths[0][j-1]
    #             if j == 0:
    #                 paths[i][j] = paths[i-1][j]
    #             paths[i][j] = paths[i-1][j] + paths[i][j-1]
    #     return paths[m-1][n-1]
    def uniquePaths(self, m, n):
        """优化1: 简洁"""
        dp = [[1]*n for i in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

so = Solution()
print(so.uniquePaths(7, 3))



