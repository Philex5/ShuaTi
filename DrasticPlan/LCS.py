"""
给出两个字符串，找到最长公共子序列(LCS)，返回LCS的长度。
"""
class Solution(object):
    def lcs(self, p, q):
        """
        LIS子序列的拓展
        dp[i][j] = ( dp[i][j-1], dp[i-1][j]  dp[i] != dp[j]
        dp[i][j] = (dp[i-1][j-1] + 1         dp[i] == dp[j]
        :param p: 字符串1
        :param q: 字符串2
        :return:
        """
        n = len(p)
        m = len(q)
        dp = [[0] * (n+1) for i in range(m+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if p[i-1] == q[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return dp[-1][-1]

so = Solution()
print(so.lcs('abcdefg', 'adeghlm'))





