class Solution:
    def fourSum(self, nums, target):
        """
        思路： 参考3-sum，固定左右边界
        """
        lens = len(nums)
        if lens < 4:
            return []
        res = []
        nums = sorted(nums)
        for i in range(lens // 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(lens-1, 2, -1):
                if j < lens - 1 and nums[j] == nums[j+1]:
                    continue
                l = i + 1
                r = j - 1
                print(i, l, r, j)
                print(nums[i], nums[l], nums[r], nums[j])
                while l < r:
                    temp = nums[l] + nums[r] + nums[i] + nums[j]
                    if temp == target:
                        res.append([nums[i], nums[l], nums[r], nums[j]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif temp > target:
                        r -= 1
                    else:
                        l += 1
        return res


so = Solution()
print(so.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11))








