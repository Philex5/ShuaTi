class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        注意: 字符串是不可变的,不能直接使用反转数组的方法
        """
        length = len(s)
        new_s = ''
        for i in range(length):
            new_s += s[length - i -1]
        # new_s = s[::-1]
        print(new_s)
        return new_s


so = Solution()

so.reverseString('I am luffy !')

