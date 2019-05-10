# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
#   ]
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]


class Solution:
    # beat 85%
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # 先沿着从右到左的对角线调换所有对角元素, 之后{i行与size-i-1行, 0<=i<=size//2-1)调换所有列元素即可实现数组原地旋转
        size = len(matrix[0])
        for i in range(size-1):
            for j in range(size-i-1):
                matrix[i][j], matrix[size-j-1][size-i-1] = matrix[size-j-1][size-i-1], matrix[i][j]
        print(matrix)

        for i in range(size//2):
            for j in range(size):
                matrix[i][j], matrix[size-i-1][j] = matrix[size-i-1][j], matrix[i][j]

        print(matrix)

a = [
  [5, 1, 9, 11],
  [2, 4, 8, 10],
  [13, 3, 6, 7],
  [15, 14, 12, 16]
]
so = Solution()
so.rotate(a)




