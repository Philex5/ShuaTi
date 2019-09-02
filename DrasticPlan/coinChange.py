"""
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1
说明:
你可以认为每种硬币的数量是无限的

leetcode 322
"""

import sys
class Solution(object):
    def coinChange(self, coins, amount):
        """
        思路：
        关键点解析： 动态规划，子问题
        dp[i] 表示组成i块钱，需要最少的硬币数
        如果不拿第j种硬币，硬币数dp[i]
        如果拿第j种硬币，硬币数为dp[i-count[j]] + 1
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        # i表示当前总额
        # j表示使用的是第几种面额的钱
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i - coins[j] > 0:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1


so = Solution()
print(so.coinChange([1, 2, 5], 1))