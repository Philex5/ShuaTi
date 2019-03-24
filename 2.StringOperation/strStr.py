class Solution(object):
    # beat 25.18%
    # def strStr(self, haystack, needle):
    #     """
    #     :type haystack: str
    #     :type needle: str
    #     :rtype: int
    #     直接遍历haystack，从与needle第一个字符匹配的位置，开始逐个比对之后的字符
    #     """
    #     if needle == ' 'or needle == '':
    #         return 0
    #     if len(haystack) < len(needle):
    #         return -1
    #     for i in range(len(haystack)):
    #         if len(haystack) - i + 1 < len(needle):
    #             return -1
    #         if haystack[i] == needle[0]:
    #             j = 1
    #             while j < len(needle) and i + j < len(haystack) and haystack[i+j] == needle[j]:
    #                 j += 1
    #             if j == len(needle):
    #                 return i
    #     return -1
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        KMP算法，之后实现
        """





so = Solution()
print(so.strStr("mississippi", "a"))