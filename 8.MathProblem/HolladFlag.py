
"""
荷兰问题，只要求大于指定数的在该数后边，小于指定数的在该数左边
递归起来，其实就是三向切分的快速排序

"""

def holladFlag(nums, num):
    if num not in nums:
        return nums
    lt = 0
    gi = 0
    rt = len(nums) - 1
    while gi <= rt:
        if nums[gi] < num :
            nums[gi], nums[lt] = nums[lt], nums[gi]
            gi += 1
            lt += 1
        elif nums[gi] > num:
            nums[gi], nums[rt] = nums[rt], nums[gi]
            rt -= 1
        else:
            gi += 1
    return nums

print(holladFlag([1,2, 1, 5, 4, 7, 2, 3, 9,1], 2))
