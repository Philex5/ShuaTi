import sys
for line in sys.stdin:
    n, m = list(map(int, line.strip().split()))
    p = [i for i in range(1, n+1)]
    out = 0
    index = 0
    res = []
    while len(p) > 1:
        out += 1
        index += 1
        if index > len(p):
            index = 1
        if out == m:
            out = 0
            res.append(p[index-1])
            p.pop(index-1)
            index -= 1
    res.append(p[-1])
    res = [str(i) for i in res]
    print(' '.join(res))




