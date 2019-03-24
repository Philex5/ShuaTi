class Solution:
    # beat 97.28%
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        颠倒整数: 计算出每一位再依次颠倒
        """
        if x < -2 ** 31 or x > (2 ** 31 -1):
            return 0
        nums = []
        result = 0
        a = abs(x)
        while a > 0:
            nums.append(a % 10)
            a = a // 10
        print(nums)
        for i in range(len(nums)):
            result += nums[len(nums)-i-1] * (10 ** i)
        if x < 0:
            result = -1 * result
        if result < -2 ** 31 or result > (2 ** 31 -1):
            return 0
        return result

so = Solution()
print(so.reverse(-123))



