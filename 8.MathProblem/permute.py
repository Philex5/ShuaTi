"""
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

import copy
import random
class Solution:
    def permute(self, nums):
        """
        采用回溯法,使用list的remove函数
        """
        n = len(nums)
        # if n <= 1:
        #     return nums
        res = []
        for i in range(n):
            temp = copy.copy(nums)
            temp.remove(nums[i])
            re = []
            re.append(nums[i])
            self.permuteNum(temp, res, re)
        return res

    def permuteNum(self, nums, res, re):
        n = len(nums)
        if n == 0:
            res.append(re)
            return
        temp = copy.copy(nums)
        while temp:
            a = random.choice(temp)
            temp.remove(a)
            recopy = copy.copy(re)
            numscopy = copy.copy(nums)
            numscopy.remove(a)
            recopy.append(a)
            self.permuteNum(numscopy, res, recopy)

so = Solution()
print(so.permute([1]))






