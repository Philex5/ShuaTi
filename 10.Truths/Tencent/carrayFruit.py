import sys


def carried(neg, pos):
    if abs(neg) > abs(pos):
        neg = neg + pos
        pos = 0
    elif abs(neg) < abs(pos):
        pos = pos - abs(neg)
        neg = 0
    else:
        neg = 0
        pos = 0
    return neg, pos


if __name__ == "__main__":
    # 读取第一行的n
    while 1:
        n = int(sys.stdin.readline().strip())
        ans = 0
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        cost = 0










