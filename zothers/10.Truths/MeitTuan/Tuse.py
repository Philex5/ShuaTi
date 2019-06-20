# import sys
#
#
# def tuse(pointA, pointB, gridRowDict):
#     x1, y1 = pointA
#     x2, y2 = pointB
#     if x1 == x2:
#         start = y1 if y1 < y2 else y2
#         end = y1 + 1 if y1 > y2 else y2 + 1
#         if x1 not in gridRowDict.keys():
#             gridRowDict[x1] = [j for j in range(start, end)]
#         else:
#             for i in range(start, end):
#                 if i not in gridRowDict[x1]:
#                     gridRowDict[x1].append(i)
#         return
#     if y1 == y2:
#         start = x1 if x1 < x2 else x2
#         end = x1 + 1 if x1 > x2 else x2 + 1
#         for i in range(start, end):
#             if i not in gridRowDict.keys():
#                 gridRowDict[i] = [y1]
#             else:
#                 if i not in gridRowDict[i]:
#                     gridRowDict[i].append(y1)
#
#
# if __name__ == '__main__':
#     n = int(input())
#     points = []
#     for i in range(n):
#         points.append(list(map(int, sys.stdin.readline().strip('').split())))
#     gridDict = {}
#     for line in points:
#         pointA = [line[0], line[1]]
#         pointB = [line[2], line[3]]
#         tuse(pointA, pointB, gridDict)
#     tusePoints = 0
#     for key in gridDict.keys():
#         tusePoints += len(gridDict[key])
#     print(tusePoints)
import sys

def tuse(pointA, pointB, grid):

    x1, y1 = pointA
    x2, y2 = pointB
    # 同一行
    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1+1):
                grid[x1-1][i-1] = 1
        else:
            for i in range(y1, y2+1):
                grid[x1-1][i-1] = 1
    # 同一列
    if y1 == y2:
        if x1 > x2:
            for j in range(x2, x1+1):
                grid[j-1][y1-1] = 1
        else:
            for j in range(x1, x2+1):
                grid[j-1][y1-1] = 1


def tuDian(n, points):
    gridNum = max(max(points))
    grid = [[0]*gridNum for i in range(gridNum)]

    for line in points:
        pointA = [line[0], line[1]]
        pointB = [line[2], line[3]]
        tuse(pointA, pointB, grid)
    tusePoints = 0
    for i in range(gridNum):
        tusePoints += sum(grid[i])
    print(tusePoints)

if __name__ == '__main__':
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, sys.stdin.readline().strip('').split())))
    tuDian(n, points)
