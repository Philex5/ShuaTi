import sys

def canBeTransformed(values):
    l = len(values)
    w = len(values[0])
    isTransform = True
    minutes = 0
    while isTransform:
        isTransform = False
        changes = 0
        temp = []
        for i in range(l):
            for j in range(w):
                if values[i][j] == 2:
                    temp.append([i, j])
        for num in temp:
            change = transform(values, l, w, num[0], num[1])
            changes += int(change)
        if changes > 0:
            minutes += 1
            isTransform = True
    for j in range(l):
        if 1 in values[j]:
            return -1
    return minutes


def transform(nums, l, w, i, j):
    flag = False
    if i - 1 >= 0 and nums[i-1][j] == 1:
        nums[i-1][j] = 2
        flag = True
    if i + 1 < l and nums[i+1][j] == 1:
        nums[i+1][j] = 2
        flag = True
    if j - 1 >= 0 and nums[i][j-1] == 1:
        nums[i][j-1] = 2
        flag = True
    if j + 1 < w and nums[i][j+1] == 1:
        nums[i][j+1] = 2
        flag = True
    return flag


if __name__ == '__main__':
    values = []
    while 1:
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        if not line:
            break
        value = list(map(int, line.split()))
        values.append(value)
    print(canBeTransformed(values))
