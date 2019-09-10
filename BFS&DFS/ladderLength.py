"""
单词接龙
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

"""

from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        本质上也是在找路径，所以可以使用BFS，把当前位置能到达的字典内的单词加入队列
        然后出队列向前走一步，即转换一次
        记录层次，可以把每次加入队列的元素设置成[value, level]的结构
        那怎么记录路径呢？
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        transforms = deque()
        transforms.append([beginWord, 1])
        while len(transforms) > 0:
            word, count = transforms.popleft()
            for w in wordList:
                if self.canTransform(w, word):
                    transforms.append([w, count+1])
                    if w == endWord:
                        return count + 1
                    wordList.remove(w)
        return 0

    def canTransform(self, word1, word2):
        c = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                c += 1
        return True if c == 1 else False

so = Solution()
print(so.ladderLength(beginWord="hit", endWord="cog",
                      wordList=["hot", "dot", "dog", "lot", "log", "cog"]))





