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

    def twoSumTwoHash(self, nums, target):
        """
        两趟遍历的hash需要处理可能是同一个
        """
        if not nums:
            return
        h = {}
        for i, n in enumerate(nums):
            h[n] = i
        for i, n in enumerate(nums):
            if target - n in h.keys() and i != h[target-n]:
                return [i, h[target-n]]

    def twoSumOneHash(self, nums, target):
        """
        两趟遍历的hash需要处理可能是同一个
        """
        if not nums:
            return
        h = {}
        for i, n in enumerate(nums):
            if target - n in h.keys():
                return [h[target-n], i]
            h[n] = i



so = Solution()
print(so.twoSum([2, 7, 11, 5], 9))
print(so.twoSumTwoHash([6, 4, 11, 3, 5], 8))
print(so.twoSumOneHash([6, 4, 11, 3, 5], 8))





