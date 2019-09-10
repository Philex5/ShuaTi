"""
如果可以通过将 A 中的两个小写字母精确地交换位置 K 次得到与 B 相等的字符串，我们称字符串 A 和 B 的相似度为 K（K 为非负整数）。

给定两个字母异位词 A 和 B ，返回 A 和 B 的相似度 K 的最小值。

 

示例 1：

输入：A = "ab", B = "ba"
输出：1
示例 2：

输入：A = "abc", B = "bca"
输出：2
示例 3：

输入：A = "abac", B = "baca"
输出：2
示例 4：

输入：A = "aabc", B = "abca"
输出：2
 

提示：

1 <= A.length == B.length <= 20
A 和 B 只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母。
"""


class Node:
    def __init__(self, s, step):
        self.s = s
        self.step = step

from collections import deque
import copy
class Solution(object):
    def kSimilarity(self, A, B):
        """
        最短交换次数 类似于 最短路径
        这是一个bfs的问题, 每次改变A的一个字符, 和B进行比较,
        将改变后的A加入到候选队列中,直到所有出现A==B位置,得到此时的次数.
        :type A: str
        :type B: str
        :rtype: int
        """
        start = Node(A, 0)
        q = deque()
        vis = set(A)
        q.append(start)
        res = 0
        while len(q) > 0:
            str = q.popleft()
            if str.s == B:
                res = str.step
                break
            i = 0
            s = str.s
            while s[i] == B[i]:
                i += 1
            for j in range(i+1, len(B)):
                if s[j] != B[j] and s[j] == B[i]:
                    temp = copy.copy(s)
                    temp = self.swap(temp, i, j)
                    if temp not in vis:
                        q.append(Node(temp, str.step+1))
                        vis.add(temp)
        return res

    def swap(self, s, i, j):
        a, b = s[i], s[j]
        s = s[:i] + b + s[i+1:]
        s = s[:j] + a + s[j+1:]
        return s


so = Solution()
print(so.kSimilarity("abccaacceecdeea", "bcaacceeccdeaae"))

