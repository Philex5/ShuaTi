class Solution:
    def maxArea(self, height):
        # 固定左边界，寻找右边界，时间复杂度O(n^2)
        # 超出时间限制
        # l = len(height)
        # maxAreas = 0
        # for i in range(height-1):
        #     for j in range(i+1, height):
        #         currAreas = (j-i) * min(height[i], height[j])
        #         maxAreas = currAreas if currAreas > maxAreas else maxAreas
        #
        # return maxAreas

        # 双指针法，所指线段短的指针进行移动
        l = len(height)
        maxAreas = 0
        i = 0
        j = l - 1
        while i < j:
            currAreas = (j-i) * min(height[i], height[j])
            maxAreas = currAreas if currAreas > maxAreas else maxAreas
            if height[i] <= height[j]:
                i += 1
            else:
                j += 1
        return maxAreas




