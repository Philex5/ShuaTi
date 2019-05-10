import numpy as np
class Solution:
    # beat %1
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        board = np.asarray(board)
        for i in range(9):
            if not self.judge(board[i, :]):
                print('第 %s 行 不独' % i)
                return False
            if not self.judge(board[:, i]):
                print('第 %s 列 不独' % i)
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                print(i, j)
                if not self.judge(np.reshape(board[i:i+3, j:j+3], [9, ])):
                    print('坐上角坐标为(%s, %s) 的正方框不独'.format(i, j))
                    return False
        return True

    def judge(self, nums):
        """
        :type  nums: List[list[str]]
        :return: bool
        """
        flags = [False] * 10
        for i in range(9):
            if nums[i] == '.':
                continue
            if flags[int(nums[i]) - 1]:
                return False
            flags[int(nums[i])-1] = True
        return True

    # beat 7%
    def isValidSudoku1(self, board):
        raw_record = np.zeros([9, 10])
        col_record = np.zeros([9, 10])
        square_record = np.zeros([9, 10])

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if raw_record[i, num] == 1 or col_record[j, num] == 1\
                        or square_record[(j//3)*3 + i//3, num] == 1:
                    print(num)
                    return False
                else:
                    raw_record[i, num] = 1
                    col_record[j, num] = 1
                    square_record[(j//3)*3 + i//3, num] = 1
        return True

board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
         ["2", ".", ".", ".", ".", ".", ".", ".", "."],
     ["3", ".", ".", ".", ".", ".", ".", ".", "."],
         ["4", ".", ".", ".", ".", ".", ".", ".", "."],
     ["5", ".", ".", ".", ".", ".", ".", ".", "."],
     ["6", ".", ".", ".", ".", ".", ".", ".", "."],
     ["7", ".", ".", ".", ".", ".", ".", ".", "."],
     ["8", ".", ".", ".", ".", ".", ".", ".", "."],
     ["9", ".", ".", ".", ".", ".", ".", ".", "."]]


so = Solution()
print(so.isValidSudoku1(board))