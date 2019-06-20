import sys
import math


def calcDist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


for line in sys.stdin:
    a = line.split()
    values = list(map(int, line.split()))
    n = len(values)
    points = []
    pointNum = n // 2
    for i in range(pointNum):
        points.append([values[i * 2], values[i * 2 + 1]])
    dists = [[0] * pointNum for i in range(pointNum)]
    for i in range(pointNum):
        for j in range(pointNum):
            dists[i][j] = calcDist(points[i], points[j])

    ans = []
    # 选择起点
    for i in range(pointNum):
        #print('Start: ', i)
        visited = [False] * pointNum
        visited[i] = True
        currentDist = calcDist(points[i], [0, 0])
        pointCount = 4
        pos = i  # 当前节点
        while pointCount > 0:
            candidates = []
            for k in range(5):
                if not visited[k]:
                    candidates.append(k)
            if len(candidates) == 1:
                minDist = calcDist(points[pos], points[candidates[0]]) + calcDist(points[candidates[0]], [0, 0])
                currentDist += minDist
                #print(minDist)
                pointCount -= 1
                #print('to: ', candidates[0])
                #print('to End', )
                break
            minDist = calcDist(points[pos], points[candidates[0]])
            now = candidates[0]
            for candi in candidates:
                curDist = calcDist(points[pos], points[candi])
                if curDist < minDist:
                    minDist = curDist
                    now = candi
            visited[now] = True
            #print('to: ', now)
            #print(minDist)
            currentDist += minDist
            pointCount -= 1
            pos = now
        #print(currentDist)
        ans.append(int(currentDist))
    print(min(ans))



