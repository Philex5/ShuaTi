class Solution:
    def searchInsert(self, nums, target):
        l = len(nums)
        if l <= 0 :
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
                right = mid
        return left

so = Solution()
print(so.searchInsert([1, 3, 5, 6], 7))

