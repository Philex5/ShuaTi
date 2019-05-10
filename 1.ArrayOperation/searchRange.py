"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
"""

class Solution:
    def searchRange(self, nums, target):
        """
        二分查找的变形,从中心向两边扩散
        主要是边界问题很烦人,额，是我傻了，不用考虑，它至少会向两边扩散出去一位
        还有mid是索引，值是nums[mid]，别老把索引和值弄混淆
        """
        l = len(nums)
        if l <= 0 or target not in nums:
            return [-1, -1]
        left = 0
        right = l - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                j = mid
                i = mid
                while j < l and nums[j] == target:
                    j += 1
                while i > -1 and nums[i] == target:
                    i -= 1
                return [i+1, j-1]
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return [-1, -1]

so = Solution()
print(so.searchRange([1,2], 2))

