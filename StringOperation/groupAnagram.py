"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。
"""

class Solution:
    # def groupAnagrams(self, strs):
    #     """
    #     思路: 一个一个遍历原数组，并且与结果列表中的每一字母组合比较，
    #           如果不在结果列表中，则在结果列表中新增一个字母组合
    #           怎么比较：变为小写形式并排序之后比较是否相等
    #     时间复杂度：　Ｏ(n^2)
    #     空间复杂度： O(n)
    #     结果： 超出时间限制
    #     """
    #     res = []
    #     for anagram in strs:
    #         flag = False
    #         for re in res:
    #             if sorted(re[0].lower()) == sorted(anagram.lower()):
    #                 re.append(anagram)
    #                 flag = True
    #                 break
    #         if not flag:
    #             res += [[anagram]]
    #     return res

    def groupAnagrams(self, strs):
        """
        改进思路：
        维护一个字典： 排序后组合： 原始字符串合集
        """
        if  not strs or len(strs) == 0:
            return
        map = {}
        for anagram in strs:
            sortedAna = sorted(anagram.lower())
            chars = ''.join(sortedAna)
            if chars not in map.keys():
                map[chars] = [anagram]
            else:
                map[chars].append(anagram)
        return list(map.values())


so = Solution()
print(so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))





