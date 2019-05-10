# Utils

# 元素替换
def swap(a, b):
    swap = b
    b = a
    a = swap
    return a, b


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: ints
        """
        l = len(nums)
        a = 0
        b = 1
        unique = []
        unique.append(nums[a])
        while b < l:
            if nums[b] == nums[a]:
                b += 1
            else:
                unique.append(nums[b])
                a = b
                b += 1
        for i in range(len(unique)):
            nums[i] = unique[i]
        print(unique)
        return len(unique)


s= Solution()
s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])