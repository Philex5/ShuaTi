from collections import deque
class Solution:
    # debeat 32.7% test time 64ms
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        l = len(digits)
        for i in range(l):
            num += digits[i] * (10 ** (l-i-1))
        print(num)

        num += 1
        result = []

        print(num)

        if num // (10 ** l) == 1:
            l += 1
        for i in range(l):
            result.append(num // (10 ** (l-i-1)))
            num = num % (10 ** (l-i-1))
        print(result)
        return result

    # debeat 63.7% test time: 52ms
    def plusOne1(self, digits):
        l = len(digits)
        i = l-1
        digits[i] += 1
        while digits[i] == 10:
            digits[i] = 0
            if i > 0:
                digits[i-1] += 1
            i = i-1
            if i == -1:
                d = deque(maxlen=l+1)
                for l in digits:
                    d.append(l)
                d.appendleft(1)
                return list(d)
        return digits

so = Solution()
print(so.plusOne1([1, 2, 3]))


