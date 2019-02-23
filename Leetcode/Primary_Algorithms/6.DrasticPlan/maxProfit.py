"""
买卖股票的最佳时机
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

import time
class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        if len(prices) <= 1:
            return 0
        maxProfit = 0
        minPrices = prices[0]
        for i in range(len(prices)):
            # 虽简洁但是耗时长，因为每次两种情况都要计算
            #minPrices = min(minPrices, prices[i])
            #maxProfit = max(prices[i] - minPrices, maxProfit)
            # if prices[i] < minPrices:
            #     minPrices = prices[i]
            # else:
            #     profit = prices[i] - minPrices
            #     if profit > maxProfit:
            #         maxProfit = profit
        return maxProfit

start = time.clock()
so = Solution()
print(so.maxProfit([7, 1, 5, 3, 6, 4]))
end = time.clock()
print('Runing Time: %s ms' % ((end - start) * 1000))

