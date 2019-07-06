"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−2^31, 2^31 − 1] 。
"""

from decimal import Decimal
import time


class Solution:
    # def myPow(self, x, n):
    #     """
    #     思路：暴力法，几次方就乘几次，复述的话再取倒数
    #     时间复杂度： O(n)
    #      超出时间限制
    #     """
    #     if x == 0:
    #         return 0
    #     if n == 0:
    #         return 1
    #     flag = 1 if n > 0 else 0
    #     res = x
    #     for i in range(abs(n)-1):
    #         res *= x
    #     return round(res, 5) if flag else round(1/res, 5)
    # def myPow(self, x, n):
    #     """
    #     直接使用递归没有意义， 可以使用递归实现快速幂，即 x^2n = x^n * x^n x^(2n + 1) = x^2n * x
    #     时间复杂度： O(logn)
    #     空间复杂度：Ｏ(logn),存储 x^(n/2)的结果计算O(longn)次
    #     """
    #     if x == 0:
    #         return 0
    #     if n == 0:
    #         return 1
    #     flag = 1 if n > 0 else 0
    #     res = self.fastPow(x, abs(n))
    #     return res if flag else 1/res
    #
    # def fastPow(self, x, n):
    #     if n == 0:
    #         return 1
    #     half = self.fastPow(x, n // 2)
    #     if n % 2 == 0:
    #         return half * half
    #     else:
    #         return half * half * x


    def myPow(self, x, n):
        """
        循环实现快速幂
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        flag = 1 if n > 0 else 0
        n = abs(n)
        res = 1
        curr = x
        while n:
            if n % 2 == 0:
                n = n // 2
                curr *= curr
            else:
                res *= curr
                n -= 1
        return res if flag else 1/res

    def myPow1(self, x, n):
        """
        位运算实现
        例如 n = 13，则 n 的二进制表示为 1101, 那么 m 的 13 次方可以拆解为:
        m^1101 = m^0001 * m^0100 * m^1000。
        """
        res = 1
        temp = x
        flag = True if n > 0 else False
        n = abs(n)
        while n != 0:
            if n & 1 == 1:
                res *= temp
            temp *= x
            n = n >> 1
        return res if flag else 1/res

so = Solution()
start = time.time()
print(so.myPow1(2, -2))
end = time.time()
print(end - start)
