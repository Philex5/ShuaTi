"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
"""

class Solution:
    # 超出时间限制,还是得递归改成迭代
    # def climbStairs(self, n: 'int') -> 'int':
    #     if n == 1:
    #         return 1
    #     # 理清楚上一步走的，和接下来一步走的
    #     return self.plan(n, 1) + self.plan(n, 2)
    #
    # def plan(self, m, step):
    #     if m < 0:
    #         return 0
    #     if m == step:
    #         return 1
    #     if m < step:
    #         return 0
    #     return self.plan(m-step, 2) + self.plan(m-step, 1)

    # 竟然就是斐波那契数列，d(n) = d(n-1) + d(n-2)
    # beat 7.32
    # def climbStairs(self, n: 'int') -> 'int':
    #     if n == 1:
    #         return 1
    #     d = [0] * (n+1)
    #     d[1] = 1
    #     d[2] = 2
    #     for i in range(3, n+1):
    #         d[i] += d[i-1] + d[i-2]
    #     return d[n]
    #
     # 优化方案?
    def climbStairs(self, n: 'int') -> 'int':
        if n == 1:
            return 1
        a = 1
        b = 2
        for i in range(n-2):
            b += a
            a = b - a
        return b




so = Solution()
plans = so.climbStairs(38)
print(plans)