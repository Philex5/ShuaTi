class Solution:
    def removeDuplicates(self, nums):
        """
        我想的也是使用双指针法，为什么结果一直有问题???
        快指针记录遍历位置，慢指针记录不重复数字排放的位置，均在同一个数组中
        把重复数字的第一个放入
        第二种方案更加简洁限制也没那么多，只需比较是否相同，不同则加入。而不用移动很多步来跳过重复
        """
        if len(nums) <= 1:
            return len(nums)
        pos = 1
        # way1: 一直移动跳过重复的数字
        # while i < len(nums):
            # while i < len(nums) and nums[i] == nums[i-1]:
            #     i += 1
            # if i > len(nums) - 1:
            #     break
            # nums[pos] = nums[i]
            # pos += 1
            # i += 1
        # 比较pos与i位置的数，不同则加入
        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                nums[pos] = nums[i]
                pos += 1
        nums = nums[:pos]
        return len(nums), nums

so = Solution()
n, nums = so.removeDuplicates([1, 1, 2])
print(n, nums)


