from collections import deque
import copy
#class Solution:
    # def generateParenthesis(self, n):
    #     """
    #     最初方案，交换一个 ( 和 ),行不通，因为n变大之后，可以交换多对
    #     暴力法，产生 2^n个
    #     """
    #
    #
    #     if n < 0:
    #         return []
    #     parenthesis = '(' * n + ')' * n
    #     res = []
    #     res.append(parenthesis)
    #     parenthesis = list(parenthesis)
    #
    #     for i in range(1, n):
    #         for j in range(n, 2*n-1):
    #             mode = copy.copy(parenthesis)
    #             mode[i], mode[j] = mode[j], mode[i]
    #             print(mode)
    #             res.append(''.join(mode))
    #     return res
    #
    # def AreyouOK(self, pathes):
    #     deq = deque()
    #     i = 0
    #     while i < len(pathes):
    #         if pathes[i] == '(':
    #             deq.append(pathes[i])
    #             i += 1
    #         if pathes[i] == ')' and len(deq) == 0:
    #             return False
    #         elif pathes[i] == ')' and deq.popleft() == '(':
    #             i += 1
    #         elif pathes[i] == ')' and deq.popleft() == ')':
    #             return False


class Solution(object):
    def generateParenthesis(self, N):
        """
        回溯法
        """
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                print(S)
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)
        backtrack()
        return ans


so = Solution()
print(so.generateParenthesis(4))


