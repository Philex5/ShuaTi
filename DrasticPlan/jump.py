# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 下午7:41
# @Author  : Philex
# @File    : jump.py
# @Software: PyCharm
"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

输入: [2,3,1,1,4]
输出: true
解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
示例 2:

输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

"""


class Solution:
    # def canJump(self, nums):
    #     """
    #     思路1: 递归,在当前位置寻找能到达的所有位置,然后对所有能到达的位置继续执行这样的操作,
    #     直到存在一个跳跃路径能够到达数组最后
    #     时间复杂度
    #     结果: 超出时间限制
    #     """
    #     if not nums or len(nums) == 0:
    #         return False
    #     return self.reach(nums, 0)

    # def reach(self, nums, pos):
    #     # 当前位置能到到达的最远的位置
    #     l = len(nums)
    #     if pos >= l - 1:
    #         return l - 1
    #     if nums[pos] == 0:
    #         return pos
    #     return max([self.reach(nums, pos+dis)for dis in range(1, nums[pos]+1)])

    # def reach(self, nums, pos):
    #     """
    #     改进写法,已找到可行的路径就返回,不用考虑所有的路径
    #     仍然超出时间限制
    #     """
    #     l = len(nums)
    #     if pos == l - 1:
    #         return True
    #     furthestJump = min(pos + nums[pos], l - 1)
    #
    #     # for nextPos in range(pos+1, furthestJump+1):
    #     # 优化: 从后往前需要遍历次数更少,直觉上，就是我们每次选择最大的步数去跳跃，这样就可以更快的到达终点。
    #     # 然而并不会显著提高,依旧超出时间按限制
    #     for nextPos in range(furthestJump, pos, -1):
    #         if self.reach(nums, nextPos):
    #             return True
    #     return False

    # def canJump(self, nums):
    #     """
    #     思路2: 自顶向下的动态规划法
    #     纪录每个位置是否为能够到达终点的GOOD位置,避免重复计算
    #     时间复杂度: O(n^2) 每一个元素都在它
    #     空间复杂度: O(n) memo + 递归
    #     """
    #     if nums is None or len(nums) == 1:
    #         return True
    #     l = len(nums)
    #     memo = [' '] * l
    #     def canJumpFromPosition(pos, nums):
    #         if memo[pos] != ' ':
    #             return memo[pos] == 'GOOD'
    #         furthestJump = min(pos + nums[pos], l - 1)
    #         for nextPos in range(pos+1, furthestJump+1):
    #             # 优化: 从后往前需要遍历次数更少,直觉上，就是我们每次选择最大的步数去跳跃，这样就可以更快的到达终点。
    #             # 然而并不会显著提高,依旧超出时间按限制
    #             if canJumpFromPosition(nextPos, nums):
    #                 memo[pos] = 'GOOD'
    #                 return True
    #         memo[pos] = 'BAD'
    #         return False
    #     # 必须把终点设为GOOD,才能将GOOD向前传递
    #     memo[-1] = 'GOOD
    #     return canJumpFromPosition(0, nums)
    # def canJump(self, nums):
    #     """
    #     思路2: 自底向上的动态规划法
    #     自顶向下需要递归, 自底向上省去了这部分的空间和计算时间,更为高效
    #     从右往左
    #     """
    #     if nums is None or len(nums) == 1:
    #         return True
    #     l = len(nums)
    #     memo = [' '] * l
    #     memo[-1] = 'GOOD'
    #     # 从终点前一个位置向前遍历,如果它能到达终点则为GOOD
    #     for i in range(l-2, -1, -1):
    #         furthestJump = min(i+nums[i], l-1)
    #         for j in range(i+1, furthestJump+1):
    #             if memo[j] == 'GOOD':
    #                 memo[i] = 'GOOD'
    #                 break
    #     return memo[0] == 'GOOD'
    def canJump(self, nums):
        """
        贪心法
        从右往左,如果从当前位置能够调到最远的好位置则该位置为好位置
        第一个好位置是终点
        """
        if nums is None or len(nums) == 1:
            return True
        l = len(nums)
        lastPos = l - 1
        for i in range(l-1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0


so = Solution()
print(so.canJump([2, 3, 1, 1, 4]))



