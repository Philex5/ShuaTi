"""
给定n个不同的正整数，整数k（1<= k <= n）以及一个目标数字。
在这n个数里面找出K个数，使得这K个数的和等于目标数字，你需要找出所有满足要求的方案。
"""

class Solution:
    def ksum(self, nums, k, target):
        if not nums or k == 0:
            return []
        res = []
        nums = sorted(nums)
        def helper(i, temp, now):
            if len(temp) > k:
                return
            if len(temp) == k and now == target:
                res.append(temp)
            for j in range(i, len(nums)):
                helper(j+1, temp+[nums[j]], now+nums[j])
        helper(0, [], 0)
        return res

so = Solution()
print(so.ksum([1, 2, 5, 4, 7, 9, 6], 3, 12))

