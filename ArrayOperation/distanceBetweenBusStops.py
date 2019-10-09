"""
环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号为 (i + 1) % n 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 start 到目的地 destination 之间的最短距离。

leetcode 1184
"""
class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        思路：选择顺时针路线和逆时针路线中路程较短的一个
        """
        if not distance:
            return
        if start == destination:
            return 0
        elif start < destination:
            return min(sum(distance[start:destination]), sum(distance[destination:] + distance[:start]))
        else:
            return min(sum(distance[destination: start]), sum(distance[start:] + distance[:destination]))

so = Solution()
print(so.distanceBetweenBusStops([3,14,5,2,21,12,17,24,11,16,15,4,9],3,1))