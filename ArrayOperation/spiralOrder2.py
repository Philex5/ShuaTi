# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 下午2:40
# @Author  : Philex
# @File    : spiralOrder2.py
# @Software: PyCharm

"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

class Solution:
    def generateMatrix(self, n):
        """
        参考螺旋矩阵的思路,顺时针访问矩阵,再将数字(1 ~ n^2)进行填充
        """
        if n == 0:
            return []

        matrix = [[0] * n for i in range(n)]
        x1 = y1 = 0
        x2 = n - 1
        y2 = n - 1
        self.cur = 1

        def fill(x1, y1, x2, y2):
            print(f'{x1},{y1} -> {x2},{y2}')
            if x1 == x2:
                for i in range(y1, y2 + 1):
                    matrix[x1][i] = self.cur
                    self.cur += 1
                return
            if y1 == y2:
                for j in range(x1, x2+1):
                    matrix[j][y1] = self.cur
                    self.cur += 1
                return
            for i in range(y1, y2+1):
                matrix[x1][i] = self.cur
                self.cur += 1
            for j in range(x1+1, x2):
                matrix[j][y2] = self.cur
                self.cur += 1
            for k in range(y2, y1-1, -1):
                matrix[x2][k] = self.cur
                self.cur += 1
            for l in range(x2-1, x1, -1):
                matrix[l][y1] = self.cur
                self.cur += 1

        while x1 <= x2 and y1 <= y2:
            fill(x1, y1, x2, y2)
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return matrix

so =Solution()
print(so.generateMatrix(0))