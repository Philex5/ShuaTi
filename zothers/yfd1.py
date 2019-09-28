import sys
global res



if __name__ == "__main__":
    # 读取第一行的n
    n, m = list(map(int, sys.stdin.readline().strip().split()))
    ans = 0
    values = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        value = list(map(int, line.split()))
        values.append(value)
    x1, y1 = 0, 0
    x2 = n - 1
    y2 = m - 1
    res = []

    def drawAround(x1, y1, x2, y2):
        if x1 == x2:
            for i in range(y1, y2 + 1):
                res.append(values[x1][i])
            return
        if y1 == y2:
            for j in range(x1, x2+1):
                res.append(values[j][y1])
            return
        for i in range(x1, x2+1):
            res.append(values[i][y1])
        for j in range(y1+1, y2):
            res.append(values[x2][j])
        for k in range(x2, x1-1, -1):
            res.append(values[k][y2])
        for l in range(y2-1, y1, -1):
            res.append(values[x1][l])

    while x1 <= x2 and y1 <= y2:
        drawAround(x1, y1, x2, y2)
        x1 += 1
        y1 += 1
        x2 -= 1
        y2 -= 1

    s = ''
    for element in res:
        s += str(element)
        s += ' '
    print(s)



