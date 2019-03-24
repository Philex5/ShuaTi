"""
帕斯卡三角形
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution(object):

    # beat 9.58
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        #res = []
        # 一开始填充好，之后修改值
        # for i in range(1, numRows+1):
        #     row = [1] * i
        #     res.append(row)
        # print(res)
        # for i in range(1, numRows):
        #     for j in range(1, i):
        #         res[i][j] = res[i-1][j-1] + res[i-1][j]
        # return res
        # 一行一行计算填充
        res = [[1]]
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i):
                a = res[-1][j-1]
                b = res[-1][j]
                tmp.append(a + b)
            tmp.append(1)
            res.append(tmp)
        return res






so = Solution()
print(so.generate(5))

