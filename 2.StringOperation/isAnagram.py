"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

"""

class Solution:
    # beat 55.05%
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        字母异位词，字母相同，位置不同，只需判断字母个数种类一致即可
        利用上题的做法，长度为26的数组来计数， 字符的accii码-'a'的accii码作为索引
        """
        count_s = self.count(s)
        count_t = self.count(t)
        for i in range(len(count_s)):
            if count_s[i] != count_t[i]:
                return False
        return True

    def count(self, strs):
        counts = [0] * 26
        for s in strs:
            counts[ord(s)-ord('a')] += 1
        return counts


so = Solution()
print(so.isAnagram(b'abc', 'cba'))





