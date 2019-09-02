class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        思路：按周期k天切分，计算每个周期内的得分，最终计总分
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: ints
        :rtype: int
        """
        score = 0
        days = len(calories)
        i = 0
        while i + k <= days:
            if sum(calories[i:i + k]) < lower:
                score -= 1
            elif sum(calories[i:i + k]) > upper:
                score += 1
            i += 1
        return score

so = Solution()
print(so.dietPlanPerformance([3,10,17,12,19,6,17,4,15,18], 5, 34, 53))

