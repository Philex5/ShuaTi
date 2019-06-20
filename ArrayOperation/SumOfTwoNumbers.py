class Solution:
    # beat 35.8%
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        寻找数组中和为target的两个数
        先求差,在到数组里找这个差值
        """
        for i in range(len(nums)):
            least = target - nums[i]
            if least in nums:
                if nums.index(least) != i:
                    return [i, nums.index(least)]

so = Solution()
print(so.twoSum([2, 7, 11, 5], 9))





