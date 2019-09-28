import sys


def cal(arr, n, k):
    if n == 0:
        return 0
    h = [0] * n
    h[-1] = arr[-1]
    d = {n-1: n-1}
    for i in range(n-1)[::-1]:
        if h[i+1] <= 0:
            h[i] = h[i+1] + arr[i]
            d[i] = d[i+1]
        else:
            h[i] = arr[i]
            d[i] = i
    m = 0
    end = 0
    s = 0
    for i in range(n):
        while end < n and s+h[end] <= k:
            s += h[end]
            end = d[end]+1
        m = max(m, end -i)
        s -= arr[i] if end >i else 0
        end if end > i else i+1
    return m



n, m = list(map(int, sys.stdin.readline().strip().split()))

line = sys.stdin.readline().strip()
values = list(map(int, line.split()))

ans = cal(values, n, m)




