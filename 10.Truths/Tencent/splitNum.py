import sys

def solution(num, times):
    if num == 1:
        return 1
    temp0 = []
    temp1 = []
    temp0.append(num)
    k = times
    while min(temp0) > 1 and k > 0:
        for t in temp0:
            temp1.append(t // 2)
            temp1.append(t - t // 2)
        temp0 = temp1
        temp1 = []
        k -= 1
    return times - k + max(temp0)


if __name__ == '__main__':
    for line in sys.stdin:
        num, times = list(map(int, line.split()))
        print(solution(num, times))







