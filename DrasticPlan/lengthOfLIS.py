"""
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        动态规划
        dp[i] = max(dp[i], dp[j] + 1) j < i and nums[j] < nums[i]
        注意dp[i]的值可能在j遍历[0,i]的时候发生了改变
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            dp[i] = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

so = Solution()
print(so.lengthOfLIS([5, 3, 4, 8, 6, 7]))

