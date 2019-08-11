"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。
示例 1:

输入: n = 3, k = 3
输出: "213"
示例 2:

输入: n = 4, k = 9
输出: "2314"
"""

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
         """
         可以使用回溯法来做，套用模板
         需要求出所有解，超出时间限制
         """
         if n <= 0 or k < 0:
             return ""
         res = []
         def helper(i, temp):
             if len(temp) == n:
                 res.append(temp)
                 return
             for j in range(1, n+1):
                 if str(j) in temp:
                     continue
                 helper(j, temp + str(j))
         helper(0, '')
         print(res)
         return res[k-1]

    def getPermutation1(self, n: int, k: int) -> str:
        """
         123, 1为首字母，有23,32 ,2！
         第n个位置的数字，由 k // (n-1)! 决定
        """
        if n == 0:
            return ''
        res = ''
        nums = [str(i) for i in range(1, n+1)]
        """
        1 -> 0  '123'  0/2 =0
        2 -> 1  '132'  1/2 =0
        
        3 -> 2  '213' 2/2 = 1
        4 -> 3  '231' 3/2 = 1
        """
        # 从0开始编号，保证k除以同一组的数值相同
        k -= 1
        for i in range(n):
            t = math.factorial(n-i-1)
            # 第几个组
            loc = k // t
            res += nums[loc]
            print(t, loc)
            nums = nums[:loc] + nums[loc+1:]
            k %= t
        return res


so = Solution()
print(so.getPermutation1(3, 4))



