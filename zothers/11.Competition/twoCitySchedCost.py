"""
公司计划面试 2N 人。第 i 人飞往 A 市的费用为 costs[i][0]，飞往 B 市的费用为 costs[i][1]。

返回将每个人都飞到某座城市的最低费用，要求每个城市都有 N 人抵达。
示例：

输入：[[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 A 市，费用为 10。
第二个人去 A 市，费用为 30。
第三个人去 B 市，费用为 50。
第四个人去 B 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。

提示：

1 <= costs.length <= 100
costs.length 为偶数
1 <= costs[i][0], costs[i][1] <= 1000
"""


def quickSort(nums, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = nums[low]
    while low < high:
        while not compare(nums[high], key) and low < high:
            high -= 1
        nums[high], key = key, nums[high]
        while compare(nums[low], key) and low < high:
            low += 1
        nums[low], nums[high] = nums[high], nums[low]
        nums[low] = key
    quickSort(nums, left, low-1)
    quickSort(nums, low+1, right)

def compare(a, b):
    if abs(a[0] - a[1]) > abs(b[0] - b[1]):
        return True

class Solution:
    def twoCitySchedCost(self, costs):
        # key值可能重复
        #diffs = {abs(cost[0] - cost[1]): i for i, cost in enumerate(costs)}
        # 直接快速排序
        quickSort(costs, 0, len(costs) - 1)
        print(costs)
        allFee = 0
        i = 0
        g1 = g2 = 0
        while i < len(costs):
            if g1 == len(costs) // 2:
                while i < len(costs):
                    allFee += costs[i][1]
                    i += 1
                break
            if g2 == len(costs) // 2:
                while i < len(costs):
                    allFee += costs[i][0]
                    i += 1
                break
            if costs[i][0] < costs[i][1]:
                allFee += costs[i][0]
                g1 += 1
            else:
                allFee += costs[i][1]
                g2 += 1
            i += 1
        return allFee

so = Solution()
allcost = so.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]])
print(allcost)