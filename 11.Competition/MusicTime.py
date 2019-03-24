class Solution:
    def numPairsDivisibleBy60(self, time):
        l = len(time)
        if l < 2:
            return 0
        count = 0
        time = sorted(time)
        for i in range(l):
            for j in range(i+1, l):
                if (time[i] + time[j]) % 60 == 0:
                    count += 1
        return count


so = Solution()
print(so.numPairsDivisibleBy60([60, 60, 60]))
