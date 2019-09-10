"""
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

"""
from collections import deque

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        思路：使用DFS/回溯法，找出可能的情况
        但有个问题，必须要找出所有的解，有点浪费时间了
        除此之外，还有问题：之前回溯法是判断完整解，而这里只有解的一部分(一个单词)
        直接遍历就好了，如果划分之后，能到数组最后表示可以拆分
        用 wordBreak2也不对
        “单个状态满足则为True” 不适合使用DFS
        这个问题其实就是相当于寻找路径是否存在
        起点为字符开始，中间结点为单词结尾，终点为字符的结尾
        所以应该使用BFS
        还是存在 超出时间限制的问题
        通过visited数据来避免重复遍历
        """
        if not s or not wordDict:
            return False
        deq = deque()
        n = len(s)
        visited = [False] * n
        deq.append(0)
        while len(deq):
            p = deq.popleft()
            if not visited[p]:
                for i in range(p+1, n+1):
                    if s[p: i] in wordDict:
                        deq.append(i)
                        if i == n:
                            return True
            visited[p] = True
        return False

so = Solution()
print(so.wordBreak("leetcode",
["leet","code"]))







