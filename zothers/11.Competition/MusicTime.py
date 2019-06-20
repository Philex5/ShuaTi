class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        count, dic = 0, {}
        remainders = (t % 60 for t in time)

        for item in remainders:
            if item == 0 and item in dic:
                count += dic[item]
            elif item != 0 and 60 - item in dic:
                count += dic[60 - item]

            # 和为60倍数的值一个放在dic里，一个在外面判断，value值对应重复情况
            # 这样就避免了直接判断 30 in dic,次数会为两倍的问题
            if item not in dic:
                dic[item] = 1
            else:
                dic[item] += 1

        return count

so = Solution()
print(so.numPairsDivisibleBy60([30,20,150,100,40]))
