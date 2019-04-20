"""
一个序列有N个数：A[1],A[2],…,A[N]，求出最长非降子序列的长度。
子序列不是子串，有序但不一定连续

eg. 5，3，4，8，6，7
output: 2, 4, 6, 7

from: http://www.hawstein.com/posts/dp-novice-to-advanced.html
"""

import numpy as np

def LIS(nums):
    # d[i] = max(1, d[j] + 1) j < i and A[j] <= A[i]
    # 时间复杂度 O(n^2),空间复杂度
    l = len(nums)
    if l == 0:
        return 0
    if l == 1:
        return 1
    d = [0] * l
    d[0] = 1
    for i in range(l):
        d[i] = 1
        for j in range(i):
            if nums[j] <= nums[i] and d[j]+1 > d[i]:
                d[i] = d[j] + 1
    return max(d)

print (LIS([5, 3, 4, 8, 6, 7]))


def LIS(nums):
    # d[i] = max(1, d[j] + 1) j < i and A[j] <= A[i]
    # 时间复杂度 O(n^2),空间复杂度
    l = len(nums)
    if l == 0:
        return 0
    if l == 1:
        return 1
    d = [0] * l
    d[0] = 1
    for i in range(l):
        d[i] = 1
        for j in range(i):
            if nums[j] <= nums[i] and d[j]+1 > d[i]:
                d[i] = d[j] + 1
    return max(d)

print (LIS([5, 3, 4, 8, 6, 7]))


"""
改进方案：用B记录每个长度的LIS中最小的最大值，如B[1] = 1，代表，长度为1的lIS中最大值为1
"""

# 在非递减序列上二分查找大于等于key的位置，如果都小于key，就返回最大索引加一
def upper_bound(nums, key):
    e = len(nums) - 1
    s = 0
    if key > nums[e]:
        return e + 1
    while s < e:
        mid = s + (e - s) // 2
        if nums[mid] > key:
            e = mid
        else:
            s = mid + 1
    return s




def LIS1(d):
    n = len(d)
    i = 0
    l = 1
    end = np.zeros([n+1, ])
    end[1] = d[0]
    for i in range(1, n):
        pos = upper_bound(end, d[i])
        end[pos] = d[i]
        if l < pos:
            l = pos

    return l