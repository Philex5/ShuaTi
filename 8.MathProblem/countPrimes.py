"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

"""
class Solution:
    # 时间复杂度太高了，笨法子
    # def countPrimes(self, n: int) -> int:
    #     if n <= 1:
    #         return 0
    #     count = 0
    #     for i in range(2, n):
    #         if self.isPrime(i):
    #             count += 1
    #     return count
    #
    # def isPrime(self, n):
    #     for i in range(2, n):
    #         if n % i == 0:
    #             return False
    #     return True
    # beat 2.97%
    def countPrimes(self, n: int) -> int:
        count = 0
        flags = [True] * n
        for i in range(2, n):
            if flags[i]:
                count += 1
            j = 1
            while i * j < n:
                flags[i * j] = False
                j += 1
        return count

so = Solution()
print(so.countPrimes(3))

