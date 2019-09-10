import sys
class compare(str):
    def __lt__(a, b):
        return a + b > b + a


for line in sys.stdin:
    nums = list(map(int, line.strip().split(',')))
    nums = [str(num) for num in nums]
    sorted_nums = sorted(nums, key=compare)
    value = ''.join(sorted_nums)
    if value[0] == '0':
        print('0')
    else:
        print(value)

