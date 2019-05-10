"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        很简单的遍历，为什么弄得这么复杂？
        就和3-sum一样先排序再双指针就好了，为什么考虑那么多？从大变小，比
        """
        n = len(nums)
        if n < 3:
            return None
        nums = sorted(nums)
        dist = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]
                if abs(target - threeSum) < abs(target - dist):
                    dist = threeSum
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    return target
        return dist

so = Solution()
print(so.threeSumClosest([1,2,4,8,16,32,64,128], 82))