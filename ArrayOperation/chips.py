"""

leetcode 5213 玩筹码
"""

from collections import Counter
class Solution:
    def minCostToMoveChips(self, chips):
        """
        思路：豁然开朗系列
        奇数位置的砝码移动到奇数位置是没有代价的，偶数位置的砝码移动到偶数位置是没有代价的。
        所以可以把所有奇数位置的砝码移动到位置一，所有偶数位置的砝码移动到位置二，再把其中数量少的
        位置的砝码全部移动到另一个位置即可。
        :param chips:
        :return:
        """
        if not chips:
            return 0
        oddCount = 0
        evenCount = 0
        for pos in chips:
            if pos % 2 == 0:
                evenCount += 1
            else:
                oddCount += 1
        return min(oddCount, evenCount)

so = Solution()
print(so.minCostToMoveChips([1, 2, 3]))


