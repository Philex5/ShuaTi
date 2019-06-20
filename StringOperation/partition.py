"""
  分割回文串
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

"""又蠢又蛮有麻烦"""
# class Solution:
#
#     def partition(self, s: str):
#
#         res = []
#         for i in range(0, len(s)):
#             a = s[:i]
#             b = s[i:]
#             if self.isPalindrome(a) and self.isPalindrome(b):
#                 if len(a) == 0:
#                     res.append([b])
#                 elif len(a) == 0:
#                     res.append([a])
#                 else:
#                     res.append([a, b])
#                 if len(a) > 1:
#                     res += self.partitionMore('', a, b)
#                 if len(b) > 1:
#                     res += self.partitionMore(a, b, '')
#         final_res = []
#         for re in res:
#             if re not in final_res:
#                 final_res.append(re)
#         return final_res
#
#     def partitionMore(self, before, s, after):
#         res = []
#         for i in range(1, len(s)):
#             a = s[:i]
#             b = s[i:]
#             if self.isPalindrome(a) and self.isPalindrome(b):
#                 if before:
#                     res.append([before] + [a, b])
#                 if after:
#                     res.append([a, b] + [after])
#                 if not after and not before:
#                     res.append([a, b])
#                 if len(a) > 1:
#                     if b:
#                         res += self.partitionMore('', a, b)
#                     else:
#                         res += self.partitionMore('', a, '')
#                 if len(b) > 1:
#                     if a:
#                         res += self.partitionMore(a, b, '')
#                     else:
#                         res += self.partitionMore('', b, '')
#         return res
#
#
#     def isPalindrome(self, s):
#         if len(s) <= 1:
#             return True
#         i = 0
#         j = len(s) - 1
#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True

class Solution:
    def partition(self, s: str):
        """
        因为要找出所有组合，所有需要递归
        最后的结果要把之前划分的部分全部统合起来，所以需要回溯
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        # end statu
        if not s:
            res.append(path)
        # way to expand
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                 # record it if the path to the end of s
                 self.dfs(s[i:], path+[s[:i]], res)

    def isPalindrome(self, s):
        """
         逆置与原来相同，则为回文
        """
        return s == s[::-1]


so = Solution()
print(so.partition("bb"))