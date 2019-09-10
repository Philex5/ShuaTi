"""
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:

    def subsets(self, nums):
        """
        思路: 回溯法,使用模板,先排序,从前到后, 先选取初始元素,之后 求以该初始元素索引为起点的子数组的子集
        """
        if nums is None or len(nums) == 0:
            return
        res = []
        l = len(nums)
        nums = sorted(nums)
        def getSubsets(i, temp_res):
            if len(temp_res) > l:
                return
            res.append(temp_res)
            for j in range(i, l):
                # i为下一个索引，结果加入当前索引的值完美消除外部循环
                getSubsets(j+1, temp_res + [nums[j]])
        getSubsets(0, [])
        return res
    # def subsets(self, nums):
    #     """ 思路:位运算：如 [1,2,3]中[1,0,0]表示[1]"""
    #     l = len(nums)
    #     res = []
    #     for i in range(2**l):
    #         tmp = []
    #         for j in range(l):
    #             if i & (1 << j):
    #                 tmp.append(nums[l-1-j])
    #         res.append(tmp)
    #     return res


so = Solution()
print(so.subsets([1, 2, 3]))
