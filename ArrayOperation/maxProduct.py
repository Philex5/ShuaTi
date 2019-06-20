"""
乘积最大子序列
给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        maxProduct = nums[0]
        # 贪心算法不可取，乘上下一个不变大不代表乘上下下一个不变大
        # for i in range(0, len(nums)):
        #     j = i + 1
        #     init = nums[i]
        #     temp = init
        #     while temp >= init and j < len(nums):
        #         init = temp
        #         temp *= nums[j]
        #         j += 1
        #     maxProduct = max(maxProduct, max(init, temp))

        # brute method O(n^2) overtime!!!
        # for i in range(len(nums)):
        #     temp = nums[i]
        #     for j in range(i+1, len(nums)):
        #         temp *= nums[j]
        #         maxProduct = max(maxProduct, temp)

        # 动态规划
        # maxdp[i] = max(maxdp[i-1]*a[i] , a[i]]
        # 不对，可能最小值负的，能一下子变成最大值， 反之亦然
        # 所以
        # maxdp = [nums[0]] * len(nums)
        # mindp = [nums[0]] * len(nums)
        #
        # for i in range(1, len(nums)):
        #     maxdp[i] = max(mindp[i - 1] * nums[i], maxdp[i - 1] * nums[i], nums[i])
        #     mindp[i] = min(maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i], nums[i])
        #
        # return max(maxdp)
        #return maxProduct

        reverse = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            reverse[i] *= reverse[i - 1] or 1
        print(nums)
        print(reverse)
        return max(nums + reverse)


so = Solution()
print(so.maxProduct([2, 3, -2, 4]))