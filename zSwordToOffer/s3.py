"""
剑指offer 3 数组中重复的数字

长度为n的数组里所有的数字在0~n-1之间，寻找其中重复的数字

"""

### 方案一,使用字典统计

def count1(nums):
    if not nums:
        return []
    res = []
    cnt = {}
    for num in nums:
        if num in cnt.keys():
            res.append(num)
        else:
            cnt[num] = 1
    return res

### 利用n个0~n-1范围内的数的特点
### 排序后，每个数字应该在它索引的位置，但有重复数字存在所以不可能


def count2(nums):
    if not nums:
        return []
    for i in range(len(nums)-1):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
    return []


### 思路3，不改变数组本身，使用二分思想，统计1-m, m-n之间的数组，大于一半说明重复数字在其中

def count3(nums):
    if not nums:
        return []
    l = 0
    r = len(nums)
    while l >= r:
        m = l + (r - l) // 2
        countl = countRange(l, m-1)
        if l == r:
            if countl > 1:
                return True
        if countl > (m-l + 1):
            l = m
        else:
            r = m-1


#print(count1([2, 3, 1, 0, 2, 5, 3]))
print(count2([2, 3, 1, 0, 2, 5, 3]))