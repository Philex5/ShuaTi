"""
无向图G有N个结点(1<N<=1000)及一些边，每一条边上带有正的权重值。 找到结点1到结点N的最短路径，
或者输出不存在这样的路径。

提示：在每一步中，对于那些没有计算过的结点， 及那些已经计算出从结点1到它的最短路径的结点，
如果它们间有边， 则计算从结点1到未计算结点的最短路径。

"""
import sys
from collections import deque


class Solution:
    def shortestPathOfGraph(self, graph, start, end):
        """
        带权重的图的最短路径使用迪杰斯特拉算法
        本质是不断的刷新起点与其他各个顶点的距离表
        距离表通过迭代刷新，用新路径长度取代旧路径长度，
        最终可以得到从起点到其他顶点的最短距离
        时间复杂度: O(n^2)
        空间复杂度：O(n)
        """
        point_nums = len(graph)
        dis = {}
        for i in range(point_nums):
            dis[i] = sys.maxsize
        dis[start] = 0
        # 首先更新起点到相邻点的距离
        for i in range(point_nums):
            if graph[start][i] != 666 and i != start:
                dis[i] = graph[start][i]
        # 迭代更新距离表
        dis.pop(start)
        for i in range(point_nums-1):
            # 寻找距离起点最近的点
            # min_index = 0
            # min_dis = sys.maxsize
            # for j in range(point_nums):
            #     if j != start and not visited[j] and dis[j] < min_dis:
            #         min_dis = dis[j]
            #         min_index = j
            # 优化使用最小堆
            min_index, min_dis = self.minHeapPop(dis)
            print(min_index, min_dis)
            # 更新最近的点的邻近点到起点的距离
            for j in range(point_nums):
                if j != start and j != min_index and graph[min_index][j] != 666 and j in dis.keys():
                     dis[j] = min(dis[min_index] + graph[min_index][j], dis[j])
            if min_index == end:
                return dis[min_index]
            dis.pop(min_index)



    def shortestPathOfGraphNoWeight(self, graph, start, end):
        """
        无权重，距离的远近由起点到终点经过的结点数量决定
        不用寻找最近的点，直接从已被访问的点进行传播就好了
        时间复杂度O(n^3) 无法接受 迭代次数 * 已更新 * 相邻未更新
        其实就是广度优先遍历呀，复杂度应该没有这么高才对
        广度优先遍历使用列表
        压入弹出控制迭代次数和确定用来传播的结点，机智
        :param graph:
        :param start:
        :param end:
        :return:
        """
        point_nums = len(graph)
        dis = [sys.maxsize] * point_nums
        dis[start] = 0

        # 原始版
        # visited = [False] * point_nums
        # # 首先更新起点到相邻点的距离
        # for i in range(point_nums):
        #     if graph[start][i] != 666 and i != start:
        #         dis[i] = 1
        # visited[start] = True
        # print(dis)
        # # 迭代更新距离表
        # for p in range(point_nums):
        #     # 用被访问过的点更新没有被访问过的点的距离
        #     for i in range(point_nums):
        #         if i != start and dis[i] != sys.maxsize and not visited[i]:
        #             for j in range(point_nums):
        #                 if j != start and j != i and graph[i][j] != 666:
        #                     dis[j] = min(dis[i] + 1, dis[j])
        #         visited[i] = True
        # print(dis)

        # 修改版
        deq = deque()
        for i in range(point_nums):
            if graph[start][i] != 666 and i != start:
                dis[i] = 1
                deq.append(i)
        while deq:
            i = deq.popleft()
            for j in range(point_nums):
                if j != start and j != i and graph[i][j] != 666:
                    dis[j] = min(dis[i] + 1, dis[j])
                    deq.append(j)
        return dis[end]


    def minHeapPop(self, dis):
        """
        使用最小堆优化寻找最短距离，这里每轮构造一个堆，并获得堆顶的值
        """
        def heapConstruct(arr):
            """
            堆的构造: 从倒数第二层使用下沉操作,把最小值置换到堆顶
            """
            N = len(arr) - 1
            k = N // 2
            # 执行下沉操作，构造堆
            while k >= 0:
                sink(arr, k, N)
                k -= 1

        def heapSort(arr):
            # 不断调整各个结点的位置
            N = len(arr) - 1
            while N >= 0:
                arr[0], arr[N] = arr[N], arr[0]
                N -= 1
                sink(arr, 0, N)

        def heapDel(arr):
            """
            堆弹出堆顶值，即最小值
            再把最后一个结点拿到堆顶，执行下沉操作
            """
            arr = arr[1:]
            return heapConstruct(arr)

        def heapAdd(arr, node):
            """
            堆增加新的结点，使用上浮操作
            :param arr:
            :return:
            """
            arr.append(node)
            return heapConstruct(arr)

        def sink(arr, k, N):
            while k * 2 + 1 <= N:
                j = k * 2 + 1
                if j < N and arr[j] > arr[j+1]:
                    j += 1
                if arr[k] < arr[j]:
                    break
                arr[k], arr[j] = arr[j], arr[k]
                k = j

        # 使用距离矩阵构建堆
        disD = {}
        nodes = []
        for key in dis.keys():
            disD[dis[key]] = key
            nodes.append(dis[key])
        heapConstruct(nodes)
        node = nodes[0]
        return disD[node], node


edges = [[0, 1, 12, 666, 666, 666],
         [666, 0, 9, 3, 666, 666],
         [666, 666, 0, 666, 5, 666],
         [666, 666, 4, 0, 13, 15],
         [666, 666, 666, 666, 0, 4],
         [666, 666, 666, 666, 666, 0]]

so = Solution()
print(so.shortestPathOfGraph(edges, start=0, end=5))

