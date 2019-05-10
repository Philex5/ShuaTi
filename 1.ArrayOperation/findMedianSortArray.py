class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        """
        很暴力的方法，把小数组加到大数组里面，之后再排序选择中间位置的数
        """
        m = len(nums1)
        n = len(nums2)
        if m >= n:
            for i in range(n):
                nums1.append(nums2[i])
            self.quickSort(nums1, 0, m + n - 1)
            print(nums1)
            half = (m + n) // 2
            if (m + n) % 2 == 0:
                print((nums1[half] + nums1[half - 1]) / 2)
            else:
                print(nums1[half])
        else:
            for i in range(m):
                nums2.append(nums1[i])
            self.quickSort(nums2, 0, m + n - 1)
            print(nums2)
            half = (m + n) // 2
            if (m + n) % 2 == 0:
                print((nums2[half] + nums2[half - 1]) / 2)
            else:
                print(nums2[half])


    def quickSort(self, nums, low, high):
        if low >= high:
            return
        left = low
        right = high
        key = nums[low]
        while left < right:
            if nums[right] >= key and right > left:
                right -= 1
            nums[left] = nums[right]
            if nums[left] < key and left < right:
                left += 1
            nums[right] = nums[left]
        nums[left] = key
        self.quickSort(nums, low, left-1)
        self.quickSort(nums, left+1, high)

so = Solution()
so.findMedianSortedArrays([1], [1])


