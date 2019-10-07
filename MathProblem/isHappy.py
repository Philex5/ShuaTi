"""
编写一个算法来判断一个数是不是“快乐数”。

一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例: 

输入: 19
输出: true
解释:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

leetcode 202
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        限定计算次数来判断是否能够得到1
        改进1： 使用字符串来计算每一位平方的和
        改进2： 快乐数是会循环的，计算的和如果出现过那么就不是快乐数
        :param n:
        :return:
        """
        # count = 0
        # while count < 50:
        #     if n == 1:
        #         return True
        #     next = 0
        #     while n > 0:
        #         m = n % 10
        #         n = n // 10
        #         next += m ** 2
        #     n = next
        #     count += 1
        # return False

        n = str(n)
        visited = set()
        while 1:
            n = str(sum(int(i) ** 2 for i in n))
            if n == '1':
                return True
            if n in visited:
                return False
            visited.add(n)


so = Solution()
print(so.isHappy(19))

