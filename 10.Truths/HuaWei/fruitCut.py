import sys

def sameCut(points, i, j):
    x1 = points[i][0]
    y1 = points[i][1]
    x2 = points[j][0]
    y2 = points[j][1]
    if x1 == x2 or y1 == y2 or abs(y1-y2) == abs(x1 - x2):
        return True
    return False


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    points = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        points.append([values[0], values[1]])
    pointNum = len(points)
    visited = [False] * pointNum
    cuts = 0
    for i in range(pointNum):
        if visited[i]:
            continue
        visited[i] = True
        for j in range(pointNum):
            if visited[j]:
                continue
            if sameCut(points, i, j):
                visited[j] = True
        cuts += 1
    print(cuts)
