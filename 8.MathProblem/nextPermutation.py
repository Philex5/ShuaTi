"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须原地修改，只允许使用额外常数空间。

以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        只有在逆序的时候没有下一个排列的，所以从后往前遍历，找到第一个非逆序的数，然后用它之后的比它大
        的最小的数，与它交换，之后把它以后的数逆转顺序即可(从小到大排序)
        """
        n = len(nums)
        i = n - 2
        while i >=0 and nums[i] > nums[i+1]:
                i -= 1
        print(i)
        if i >= 0:
            j = n - 1
            while j > i and nums[j] < nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = nums[i+1:][::-1]
        return nums


so = Solution()
print(so.nextPermutation([3, 2, 1]))
