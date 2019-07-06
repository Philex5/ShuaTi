# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 下午5:50
# @Author  : Philex
# @File    : mergeSection.py
# @Software: PyCharm
"""
leetcode 56: 合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


class Solution:
    def merge(self, intervals):
        """
        思路,先根据第一个元素排序,然后遍历,相邻两个区间判断是否可以合并
        时间复杂度: 除去排序的开销,一次遍历O(n)
        """
        if intervals is None or len(intervals) == 0:
            return []
        intervals = sorted(intervals)
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0],
                                max(intervals[i][1], intervals[i+1][1])]
                intervals.remove(intervals[i+1])
            else:
                i += 1
        return intervals


so = Solution()
print(so.merge([[1, 4], [4, 5]]))



