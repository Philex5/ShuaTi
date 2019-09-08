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
    # def permute(self, nums):
    #     """
    #     采用回溯法,使用list的remove函数,去掉当前num得到新的数组
    #     """
    #     n = len(nums)
    #     # if n <= 1:
    #     #     return nums
    #     res = []
    #     for i in range(n):
    #         temp = copy.copy(nums)
    #         temp.remove(nums[i])
    #         re = []
    #         re.append(nums[i])
    #         self.permuteNum(temp, res, re)
    #     return res
    #
    # def permuteNum(self, nums, res, re):
    #     n = len(nums)
    #     if n == 0:
    #         res.append(re)
    #         return
    #     temp = copy.copy(nums)
    #     while temp:
    #         a = random.choice(temp)
    #         temp.remove(a)
    #         recopy = copy.copy(re)
    #         numscopy = copy.copy(nums)
    #         numscopy.remove(a)
    #         recopy.append(a)
    #         self.permuteNum(numscopy, res, recopy)
    def permute(self, nums):
        """改进版本"""
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res

    # def permute(self, nums):
    #     """
    #     回溯法, 每轮都遍历全部,通过判断筛选解,效率低
    #     """
    #     if not nums or len(nums) == 0:
    #         return
    #     l = len(nums)
    #     res = []
    #
    #     def getPermute(i, temp):
    #         # 满足条件加入
    #         if len(temp) == l:
    #             if temp not in res:
    #                 res.append(temp)
    #             return
    #         for j in range(l):
    #             if nums[j] not in temp:
    #                 getPermute(j, temp + [nums[j]])
    #     for i in range(l):
    #         getPermute(i, [])
    #
    #     return res


so = Solution()
print(so.permute([1]))






