class Solution:
    # def isPalindrome(self, x: int) -> bool:
    # 把整数转成字符串
    #     if x < 0:
    #         return False
    #     if x < 10:
    #         return True
    #     strx = str(x)
    #     for i in range(len(strx) // 2):
    #         if strx[i] != strx[len(strx)-1-i]:
    #             return False
    #
    #     return True

    # def isPalindrome(self, x: int) -> bool:
    #     # 计算出每一位加入列表
    #     if x < 0:
    #         return False
    #     if x < 10:
    #         return True
    #     strx = []
    #     while x >= 1:
    #         strx.append(x % 10)
    #         x = x // 10
    #
    #     for i in range(len(strx) // 2):
    #         if strx[i] != strx[len(strx)-1-i]:
    #             return False
    #     return True
    def isPalindrome(self, x: int) -> bool:
        # 反转一半长度的数字
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversedNum = 0
        while x > reversedNum:
            reversedNum = reversedNum * 10 + (x % 10)

        return x == reversedNum or x == reversedNum//10









so = Solution()
print(so.isPalindrome(1001))

