# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 下午3:01
# @Author  : Philex
# @File    : lengthOfLastWord.py
# @Software: PyCharm
"""
给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指由字母组成，但不包含任何空格的字符串。

示例:

输入: "Hello World"
输出: 5
"""


class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     """
    #     思路一: 直接调用库函数分割出各个单词
    #     """
    #     words = s.split()
    #     if not words:
    #         return 0
    #     return len(words[-1])

    def lengthOfLastWord(self, s):
        """
        思路二: 找最后一个空格,纪录空格只有的单词,对于最后有多个连续空格的情况难以操作
        从前往后的思维方式 --> 从后往前的思维方式
        先找最后一个单词的最后一个字母,然后再找最后一个单词的第一个字母
        """
        # if not s:
        #     return 0
        # i = 0
        # res = ''
        # s = ' ' + s
        # while i < len(s):
        #     失败! 不能处理最后有连续多个空格的情况
        #     if s[i] == ' ' and i + 1 == len(s):
        #         break
        #     if s[i] == ' ' and i + 1 < len(s):
        #         res = ''
        #     else:
        #         res += s[i]
        #     i += 1
        # return len(res)
        if not s:
            return 0
        l = len(s)
        i = l - 1
        # 找到最后一个单词的最后一个字母
        while i > -1 and s[i] == ' ':
            i -= 1
        # s内元素都为空格
        if i == - 1:
            return 0
        # 在找最后一个单词的第一个字母
        j = i
        while j > - 1 and s[j] != ' ':
            j -= 1
        return i - j


so = Solution()
print(so.lengthOfLastWord('a  '))


