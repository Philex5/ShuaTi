"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""

# beat 94.99%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        巧用列表生成器，得到最短字符长度，再从头开始比较各个字符相同位置的字符是否相等，每一次比较都生成一个
        结果列表，ａｌｌ操作判断是否相同
        """
        if strs == [] or strs == ['']or strs == [' ']:
            return ""
        if len(strs) == 1:
            return strs[0]
        minlen = min([len(strs[i]) for i in range(len(strs))])
        count = 0
        for i in range(minlen):
            a = [strs[k][i] == strs[0][i] for k in range(1, len(strs))]
            if not all(a):
                break
            count += 1
        if count == 0:
            return ""
        return strs[0][:count]

so = Solution()
print(so.longestCommonPrefix(["aca", "cba"]))
