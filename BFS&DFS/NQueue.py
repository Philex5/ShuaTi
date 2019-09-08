# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 下午9:51
# @Author  : Philex
# @File    : NQueue.py
# @Software: PyCharm

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
两个皇后不属于同一行,同一列或者同一条斜线上

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

"""


class Solution:
    def solveNQueens(self, n):
        """
        思路: 不同时将两个皇后放在同一行同一列或者同一条斜线上
        使用回溯法,一列一列的确定皇后的位置
        不对,只考虑到了与前一行的皇后同一条斜线的情况
        还可能与更远的皇后同一条斜线
        """
        res = []
        def setQueue(k, temp, visited):
            if k == n:
                res.append(temp)
                return
            for j in range(0, n):
                if not visited[j]:
                    if k > 0 and not hill_diagonals[j-k] and not dale_diagonals[j+k]:
                        visited[j] = True
                        hill_diagonals[j-k] = True
                        dale_diagonals[j+k] = True
                        setQueue(k+1, temp+[[k, j]], visited)
                        visited[j] = False
                        hill_diagonals[j-k] = False
                        dale_diagonals[j+k] = False
                    elif k == 0:
                        visited[j] = True
                        hill_diagonals[j-k] = True
                        dale_diagonals[j+k] = True
                        setQueue(k + 1, temp + [[k, j]], visited)
                        visited[j] = False
                        hill_diagonals[j-k] = False
                        dale_diagonals[j+k] = False

        hill_diagonals = [False] * (2 * n - 1)
        dale_diagonals = [False] * (2 * n - 1)
        setQueue(0, [], [False] * n)
        rets = []
        print(len(res))
        for i in range(len(res)):
            ret = []
            for j in range(len(res[i])):
                row, col = res[i][j]
                ret.append(col * '.' + 'Q' + (n-col-1) * '.')
            rets.append(ret)
        return rets


so = Solution()
print(so.solveNQueens(9))








