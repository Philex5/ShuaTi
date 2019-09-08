"""
现在你总共有 n 门课需要选，记为 0 到 n-1。

在选修某些课程之前需要一些先修课程。 例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]

给定课程总量以及它们的先决条件，判断是否可能完成所有课程的学习？

示例 1:

输入: 2, [[1,0]]
输出: true
解释: 总共有 2 门课程。学习课程 1 之前，你需要完成课程 0。所以这是可能的。
示例 2:

输入: 2, [[1,0],[0,1]]
输出: false
解释: 总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0；并且学习课程 0 之前，你还应先完成课程 1。这是不可能的。
说明:

输入的先决条件是由边缘列表表示的图形，而不是邻接矩阵。详情请参见图的表示法。
你可以假定输入的先决条件中没有重复的边。
提示:

这个问题相当于查找一个循环是否存在于有向图中。如果存在循环，则不存在拓扑排序，因此不可能选取所有课程进行学习。
通过 DFS 进行拓扑排序 - 一个关于Coursera的精彩视频教程（21分钟），介绍拓扑排序的基本概念。
拓扑排序也可以通过 BFS 完成。

"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        广度优先排序/拓扑排序：
        [0, 1] <-> 0 <- 1, 能否完成，相当于判断是否存在有向无环图(DAG)
        将入度为0的结点加入列表
        去掉入度为0的结点，再将它指向的结点入度-1，学习过的courses + 1 若减去之后为0，加入列表，
        courses = numCourses -> can Finish
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        时间复杂度: O(n^2)
        空间复杂度: O(n^2)
        """
        # record nodes which into == 0
        intos = [0] * numCourses
        in0nodes = []
        links = [[0] * numCourses for i in range(numCourses)]
        for prere in prerequisites:
            intos[prere[0]] += 1
            links[prere[1]][prere[0]] = 1
        for c, val in enumerate(intos):
            if val == 0:
                in0nodes.append(c)
        print(in0nodes)
        count = 0
        while in0nodes:
            node = in0nodes.pop()
            count += 1
            for i in range(numCourses):
                if links[node][i] == 1:
                    intos[i] -= 1
                    if intos[i] == 0:
                        in0nodes.append(i)
                        break
        if count == numCourses:
            return True
        return False

    def canFinish1(self, numCourses, prerequisites):
        """
        深度优先排序
        通过DFS判断图中是否有环
        使用标记数组
        被当前结点访问过标记为1，若遇到为1的直接False
        被其他节点访问过标记为-1，无需重复搜索，直接返回True
        :param numCourses:
        :param prerequisites:
        :return:
        时间复杂度: O(n^2)
        空间复杂度：O(n^2)
        """
        links = [[] for i in range(numCourses)]
        flags = [0] * numCourses
        for prere in prerequisites:
            links[prere[1]].append(prere[0])
        for node in range(numCourses):
            if not self.dfs(node, links, flags, numCourses):
                return False
        return True

    def dfs(self, node, links, flags, numCourses):
        if flags[node] == -1:
             return True
        if flags[node] == 1:
             return False
        flags[node] = 1
        for i in links[node]:
            if not self.dfs(i, links, flags, numCourses):
                return False
        flags[node] = -1
        return True


so = Solution()
print(so.canFinish1(2, [[0, 1]]))








