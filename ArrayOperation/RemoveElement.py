class Solution:
    def removeElement(self, nums, val: int) -> int:
        # 防止指针溢出，倒序遍历删除，666
        l = len(nums)
        for i in range(l-1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

so = Solution()
a = [2, 3, 3, 2]
print(so.removeElement(a, 3))
print(a)
