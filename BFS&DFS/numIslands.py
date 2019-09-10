"""
给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

示例 1:

输入:
11110
11010
11000
00000

输出: 1
示例 2:

输入:
11000
11000
00100
00011

输出: 3

"""

class Solution(object):
    def numIslands(self, grid):
        """
        怎么快速找到边界？ 确定岛屿
        深度优先搜索，将二维网格看成一个无向图，竖直或水平相邻的 1 之间有边。
        线性扫描整个二维网格，如果一个结点包含 1，则以其为根结点启动深度优先搜索。
        在深度优先搜索过程中，每个访问过的结点被标记为 0。
        计数启动深度优先搜索的根结点的数量，即为岛屿的数量。
        这就是无向图的联通块问题，我们遍历所有是1的位置，进行dfs，
        并且将所有访问过的位置记录下来,如果当前位置是1,而且没有访问,则次数就加1.

        """
        if not grid or len(grid) == 0:
            return
        nr = len(grid)
        nc = len(grid[0])
        num_island = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    num_island += 1
                    self.dfs(grid, r, c)
        return num_island

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        if r < 0 or c < 0 or r >= nr or c >= nc or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)