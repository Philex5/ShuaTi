"""
图的深度优先遍历的递归实现和非递归实现
深度优先遍历，从起点出发沿着一个方向走到头，之后再换方向
"""
from graph import graph
from collections import deque
class DepthFirstSearch(object):

    def __init__(self, g, s):
        self.marked = [False] * g.getV()
        self.count = [0] * g.getV()
        # 用来记录顶点索引所对应的父节点
        # 遍历从s到达t，那么edgeTo[s
        self.edgeTo = [0] * g.getV()
        self.s = s
        self.stack = deque()
        self.stack.append(s)
        self.dfs(g, s)

    # 递归形式实现
    def dfs(self, G, s):
        self.marked[s] = True
        self.count += 1
        for temp in G.getNodeList(s):
            # 选择其中一个方向
            if not self.marked[temp]:
                self.edgeTo[temp] = s
                self.dfs(G, temp)

    # 非递归实现
    def dfs2(self, G, s):
        while len(self.stack) > 0:
            s = self.stack.
            needPop = True
            self.marked[s] = True
            self.count += 1
            for temp in G.adjNodeList(s):
                if not self.marked[temp]:
                    needPop = False
                    self.stack.append(temp)
                    self.edgeTo[temp] = s
                    break
            if needPop:
                self.stack.popleft()











