import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    times, nums = [], []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        value = list(map(int, line.split()))
        times.append(value[0])
        nums.append(value[1])

    rest = nums[0]
    temp = rest
    need = times[0] + rest
    for i in range(1, n):
        if rest > (times[i] - times[i-1]):
            rest = rest - (times[i] - times[i-1]) + nums[i]
        else:
            rest = nums[i]
        if temp < rest:
            temp = rest
        need = times[i] + rest
    print(need, temp)



