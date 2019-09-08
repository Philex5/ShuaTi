"""
给定一个n个正整数的数组, 找出最长的子序列,使得序列中每一个较小的数都能整除较大的数.
Input : arr[] = {10, 5, 3, 15, 20}
Output : 3
最长子序列: 10, 5, 20.
因为: 20能被整除10, 10能被5整除.
"""
class Solution:
    def largeSubset(self, nums):
        """
        先排序，很关键！！！
        子问题： 到当前位置的子序列长度为之前能整除当前值的最长序列的长度加一
        dp[j] = max(dp[i] + 1, dp[j]) if a[j] % a[j] == 0 j in [i+1, n]
        :param nums:
        :return:
        """
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        # 自己整除自己
        dp = [1] * n
        for j in range(1, n):
            for i in range(0, j):
                if nums[j] % nums[i] == 0:
                    dp[j] = max(dp[j], dp[i]+1)
        print(dp)
        return max(dp)

so = Solution()
print(so.largeSubset([10, 5, 3, 15, 20]))
