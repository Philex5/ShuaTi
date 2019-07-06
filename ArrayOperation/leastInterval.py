# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 下午5:20
# @Author  : Philex
# @File    : leastInterval.py
# @Software: PyCharm
"""
给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。

然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的最短时间。

示例 1：

输入: tasks = ["A","A","A","B","B","B"], n = 2
输出: 8
执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
注：

任务的总个数为 [1, 10000]。
n 的取值范围为 [0, 100]。
"""


class Solution:
    def leastInterval(self, tasks, n):
        """
        思路: 找出出现频率最高的任务号,以n为间隔,将其他任务号填充
        比如 "A A A B B C C", n=2
        A -> X -> X -> A -> X -> X -> A
        X填充什么并不关心
        公式为 maxFrenq * (1 + n) + maxFreqCount (可能有多个任务号出现频率最大)
        设总共有m个任务号, 公式结果为k, 数组长为l
        if n > m - 1: k > l , 结果为k
        eg. A A A B B  n = 2
        AB-AB-A
        if n = m - 1: k = l ,结果均可
        eg. A A A B B C
        ABCABCA
        if n < m - 1: k < l ,结果为l
        eg. A A A B B C C D
        A--A--A k = 7 l = 9
        存在解: ABCDABCA,这里我们只关心最终的时长,而不是最终解
        这是的时长为l,因为部分间隔m-1填充,最终长度和l相同
        """
        l = len(tasks)
        letters = [0] * 26
        for i in range(l):
            letters[ord(tasks[i])-65] += 1
        letters = sorted(letters, reverse=True)
        maxFreq = letters[0]
        maxFreqCount = 1
        i = 1
        while letters[i] == maxFreq and i < 26:
            maxFreqCount += 1
            i += 1
        return max((maxFreq -1) * (n + 1) + maxFreqCount, l)

so = Solution()
print(so.leastInterval(tasks=["A","A","A","B","B","B", "C", "C", "C", "D"], n=2))






