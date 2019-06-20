"""
数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
"""


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        """
        K个最大的元素，不是第K个不同的元素
        开始的做法排除了重复的元素，是不符合题意的
        """
        # l = len(nums)
        # if l == 0 or l < k:
        #     return
        # if l == 1 and k == 1:
        #     return nums[0]
        # if l == 1 and k != 1:
        #     return
        # count = 1
        # i = 0
        # j = 1
        # nums = sorted(nums, reverse=True)
        # print(nums)
        # while j < l:
        #     if count == k:
        #         return nums[j]
        #     if nums[j] != nums[i]:
        #         count += 1
        #     i = j
        #     j += 1
        # return

        """很简单的真正解法"""
        # 有本事不调库函数啊？
        # l = len(nums)
        # if l == 0 or l < k:
        #     return
        # nums = sorted(nums, reverse=True)
        # return nums[k - 1]

        """快排的思路，取一个值，比它大的，和它相等的， 比它小分成三个数组，再在里面找， 秀~"""
        pivot = nums[0]
        samller = [num for num in nums if num < pivot]
        equal = [num for num in nums if num == pivot]
        greater = [num for num in nums if num > pivot]

        # 如果greater中数比K多那么在greater中找
        if len(greater) >= k:
            return self.findKthLargest(greater, k)
        # 又不比greater + equal数加起来多
        elif len(equal) >= k - len(greater):
            return equal[0]
        # 比greater + equal数加起来多
        else:
            return self.findKthLargest(samller, k - len(greater) - len(equal))







so = Solution()
print(so.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))