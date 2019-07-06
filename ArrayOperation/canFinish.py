# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 下午9:22
# @Author  : Philex
# @File    : canFinish.py
# @Software: PyCharm
"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
"""


class Solution:
    # def subarraySum(self, nums, k):
    #     """
    #     思路:连续子数组的和为一确定值
    #     暴力法: 确定开始位置,向后遍历,累计从开始位置到当前位置的数字之和, 等于加入解集,大于终止,
    #            把当前开始位置下一个位置作为开始位置
    #     考虑的情况有点复杂,比如最后一个数字等于k,j=l不符合要求,不会进入while循环
    #     还是会少考虑一些情况
    #     直接简化,不用while,虽然会引入更多的计算
    #     时间复杂度为: O(n^2)
    #     空间复杂度为: O(1)
    #     超出时间限制
    #     """
    #     if not nums or len(nums) == 0:
    #         return 0
    #     l = len(nums)
    #     res = 0
    #     for i in range(l):
    #         sums = 0
    #         for j in range(i, l):
    #             sums += nums[j]
    #             res += sums == k
    #     return res

    def subarraySum(self, nums, k):
        """
        思路: cumulative纪录从第一个位置到数组其他位置的和, cumulative[j] - cumulative[i]表示第j个元素
        到第i个元素的和.
        然后通过双重循环计算所有 两个元素之间的累计和
        """
        if nums is None or len(nums) == 0:
            return 0
        l = len(nums)
        cumu = [0] * (l+1)
        res = 0
        for i in range(1, l+1):
            cumu[i] = cumu[i-1] + nums[i-1]
        for i in range(l):
            for j in range(i+1, l):
                res += cumu[j+1] - cumu[i] == k
        return res

    def subarraySum1(self, nums, k):
        """
        思路: 哈希表
        利用字典存储 sum-k 出现的次数, sum-k = n -> sum = k + n, n存在, k肯定也存在
        注意初始化0:1,保证结果能够累加
        """
        sum, res, cul = 0, 0, {}
        cul[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in cul:
                res += cul[sum-k]
            if sum not in cul:
                cul[sum] = 0
            cul[sum] += 1

        return res


so = Solution()
print(so.subarraySum1([1, 2, 3, 5], 3))

