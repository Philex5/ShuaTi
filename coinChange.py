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


class Solution(object):
    def coinChange(self, coins, amount):
        """
        使用回溯法，
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not coins or amount <= 0:
            return -1
        def count(i, amt, c):
            if amt < 0 or i > len(coins) - 1:
                return -1
            if amt == 0:
                return c
            maxCoin = amt // coins[i]
            for m in range(maxCoin):
                c1 = count(i+1, amt - m * coins[i], c+m)
                if c1 == -1:
                    continue
            return c
        return count(0, amount, 0)

so = Solution()
print(so.coinChange([1, 2, 5], 1))