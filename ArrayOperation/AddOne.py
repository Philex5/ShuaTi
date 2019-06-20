from collections import deque
"""
题目描述：
    给定一个非负整数组成的非空数组，在该数的基础上加一，返回一个新的数组。
    最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
    你可以假设除了整数 0 之外，这个整数不会以零开头。
    示例 1:
    输入: [1,2,3]
    输出: [1,2,4]
    解释: 输入数组表示数字 123。
    示例 2:
    输入: [4,3,2,1]
    输出: [4,3,2,2]
    解释: 输入数组表示数字 4321。
"""
class Solution:
    # debeat 32.7% test time 64ms
    def plusOne(self, digits):
        """
        思路: 先得到数组对应的10进制数,加上1,再转换为数组
        """
        num = 0
        l = len(digits)
        for i in range(l):
            num += digits[i] * (10 ** (l-i-1))
        print(num)

        num += 1
        result = []

        print(num)

        # 最高位进位的情况
        if num // (10 ** l) == 1:
            l += 1
        for i in range(l):
            result.append(num // (10 ** (l-i-1)))
            num = num % (10 ** (l-i-1))
        print(result)
        return result

    # debeat 63.7% test time: 52ms
    def plusOne1(self, digits):
        l = len(digits)
        i = l-1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            if i > 0:
                digits[i-1] += 1
            i = i-1
            if i == -1:
                d = deque(maxlen=l+1)
                for l in digits:
                    d.append(l)
                d.appendleft(1)
                return list(d)
        return digits

so = Solution()
print(so.plusOne1([1, 2, 3]))


