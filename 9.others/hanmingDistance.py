"""
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。
"""

class Solution(object):
    # 内置函数
    # beat 99.38
    # def hammingDistance(self, x, y):
    #     """
    #     :type x: int
    #     :type y: int
    #     :rtype: int
    #     """
    #     return bin(x ^ y).count('1')

    # 位操作
    # beat
    def hammingDistance(self, x, y):
        a = x ^ y
        count = 0
        for i in range(32):
            count += (a >> i) & 1
        return count


so = Solution()
print(so.hammingDistance(1, 4))


