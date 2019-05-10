"""
验证回文字符串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
示例 1:
输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:
输入: "race a car"
输出: false
"""


class Solution:
    # beat 31%
    # def isPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     注意此题的难点是有数字和符号的干扰
    #     way1: 去掉多余数字和符号
    #     """
    #     new_s = []
    #     for s1 in s:
    #         if 'a' <= s1.lower() <= 'z':
    #             new_s.append(s1.lower())
    #         if '0' <= s1 <= '9':
    #             new_s.append(s1)
    #     if len(new_s) == 0:
    #         return True
    #     if len(new_s) == 1:
    #         return True
    #     i = 0
    #     j = len(new_s) - 1
    #     while i < j:
    #         if new_s[i] != new_s[j]:
    #             return False
    #         i += 1
    #         j -= 1
    #     return True

    # beat 23.48 %
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        # 巧用 continue 把判断转移到外面的while循环，内循环可以不使用while
        while i < j and i < len(s) and j > 0:
            if not ('a' <= s[i].lower() <= 'z' or '0' <= s[i] <= '9'):
                i += 1
                continue
            if not ('a' <= s[j].lower() <= 'z' or '0' <= s[j] <= '9'):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True


so = Solution()
print(so.isPalindrome(',.'))

so = Solution()
print(so.isPalindrome('0P'))

so = Solution()
print(so.isPalindrome("race a car"))



