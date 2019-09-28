"""
HiHoCoder 1338 A Game

"""
import sys
n = int(sys.stdin.readline().strip())
line = sys.stdin.readline().strip()
values = list(map(int, line.split()))
sums = [0] * (2*(n+1))
dp = [[0] * (n+1) for i in range(n+1)]
for i in range(1, n+1):
    sums[i] = sums[i-1] + values[i-1]
    dp[i][i] = values[i-1]

for i in range(1, n+1):
    for j in range(1, n-i+1):
        dp[j][i+j] = sums[i+j] - sums[j-1] - min(dp[j+1][i+j], dp[j][i+j-1])
print(dp[1][n])