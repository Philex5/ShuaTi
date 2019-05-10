"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
"""
import time
class Solution:
    # 暴力法 O(n^3)
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        sum = 0
        for i in range(1, len(nums)+1):
            j = 0
            k = 0
            while j < len(nums):
                 sum = max(sum, sum(nums[j: j+i]))
                 j = j + i
            while k < len(nums):








start = time.clock()
so = Solution()
print(so.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
end = time.clock()
print('Runing Time: %s ms' % ((end - start) * 1000))



