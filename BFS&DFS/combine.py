class Solution(object):
    def combine(self, n, k):
        """
        回溯法的标准思路，从1开始，在依次向后选择一位，之后从2开始向后
        使用回溯法的模板
        半个月没写，依旧宝刀未老啊，啊哈哈哈
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(i, temp, l):
            if l == k:
                res.append(temp)
            for j in range(i + 1, n+1):
                helper(j, temp + [j], l + 1)
        helper(0, [], 0)
        return res
so = Solution()
print(so.combine(4, 2))