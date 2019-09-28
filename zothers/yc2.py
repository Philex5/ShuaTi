import sys


def dfs(x, y):
    if x == N-1:
        C[y] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if x1 >= 0 and x1 < N and y1 >= 0 and y1 < M and G[x][y] > G[x1][y1]:
            if Vis[x1][y1] == 0:
                Vis[x1][y1] = 1
                dfs(x1, y1)
        if L[x][y] == -1 or (L[x][y] > L[x1][y1] and L[x1][y1] != - 1):
            L[x][y] = L[x1][y1]
        if R[x][y] == -1 or (R[x][y] > R[x1][y1] and R[x1][y1] != - 1):
            R[x][y] = R[x1][y1]


def cmp(a, b):
    if L[0][a] != L[0][b]:
        return L[0][a] < L[0][b]
    return R[0][a] > R[0][b]

def find_pos(lastpos, rpos):
    larpos = 0
    rem = rpos
    for i in range(rem, M):
        if L[0][City[i]] <= lastpos + 1:
            if R[0][City[i]] > larpos:
                larpos = R[0][City[i]]
                rpos = i
        else:
            break
    lastpos = larpos
    return lastpos


M, N = list(map(int, sys.stdin.readline().strip().split()))
values = []
for i in range(M):
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    value = list(map(int, line.split()))
    values.append(value)

maxsize = max(M, N)
G = [[0] * maxsize for i in range(maxsize)]
L = [[0] * maxsize for i in range(maxsize)]
R = [[0] * maxsize for i in range(maxsize)]
Vis = [[0] * maxsize for i in range(maxsize)]
C = [0] * maxsize
City = [0] * maxsize
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(M):
    for j in range(N):
        G[i][j] = values[i][j]

for j in range(M):
    L[N-1][j] = R[N-1][j] = j

for j in range(0, M):
    if not Vis[0][j]:
        Vis[0][j] = 1
        dfs(0, j)

cnt = 0
for y in range(0, M):
    if C[y] == 0:
        cnt += 1
if cnt:
    print(1)
    print(cnt)
else:
    print(0)
    for y in range(0, M):
        City[y] = y
    a = sorted(City[:M+1], key=cmp)
    cnt = 0
    pos = rpos = 0
    while pos != M-1:
        cnt += 1
        find_pos(pos, rpos)
    print(cnt)



