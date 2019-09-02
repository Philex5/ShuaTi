class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        问题：替换指定数量字母能否构成回文串
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        res = []
        for query in queries:
            left, right, k =query
            q = s[left: right+1]
            # 不能全A,没有考虑重新排列的情况
            q_rev = q[::-1]
            needs = 0
            for i in range(len(q)//2):
                if q[i] != q_rev[i]:
                    needs += 1
            print(q, q_rev, needs, k)
            if needs <= k:
                res.append(True)
            else:
                res.append(False)
        return res

so = Solution()
print(so.canMakePaliQueries("hunu",
[[1,1,1],[2,3,0],[3,3,1],[0,3,2],[1,3,3],[2,3,1],[3,3,1],[0,3,0],[1,1,1],[2,3,0],[3,3,1],[0,3,1],[1,1,1]]))