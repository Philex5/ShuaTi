# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 下午9:59
# @Author  : Philex
# @File    : spiralOrder.py
# @Software: PyCharm
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""
class Solution:
    def spiralOrder(self, matrix):
        """
        """
        res = []
        n = len(matrix)
        m = len(matrix[0])
        x1 = y1 = 0
        x2 = n - 1
        y2 = m - 1

        def drawAround(x1, y1, x2, y2):
            print(f'{x1},{y1} -> {x2},{y2}')
            if x1 == x2:
                for i in range(y1, y2 + 1):
                    res.append(matrix[x1][i])
                return
            if y1 == y2:
                for j in range(x1, x2+1):
                    res.append(matrix[j][y1])
                return
            for i in range(y1, y2+1):
                res.append(matrix[x1][i])
            for j in range(x1+1, x2):
                res.append(matrix[j][y2])
            for k in range(y2, y1-1, -1):
                res.append(matrix[x2][k])
            for l in range(x2-1, x1, -1):
                res.append(matrix[l][y1])

        while x1 <= x2 and y1 <= y2:
            drawAround(x1, y1, x2, y2)
            x1 += 1
            y1 += 1
            x2 -= 1
            y2 -= 1
        return res

so = Solution()
print(so.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))


