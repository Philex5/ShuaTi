import sys
for line in sys.stdin:
    nums = list(map(int, line.strip().split()))
    print(nums)
    steps = [sys.maxsize] * len(nums)
    steps[0] = 0
    for i in range(len(nums)):
        j = 1
        while j <= nums[i] and i + j < len(nums):
            steps[i+j] = min(steps[i+j], steps[i] + 1)
            j += 1
    res = -1 if steps[-1] == sys.maxsize else steps[-1]
    print(res)

