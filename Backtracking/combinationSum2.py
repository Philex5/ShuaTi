"""
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。

说明：
所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        if not candidates:
            return
        res = []
        candidates = sorted(candidates)
        l = len(candidates)
        def find(i, temp_sum, temp_res):
            if temp_sum == target:
                res.append(temp_res)
                return
            for j in range(i, l):
                if temp_sum + candidates[j] > target:
                    break
                # 避免重复
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                # 这样写,对于每次循环,之前的元素,candidates[j-1]没有对temp_sum施加影响
                # j+1 -> 就是组合总和问题的解答
                find(j+1, temp_sum + candidates[j], temp_res + [candidates[j]])
        find(0, 0, [])
        return res


so = Solution()
print(so.combinationSum2([2, 5, 2, 1, 2], 5))






