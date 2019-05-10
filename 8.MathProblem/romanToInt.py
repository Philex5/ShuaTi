"""
  罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:

输入: "III"
输出: 3
示例 2:

输入: "IV"
输出: 4
示例 3:

输入: "IX"
输出: 9
示例 4:

输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
示例 5:

输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
"""

class Solution:
    # beat 6.80%
    # 可以看做是为这些字母对应的数字来赋 +- 值
    # 而 +-由后一个数字确定，后一个数字比当前大，当前数字为-号，否则为+
    # 除此之外，把I当做一个整体对待
    # 其实从左到右应该是递减的，不符合的都赋 -
    # def romanToInt(self, s: str) -> int:
    #     romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     nums = []
    #     start = 0
    #     end = 0
    #     for i in range(len(s)):
    #         if s[i] == 'I':
    #             start = i
    #             end = i
    #             while end < len(s)-1 and s[end] == 'I':
    #                 end += 1
    #             break
    #     print(start, end)
    #     for i in range(len(s)):
    #         nums.append(romanMap[s[i]])
    #         if nums[i] > nums[i-1]:
    #             nums[i-1] = -nums[i-1]
    #     for i in range(start, end):
    #         nums[start] = nums[end-1]
    #     return int(sum(nums))
    # 其实从右到左应该是递增的，不符合的都赋 -
    # beat 22.35%
    def romanToInt(self, s: str) -> int:
        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        maxN = 0
        result = 0
        for i in range(len(s) - 1, -1, -1):
            current = romanMap[s[i]]
            result += current if current > maxN else -current
            maxN = max(current, maxN)
        return result


so = Solution()
print(so.romanToInt('IV'))