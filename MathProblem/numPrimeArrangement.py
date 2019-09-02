class Solution(object):
    def numPrimeArrangements(self, n):
        """
        思路：质数放在质数索引上，所以假设质数由a个，根据排序组合方案为A^a^a=a!
              非质数为b个，也可以带顺序的排列组合
        :type n: int
        :rtype: int
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        a = self.countNotPrime(n)
        print(a)
        b = n - a
        res = self.factorial(a) * self.factorial(b)

        return res % (10**9+7) if res > 10**9 else res


    def countNotPrime(self, n):
        """
        统计不是质数的个数
        :param n:
        :return:
        """
        if n <= 1:
            return 0
        # 1不是质数
        c = 1
        for i in range(2, n+1):
            for j in range(2, i//2+1):
                if i % j == 0 and i != j:
                    c += 1
                    break
        return c

    def factorial(self, a):
        res = 1
        for i in range(1, a+1):
            res *= i
        return res

so = Solution()
print(so.numPrimeArrangements(5))
