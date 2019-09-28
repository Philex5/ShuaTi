import sys

def twoK(values, index, K, dup):
    cnt = 0
    low, high = 0, len(values) - 1
    while low < high:
        if values[low] + values[high] < K:
            if values[low] == values[low+1]:
                num = (high - low) - (dup[high+index] - dup[low+index]) + 1
            else:
                num = (high - low) - (dup[high+index] - dup[low+index])
            cnt += num
            while values[low] == values[low+1]:
                low += 1
            low += 1
        else:
            high -= 1
    return cnt

def dupNums(values):
    dup = [0] * len(values)
    for i in range(1, len(values)):
        if values[i] == values[i-1]:
            dup[i] = dup[i-1] + 1
        else:
            dup[i] = dup[i-1]
    return dup


def func():
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    K = int(sys.stdin.readline().strip())
    if len(values) < 3:
        return 0
    values.sort()
    dup = dupNums(values)
    cnt, i = 0, 0
    while i < len(values) - 2:
        cnt += twoK(values[i+1:], i+1, K-values[i], dup)
        while values[i] == values[i+1]:
            i += 1
        i += 1
    return cnt


if __name__ == "__main__":
    print(func())