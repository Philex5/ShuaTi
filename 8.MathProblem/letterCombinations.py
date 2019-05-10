import copy
class Solution:
    def letterCombinations(self, digits: str):
        """
        由键盘字符得到对应的字符列表比较容易，关键是怎么进行组合，如果输入字符太多，循环次数太多
        """
        # 用字典就好了，按ASCII码计算，行不通，应为有'7' '9'这两个例外
        # lettersList = []
        # for digit in digits:
        #     if int(digit) <= 6:
        #         letters = [chr(k) for k in range(ord('a')+3*(int(digit)-2), ord('a')+3*(int(digit)-2)+3)]
        #     elif int(digit) == 7:
        #         letters = ['p', 'q', 'r', 's']
        #     elif int(digit) == 8:
        #         letters = ['t', 'u', 'v']
        #     else:
        #         letters = ['w', 'x', 'y', 'z']
        #     lettersList.append(letters)

        # 参考别人的解法
        keys = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                '9': 'wxyz'}
        words = [keys[key] for key in digits if key in keys]
        print(words)
        if len(words) == 0:
            return
        ans = [a for a in words[0]]
        for i in range(1, len(words)):
            temp = ans
            for j in range(len(words[i])):
                a = [_ + words[i][j] for _ in temp]
                # 第一个要替代，不然会留下字母较少的
                if j == 0:
                    ans = a
                else:
                    ans += a
        return ans


so = Solution()
print(so.letterCombinations('923'))




