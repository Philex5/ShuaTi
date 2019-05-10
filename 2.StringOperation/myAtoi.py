"""
实现 atoi，将字符串转为整数。
该函数首先根据需要丢弃任意多的空格字符，直到找到第一个非空格字符为止。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
若函数不能执行有效的转换，返回 0。
说明：
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (2^31 − 1) 或 INT_MIN (−2^31) 。
示例 1:
输入: "42"
输出: 42
示例 2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。

"""
import re
class Solution:
    # beat 67%
    # def myAtoi(self, str):
    #     """
    #     :type str: str
    #     :rtype: int
    #     难点在于怎么保证字符串先出现则报错,各种奇怪的情况会出现‘+-’‘-            235’
    #     小数点的情况让人奔溃!,解决方案:看错了,小数的话只用
    #     其实只要先去掉空格,提取符号位(注意只有符号位和多个符号位的情况),在遍历余下的字符提取出数字即可
    #
    #     """
    #     numset = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    #     op = {"-", "+"}
    #     if str=='' or str.isspace():
    #         return 0
    #     ms = str.lstrip()
    #     low = 0
    #     res = 0
    #     while low < len(ms) and ms[low] in op:  # 判断符号位是否正确
    #         low += 1
    #     if low > 1 or low == len(ms):   # 只有一个符号位或者多个符号位
    #         return 0
    #
    #     while low < len(ms):
    #         if ms[low] in numset:
    #             res = res * 10 + int(ms[low])
    #         else:
    #             break
    #         low += 1
    #
    #     if ms[0] == '-':
    #         return max(-res, -0x80000000)
    #     return min(res, 0x7FFFFFFF)

    # beat 89.9%, 正则大法好
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        res = ' '
        tmp = re.findall('^[-+]?\d+', str.strip())  # 正则判断，非法字符串返回空，返回的必是带有一个+/-或无符号的数字串
        if tmp:
            ms = tmp[0]
            if ms[0] == "-" or ms[0] == '+':
                res = ms[1:]
            else:
                res =ms
            res = int(res)
            if ms[0] == "-":
                return max(-res, -0x80000000)
            return min(res, 0x7FFFFFFF)
        else:
            return 0

so = Solution()
print(so.myAtoi("3.1556"))


