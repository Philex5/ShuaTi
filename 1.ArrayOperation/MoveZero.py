class Solution:
    # % beat 80.3
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        把０集中在一块当做一个整体进行交换
        """
        j = 0
        i = 1
        while i < len(nums):
            while nums[j] != 0 and nums[i] != 0:
                j += 1
                i += 1
                if i > len(nums) - 1:
                    print(nums)
                    return
            if nums[j] == 0 and nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
                i += 1
                if i > len(nums) - 1:
                    print(nums)
                    return
            if nums[j] != 0 and nums[i] == 0:
                i += 1
                j += 1
                if i > len(nums) - 1:
                    print(nums)
                    return
            if nums[j] == 0 and nums[i] == 0:
                i += 1
                if i > len(nums) - 1:
                    print(nums)
                    return

        print(nums)


so = Solution()
so.moveZeroes([5, 1, 0, 3, 12])



