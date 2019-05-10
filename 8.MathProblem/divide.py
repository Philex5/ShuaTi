"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。
"""
class Solution:
    def divide(self, dividend, divisor):
        """
        使用位运算，二分思想
        位运算，只能在 “2”上做文章，要么是2^n,要么是对某个数乘或除2^n
        """
        # 符号判断
        pos = dividend > 0 and divisor > 0
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend > divisor:
            tmp, cnt = divisor, 1
            # 能除掉2^i个divisor
            # divided = temp *[\sum(2^i)] (i是递减的)
            while dividend >= tmp:
                cnt <<= 1
                tmp <<= 1
            dividend -= tmp >> 1
            res += cnt >> 1
        res = res if pos else -res
        return min(max(-(2**31), res), 2**31-1)




