# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 下午8:06
# @Author  : Philex
# @File    : searchMatrix.py
# @Software: PyCharm
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

"""


class Solution:
    # def searchMatrix(self, matrix, target):
    #     """
    #      思路1: 从矩阵的左下角移动来寻找target,如果当前位置值与target相等则返回true,如果比target小,则往右移动,
    #      负责则往上移动
    #      时间复杂度 O(n+m)
    #      空间复杂度 O(1)
    #     """
    #     if not matrix:
    #         return False
    #     n = len(matrix)
    #     m = len(matrix[0])
    #     i = n - 1
    #     j = 0
    #     while  0 <= i <= n-1 and 0 <= j <= m-1:
    #         if matrix[i][j] == target:
    #             return True
    #         elif matrix[i][j] < target:
    #             j += 1
    #         else:
    #             i -= 1
    #     return False
    def searchMatrix(self, matrix, target):
        """
        思路2: 将矩阵转化为一维数组,使用二分查找
        注意将一维数组的位置转化为二维矩阵的坐标
        时间复杂度：　O(log(mn))
        空间复杂度： O(1)
        """
        if not matrix:
            return False
        n = len(matrix)
        m = len(matrix[0])
        right = n * m - 1
        left = 0
        while left <= right:
            mid = left + (right - left) // 2
            curr = matrix[mid // m][mid % m]
            print(curr)
            if curr == target:
                return True
            elif curr > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


so = Solution()
print(so.searchMatrix([
    [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]
], target=13))