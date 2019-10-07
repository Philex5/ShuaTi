"""
给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。

假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写时，chars 中的每个字母都只能用一次。

返回词汇表 words 中你掌握的所有单词的 长度之和。

leecode 1160
"""

from copy import copy
class Solution:
    def countCharacters(self, words, chars):
        """
        暴力法，检测每一个单词的每一个字母是否出现在chars中
        因为不能重复使用，出现过的字母要在chars中删除
        其他方法： ASCII表计数
        :param words:
        :param chars:
        :return:
        """
        if not chars or not words:
            return 0
        res = 0
        chars = list(chars)
        for word in words:
            word = list(word)
            temp = copy(chars)
            flag = True
            for w in word:
                if w not in temp:
                    flag = False
                    break
                temp.remove(w)
            res += len(word) if flag else 0
        return res

so = Solution()
print(so.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))

