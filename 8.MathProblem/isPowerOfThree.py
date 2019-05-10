"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
"""
import math, sys
class Solution:
    # 递归
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n == 1:
    #         return True
    #     if n < 3:
    #         return False
    #     return self.calc(n/3)
    # 循环
    # def isPowerOfThree(self, n: int) -> bool:
    #     if n == 1:
    #         return True
    #     while n % 3 == 0:
    #         n /= 3
    #     return n == 1

    # 不用递归和循环
    # beat 48.24
    def isPowerOfThree(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # re = math.log(n) / math.log(3)# log精度问题，243 得到4.99999
        # return re == int(re)
        if n <= 0:
            return False
        # int最大值
        maxint = sys.maxsize
        # 3的最大幂次
        k = int(math.log(maxint) / math.log(3))
        max3 = 3 ** k
        # 判断能否被3的最大次幂整除即可
        return (max3 % n) == 0


so = Solution()
print(so.isPowerOfThree(243))
