"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
"""
 if not candidates:
            return []
        if min(candidates) > target:
            return []
        candidates.sort()
        res = []

        def helper(candidates, target, temp_list):
            if target == 0:
                res.append(temp_list)
            if target < 0:
                return
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                helper(candidates[i:], target - candidates[i], temp_list + [candidates[i]])
        helper(candidates,target,[])
        return res
"""
class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return
        # 先排序，避免重复
        candidates.sort()
        res = []
        self.find(candidates, 0, 0, res, target, [])
        return res

    def find(self, nums, i, total, res, target, curr):
        if total > target:
            return
        if total == target:
            res.append(curr)
            return
        for j in range(i, len(nums)):
            if total + nums[j] > target:
                break
            self.find(nums, j, total+nums[j], res, target, curr+[nums[j]])

so = Solution()
print(so.combinationSum([2, 3, 5], 8))
