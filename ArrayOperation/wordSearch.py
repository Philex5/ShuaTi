class Solution:
    def exist(self, board, word):
        """
        典型的回溯法问题，在二维数组中移动，但是要单词起始要先找出来
        """
        if word == '':
            return
        l = len(board)
        w = len(board[0])
        print(l, w)
        visited = [[False] * w for i in range(l)]
        count = 0
        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    if self.search(board, word, count, i, j, l, w, visited):
                        return True
        return False

    def search(self, board, word, count, i, j, l, w, visited):
        if i < 0 or i > l-1 or j < 0 or j > w-1 or visited[i][j]:
            return False
        if board[i][j] == word[count]:
            count += 1
            print(i, j, count)
        else:
            return False
        if count == len(word):
            print(i, j, count)
            return True
        visited[i][j] = True
        if self.search(board, word, count, i-1, j, l, w, visited) or \
                self.search(board, word, count, i+1, j, l, w, visited) or \
                self.search(board, word, count, i, j-1, l, w, visited) or \
                self.search(board, word, count, i, j+1, l, w, visited):

            return True
        else:
            visited[i][j] = False
            return False

so = Solution()
print(so.exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB"))