import sys
for line in sys.stdin:
    n, k = list(map(int, line.split()))
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, line.split()))
    nums = sorted(nums)
    start_number = 10e9 + 1
    end_number = 0
    count = 0
    for i in range(n):
        end_number = nums[i]
        if end_number != start_number and end_number != 0 and count < k:
            if count == 0:
                print(end_number)
                start_number = end_number
                count += 1
            else:
                print(end_number - start_number)
                start_number = end_number
                count += 1
    if count < k:
        for i in range(count, k):
            print(0)




