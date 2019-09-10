"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        利用f[i]记录以i为起点的每个片段的终点j，并且片段要在在字典中，
        然后从0开始搜索，每次给当前片段加上空格，然后以当前片段的末尾作为
        下一次搜索的头部，避免不必要的搜索
        深度优先搜索的思想不是体现在字符搜索上，而是单词搜索上
        所以要先找出以各个位置字符为开始的单词通过记录最后的位置，来加块之后的搜索
        """
        if not s or not wordDict:
            return []
        n = len(s)
        f = [[] for i in range(n)]
        # 寻找以当前字符作为单词开始j作为单词结束的所有情况，并统计到f中
        # 遍历所有可能的(i,j)组合,是否在字典中
        # f[i] = j 表示 s[i:j]组成单词在字典中
        # 从后往前遍历，先确定后面位置的f[i]，如果f[i]为空，表示i之后的字符无法组成单词
        # 那么之后都不需要在遍历了，节省时间
        for i in range(n-1, -1, -1):
            for j in range(i+1, n+1):
                if s[i: j] in wordDict:
                    # 加上这个条件才可通过全部测试用用例，如果j之后没有单词，没必要去遍历它了
                    if j == n or len(f[j]) > 0:
                        f[i].append(j)
        print(f)
        return self.dfs(0, s, f, '', [])

    def dfs(self, p, s, f, now, res):
        """
        深度优先搜索，当前单词搜索完之后，从结束为止下一个字符开始搜索
        """
        if p == len(s):
            res.append(now)
            return
        if p > 0:    # 找到第一个单词划分
            now += " "
        # 遍历所有以p开头，以j结尾的划分进行dfs
        for i in range(0, len(f[p])):
            self.dfs(f[p][i], s, f, now + s[p: f[p][i]], res)
        return res


so = Solution()
print(so.wordBreak(s = "pineapplepenapple",
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]))