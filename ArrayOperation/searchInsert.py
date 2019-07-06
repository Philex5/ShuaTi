"""
Leetcode No.35 Easy
"""
class Solution:
    def searchInsert(self, nums, target):
        """
        对排序好的数组寻找插入位置，为了减小算法时间复杂度，很容易联想到二分查找
        """
        l = len(nums)
        if l <= 0:
            return 0
        left = 0
        right = l
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left

so = Solution()
print(so.searchInsert([1, 3, 5, 6], 7))

