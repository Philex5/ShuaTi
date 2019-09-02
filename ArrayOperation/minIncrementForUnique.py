class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        暴力法：先排序，再从前到后一个一个比对
        """
        if not A:
            return 0
        A.sort()
        c = 0
        prev = A[0]
        for i in range(1, len(A)):
            if A[i] <= prev:
                # 相等时，位置递增，prev 表示应该在的位置
                prev += 1
                c += prev - A[i]
            else:
                # 比较大的数拔高了位置
                prev = A[i]
        return c


so = Solution()
print(so.minIncrementForUnique([3,2,1,2,1,7]))