import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    values = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        value = list(map(int, line.split()))
        values.append(value)
    ids = {}
    for value in values:
        if value[0] not in ids.keys():
            ids[value[0]] = 0
        if value[1] not in ids.keys():
            ids[value[1]] = 0

    ids_count = {}
    for value in values:
        ids[value[1]] += 1
        if value[0] in ids_count.keys():
            ids_count[value[0]] += 1
        else:
            ids_count[value[0]] = 1

    starts = []
    for key in ids.keys():
        if ids[key] == 0:
            starts.append(key)
    max_click = 0
    ans = 0
    for start in starts:
        count = ids_count[start]
        for value in values:
            if value[0] == start and value[1] in ids_count.keys():
                count += ids_count[value[1]]
        if count > max_click:
            max_click = count
            ans = start
        elif count == max_click:
            ans = start if start > ans else ans
    print(ans)
