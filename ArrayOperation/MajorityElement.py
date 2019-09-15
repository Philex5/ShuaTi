"""
题目: 给你一个证书数组，其中有一个数字出现了超过1/2，这个数就是主元素，请找出这个数字。
扩展1: 找到一个主元素，它出现的次数严格大于数组个数的1/3.
"""

class Solution():
    def majorityElement(self, nums):
        if not nums:
            return -1
        major = nums[0]
        cnt = 1
        for num in nums:
            if num == major:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    major = num
        return major

    def majorityElementExpand(self, nums):
        """
        大于1/2个数的扩展，每次去掉3个数
        """
        if not nums:
            return -1
        maina = nums[0]
        mainb = nums[1]
        cnta, cntb = 1, 1
        for i in range(2, len(nums)):
            if nums[i] == maina:
                cnta += 1
            elif nums[i] == mainb:
                cntb += 1
            elif cnta == 0:
                maina = nums[i]
                cnta = 1
            elif cntb == 0:
                mainb = nums[i]
                cntb = 1
            else:
                cnta -= 1
                cntb -= 1
            cnt = 0
            for i in range(0, len(nums)):
                if maina == nums[i]:
                    cnt += 1
            return maina if cnt > len(nums) // 3 else mainb



