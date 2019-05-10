class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if k > l:
            k = k % len(nums)
        if k == 0:
            print(nums)
            return
        rotate1 = nums[:-k]
        rotate2 = nums[-k:]
        nums[:k] =rotate2
        nums[k:] = rotate1
        print(nums)

so = Solution()
so.rotate([-1], 2)

