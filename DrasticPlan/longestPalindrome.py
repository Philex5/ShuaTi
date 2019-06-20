class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        中级的动态规划——二维关系
        时间复杂度 O(n^2)   空间复杂度O(n^2)

        """
        n = len(s)
        if n == 0:
            return s
        dp = [[0] * n for i in range(n)]
        left = 0
        right = 0
        for i in range(n-2, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i+1][j-1])
                if dp[i][j] and right - left < j-i:
                    left = i
                    right = j
        return s[left:right + 1]

    def longestPalindrome1(self, s: str) -> str:
        """
        中心扩展的方法
        时间复杂度 O(n^2) 空间复杂度O(1)
        """
        n = len(s)
        if n <= 1:
            return s
        for i in range(1, n-2):

            p1 = i







so = Solution()
print(so.longestPalindrome('babcd'))