"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 


示例 1:

输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
示例 2:

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。
示例 3:

输入: amount = 10, coins = [10]
输出: 1
 

注意:

你可以假设：

0 <= amount (总金额) <= 5000
1 <= coin (硬币面额) <= 5000
硬币种类不超过 500 种
结果符合 32 位符号整数

"""


class Solution(object):
    def change(self, amount, coins):
        """
        回溯法,使用模板，排序解决重复使用问题
        超出时间限制
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount == 0:
            return 1
        if not coins:
            return 0
        if amount < coins[0]:
            return 0
        global c
        c = 0
        coins.sort()
        def helper(i, count):
            global c
            if count == amount:
                c += 1
                return
            for j in range(i, len(coins)):
                if count + coins[j] > amount:
                    break
                helper(j, count + coins[j])
        helper(0, 0)
        return c

    def change2(self, amount, coins):
        """
        动态规划，完全背包问题
        :param amount:
        :param coins:
        :return:
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins.sort()
        # 这里不能先amount循环，再coins循环
        # 因为i并不需要加上所有i-coin，dp[5] = dp[4] + dp[3] + dp[0]不合理
        # 要先coins循环再amount循环
        # 相当于每次将金币分配到各个位置，+coin[1],利用i-coin积累的数量
        for coin in coins:
            for i in range(coin, amount+1):
                # 不是取最少或者最多，而是求总的方案数
                # dp[i] = max(dp[i], dp[i-coin] + 1)
                dp[i] += dp[i - coin]
        print(dp)
        return dp[-1]


so = Solution()
print(so.change2(5, [1, 2, 5]))


