"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    # def subsetsWithDup(self, nums):
    #     """
    #     思路一,改进自subset1, 增加一个判断是否重复的条件
    #     """
    #     if nums is None or len(nums) == 0:
    #         return
    #     res = [[]]
    #     l = len(nums)
    #     nums = sorted(nums)
    #     def getSubsets(i, temp_res):
    #         if len(temp_res) > l:
    #             return
    #         if temp_res not in res:
    #             res.append(temp_res)
    #         for j in range(i+1, l):
    #             getSubsets(j, temp_res + [nums[j]])
    #     for i in range(l):
    #         getSubsets(i, [nums[i]])
    #     return res


    def subsetsWithDup(self, nums):
        """
        解决重复的新思路
        """
        if not nums or len(nums) == 0:
            return
        res = []
        l = len(nums)
        nums = sorted(nums)
        def getSubset(i, temp):
            if len(temp) > l:
                return
            res.append(temp)
            for j in range(i, l):
                if j > i and nums[j] == nums[j-1]:
                    continue
                # + nums[j] 下一个操作的索引为j+1
                getSubset(j+1, temp + [nums[j]])
        getSubset(0, [])
        return res

so = Solution()
print(so.subsetsWithDup([1, 1, 2, 3]))