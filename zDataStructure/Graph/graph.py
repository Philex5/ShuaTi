"""
邻接矩阵，邻接表构建图
"""
class graph(object):
    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = [[0] * V for i in range(V)]
        self.adjlist = [[0] * V]

    def addEdge(self, v1, v2, weight = 1):
        if v1 < 0 or v1 > self.V or v2 < 0 or v2 > self.V:
            print('Edge added fail')
            return
        # 有向图
        self.adj[v1][v2] = weight
        self.adjlist[v1].append(v2)
        # 无向图
        #self.adj[v1][v2] = 1
        #self.adj[v2][v1] = 1
        self.adjlist[v1].append(v2)
        self.adjlist[v2].append(v1)
        self.E += 1

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    # 返回指定点的所有邻接点,两种方式
    def getNodeList(self, v):
        list = []
        for i in range(self.V):
            if self.adj[v][i] > 0:
                list.append(v)
        return list
        # return self.adjlist[v]



