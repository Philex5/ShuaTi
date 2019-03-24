"""
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
"""
class Solution:
    # beat 81.17%
    # def merge(self, nums1, m, nums2, n):
    #     """
    #     :type nums1: List[int]
    #     :type m: int
    #     :type nums2: List[int]
    #     :type n: int
    #     :rtype: void Do not return anything, modify nums1 in-place instead.
    #     遍历nums2, 逐个插入nums1,优化方案： 1.遍历到大于nums1最大值之后，剩余nums2元素直接插入nums1
    #     2. 下次遍历在上一个元素插入的位置之后，减少遍历次数
    #     不适用于无序数组
    #     """
    #     start = 0
    #     if m == 0:
    #         for i in range(n):
    #             nums1[i] = nums2[i]
    #         return
    #     for i in range(n):
    #         if nums2[i] >= nums1[m - 1]:
    #             nums1[m:] = nums2[i:]
    #             break
    #         for j in range(start, m):
    #             if nums2[i] < nums1[j]:
    #                 for k in range(m, j, -1):
    #                     nums1[k] = nums1[k-1]
    #                 nums1[j] = nums2[i]
    #                 m += 1
    #                 start = j
    #                 break
    #             if nums1[j] <= nums2[i] < nums1[j+1]:
    #                 for k in range(m, j+1, -1):
    #                     nums1[k] = nums1[k-1]
    #                 nums1[j+1] = nums2[i]
    #                 m += 1
    #                 start = j + 1
    #                 break
    #     print(nums1)

    # only beat 6.47%
    # def merge(self, nums1, m, nums2, n):
    #     # 利用一个额外数组，使用双指针法,对两个数组进行排序，排序完赋值给nums1
    #     l = m + n
    #     nums = [0] * l
    #     i = 0
    #     j = 0
    #     k = 0
    #     while i < m and j < n:
    #         if nums1[i] < nums2[j]:
    #             nums[k] = nums1[i]
    #             k += 1
    #             i += 1
    #         else:
    #             nums[k] = nums2[j]
    #             k += 1
    #             j += 1
    #     while i < m :
    #         nums[k] = nums1[i]
    #         k += 1
    #         i += 1
    #     while j < n:
    #         nums[k] = nums2[j]
    #         k += 1
    #         j += 1
    #     for i in range(l):
    #         nums1[i] = nums[i]
    #     print(nums1)
    # 在nums1中操作，从尾部开始，插入取nums1和nums2中最大值放入其中
    # only beat 6.47,和method2一样，遍历次数较多
    def merge(self, nums1, m, nums2, n):
        l = m + n
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[l-1] = nums1[m-1]
                m -= 1
                l -= 1
            else:
                nums1[l - 1] = nums2[n - 1]
                n -= 1
                l -= 1
        while n > 0:
            nums1[l-1] = nums2[n-1]
            l -= 1
            n -= 1
        print(nums1)


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

so = Solution()
so.merge(nums1, m, nums2, n)