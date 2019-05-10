# s = "leetcode"
# 返回 0.
#
# s = "loveleetcode",
# 返回 2.

class Solution:
    # beat 2.79%
    # def firstUniqChar(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     遍历数组,检查不包含该字符的原始字符串的子字符串是否包含该数字,不包含则返回
    #     使用列表的切片功能提取子字符串,注意第一和最后一个字符, 还有字符串越界问题
    #     """
    #
    #     length = len(s)
    #     if length == 0:
    #         return -1
    #     if length == 1:
    #         return 0
    #     for i in range(len(s)):
    #         if i == length -1:
    #             if not s[i] in s[:-1]:
    #                 return i
    #         elif i == 0:
    #             if not s[i] in s[1:]:
    #                 return i
    #         else:
    #             if not s[i] in s[:i] + s[i+1:]:
    #                 return i
    #     return -1

    # beat 35.41
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        遍历数组统计个数,利用字典存储统计结果,No 字典具有无序性,无法保证输出的是第一个唯一字符
        """
        length = len(s)
        if length == 0:
            return -1
        if length == 1:
            return 0
        count = {}
        for a in s:
            if a not in count.keys():
                count[a] = 1
            else:
                count[a] += 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


    # beat 29.63%
    # def firstUniqChar(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     使用int数组作为简单的哈希表,26个字母对应26个位置
    #     """
    #     length = len(s)
    #     if length == 0:
    #         return -1
    #     if length == 1:
    #         return 0
    #     count = [0] * 26
    #     for a in s:
    #         count[ord(a)-97] += 1
    #     for i in range(len(s)):
    #         if count[ord(s[i])-97] == 1:
    #             return i
    #     return -1



s = "dddccdbba"
so = Solution()
print(so.firstUniqChar(s))



