"""
给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从JFK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。

说明:

如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排序更靠前
所有的机场都用三个大写字母表示（机场代码）。
假定所有机票至少存在一种合理的行程。
示例 1:

输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
示例 2:

输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。
"""

class Solution:
    def findItinerary(self, tickets):
        """
        回溯法
        先排序，可以保证先得到排序小的
        """

        n = len(tickets)
        visited = [False] * n
        # 冒泡排个序先
        for i in range(n-1):
            for j in range(0, n-1-i):
                if tickets[j][1] > tickets[j+1][1]:
                    tickets[j], tickets[j+1] = tickets[j+1], tickets[j]
        return self.findPlan(tickets, visited, ['JFK'], 'JFK')

    def findPlan(self, tickets, visited, plan, end):
        # 设定离开状态
        if len(plan) == len(tickets)+1:
            return plan
        for i in range(len(tickets)):
            # 进入递归：
            if not visited[i] and tickets[i][0] == end:
                visited[i] = True
                res = self.findPlan(tickets, visited, plan + [tickets[i][1]], tickets[i][1])
                if res:
                    return res
                # 回溯法，消除标记
                else:
                    visited[i] = False

so = Solution()
print(so.findItinerary([["JFK", "KUL"], ["JFK", "NRT"],["NRT","JFK"]]))