"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution:
    def permuteUnique(self, nums):
        """移除num,对子集操作 思路, 通permute1,加入了一个筛选解的条件"""
        res = []
        def backtrack(nums, tmp):
            if not nums:
                if tmp not in res:
                    res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

so = Solution()
print(so.permuteUnique([1, 1, 2]))