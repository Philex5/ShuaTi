"""
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。

字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

leetcode 1189
"""

import sys
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        思路： 统计需要的各个字母的个数，然后看text相应字母的个数，满足需要的最小的倍数则为答案
        :param text:
        :return:
        """
        if not text:
            return 0
        res = sys.maxsize
        count1 = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        count = {}
        for t in text:
            if t in count.keys():
                count[t] += 1
            else:
                count[t] = 1
        print(count1)
        print(count)
        for key in count1.keys():
            if key not in count.keys():
                return 0
            res = min(count[key] // count1[key], res)
        return res


so = Solution()
print(so.maxNumberOfBalloons(text="loonbalxballpoon"))










