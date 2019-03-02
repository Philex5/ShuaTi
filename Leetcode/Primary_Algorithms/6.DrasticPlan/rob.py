"""
打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
"""


class Solution(object):

    # 基础版
    # beat 22.63%
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][0] 代表偷到第i家，并且不偷第i家的最大收益
        # dp[i][1] 代表偷到第i家，并且偷第i家的最大收益

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [[0] * 2 for i in range(n)]
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = dp[i-1][0] + nums[i]
        return max(dp[-1])
        # 太秀了，用一个一行两列的列表来表示不同状态(偷与不偷)的值，后一个元素的列表值由前一个与当前元素值
        # 来决定，完美解决了相邻之间状态不能一样的问题。

    # 进阶版
    # beat 98.90%
    # 更加简化，第三个以后的取值，就是当前值+两次之前的值与前一次的值的最大值
    def rob1(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

    # 高阶版,空间复杂度为O(1)
    def rob2(self, nums):
        last, now = 0, 0
        for num in nums:
            last, now = now, max(last+num, now)
        return now


so = Solution()
print(so.rob2([2, 4, 7, 9, 3, 1]))