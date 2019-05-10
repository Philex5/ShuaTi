"""
打乱一个没有重复元素的数组。

示例:

// 以数字集合 1, 2 和 3 初始化数组。
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。
solution.shuffle();

// 重设数组到它的初始状态[1,2,3]。
solution.reset();

// 随机返回数组[1,2,3]打乱后的结果。
solution.shuffle();
"""
"""
如何保证概率相同 -> 选取等概率不重复数字 -> 先生成数字，再打乱数字顺序
本题中数字已生成，打乱顺序即可
"""
from random import randint
class Solution:

    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        new_nums = []
        for i in range(len(self.nums)):
            new_nums.append(self.nums[i])
        for i in range(len(self.nums)):
            rand = randint(0, len(new_nums)-1)
            new_nums[i], new_nums[rand] = new_nums[rand], new_nums[i]
        return new_nums


# Your Solution object will be instantiated and called as such:
nums = [3, 4, 5]
obj = Solution(nums)
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())