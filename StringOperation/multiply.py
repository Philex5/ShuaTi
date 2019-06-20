"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
"""


class Solution:
    def multiply(self, num1, num2):
        if num1 == ' ' or num2 == ' ' or not num1 or not num2:
            return
        n1 = len(num1)
        res = 0
        for i in range(n1-1, -1, -1):
            res += int(num1[i]) * int(num2) * 10 ** (n1-1 - i)
        return str(res)

so = Solution()
print(so.multiply("2", " "))






