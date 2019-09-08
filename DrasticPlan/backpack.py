"""
0/1 背包问题
题目: 在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，
每个物品的大小为A[i].

"""
class Solution:
    def backPack(self, m, A):
        """
        思路：0/1背包问题，经典的动态规划

        :param m:
        :param A:
        :return:
        """
        if m == 0:
            return 0
        if not A:
            return 0
        dp = [0] * (m+1)
        # for a in A:
        #     dp[a] += 1
        # while 1:
        #     for a in A:
        #         # 不对，无法保证a只被使用1次，比如5在背包，m=10
        #         dp[m] = max(dp[m], dp[m-a])
        #     if dp[m] > 0:
        #         break
        #     m -= 1
        # return m

        dp[0] = 1
        for i in range(len(A)):
            for j in range(m, A[i]-1, -1):
                if dp[j - A[i]] == 1:
                    dp[j] = 1
        print(dp)
        for i in range(m, 0, -1):
            if dp[i] > 0:
                return i

so = Solution()
print(so.backPack(10, [3, 6, 5, 2]))