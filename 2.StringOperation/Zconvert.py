import math
class Solution:
    """
    我的思路，创建一个二维数组，把字符串按照规则填入其中
    分开讨论：m=2，应为n-1行和第0行都要填字符，而m>2则不用
    很差劲的方法
    """
    def convert0(self, s, numRows):
        if numRows == 1:
            return s
        l = len(s)
        m = numRows
        i = 0
        col = 0
        if m == 2:
            n = len(s)
            rows = [[''] * n for i in range(m)]
            while i < l:
                for j in range(m):
                    if i < l and i < 2:
                        rows[j][col] = s[i]
                        i += 1
                    if l > i >= 3:
                        rows[1][col] = s[i]
                        i += 1
                        break
                col += 1
                if i < l:
                    rows[0][col] = s[i]
                    i += 1
                    col += 1
        else:
            n = math.ceil(len(s) / (m + 1)) * (m - 1)
            rows = [[''] * n for i in range(m)]
            while i < l:
                for j in range(m):
                    if i < l:
                        rows[j][col] = s[i]
                        i += 1
                col += 1
                for k in range(m - 2, 0, -1):
                    if i < l:
                        rows[k][col] = s[i]
                        i += 1
                        col += 1
        # for i in range(m):
        #     print(rows[i])
        res = ''
        for i in range(m):
            for j in range(n):
                if rows[i][j] != '':
                    res += rows[i][j]
        return res


    """
    按行排序，只需要考虑行，不需要关心列
    """
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = len(s)
        rows = [''] * min(numRows, l)
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        res = ''
        for row in rows:
            res += row
        return res

    """
        按行访问
    """
    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        l = len(s)
        rows = [''] * min(numRows, l)
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1

        res = ''
        for row in rows:
            res += row
        return res

so = Solution()
print(so.convert2("ABCDE", 2))

