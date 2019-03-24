class Solution:
    # 排序遍历
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(0, len(nums), 2):
            # 只剩最后一个了,直接返回
            if i + 1 >= len(nums):
                return nums[i]
            if nums[i+1] != nums[i]:
                return nums[i]

    def singleNumber1(self, nums):
        # 对于有多个不同的数字的情况
        nums = sorted(nums)
        uniques = []

        i = 0
        while i < len(nums):
            if i + 1 >= len(nums):
                uniques.append(nums[i])
                i += 1
            elif nums[i] == nums[i+1]:
                i += 2
            elif nums[i] != nums[i+1]:
                uniques.append(nums[i])
                i += 1
            else:
                print('sfl')

        return uniques

    # byte opoeration
    # 

    def singleNumber_high(self, nums):
        pass




so = Solution()
print(so.singleNumber1([1, 2, 2, 1, 5, 4, 3]))