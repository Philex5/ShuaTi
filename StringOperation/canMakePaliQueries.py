class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        问题：替换指定数量字母能否构成回文串
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        res = []
        # 优化超时问题，用空间换时间
        # 使用一个二维数组 len(s) * 26 保存到每个位置各个字母的数量
        letters = [[0] * 26 for i in range(len(s))]
        letters[0][ord(s[0]) - ord('a')] += 1
        for i in range(len(s)):
            letters[i] = [value for value in letters[i-1]]
            index = ord(s[i]) - ord('a')
            letters[i][index] = letters[i][index] + 1
        print(letters)
        for query in queries:
            left, right, k = query
            q = s[left: right+1]
            # 构成回文字符，代表字母中心对称
            # 不能全A,没有考虑重新排列的情况
            # q_rev = q[::-1]
            # needs = 0
            # for i in range(len(q)//2):
            #     if q[i] != q_rev[i]:
            #         needs += 1
            # print(q, q_rev, needs, k)
            # if needs <= k:
            #     res.append(True)
            # else:
            #     res.append(False)

            # 其实也就是说
            # 当长度为偶数，把字母都凑成对就可以了
            # 当长度为奇数，有一个不成对就可以了
            # l = len(q)
            # # 统计成对的个数,不能使用set，可能出现3个4个呀
            # temp = [str(letter) for letter in q]
            # temp = set(temp)
            # couple_num = l - len(temp)
            # 使用dict，偶数不需要替换奇数需要
            # 然而，超出时间限制，kuso！！！
            # d = {}
            # for i in q:
            #     if i not in d.keys():
            #         d[i] = 1
            #     else:
            #         d[i] += 1
            # needs = 0
            # for key in d.keys():
            #     needs += d[key] % 2
            # 这一步时能通过的关键，减少不必要的时间
            if k >= right - left + 1:
                res.append(True)
                continue
            needs = 0
            letters_temp = letters[right] if left == 0 else [letters[right][v] - letters[left-1][v] for v in range(26)]
            for i in range(26):
                needs += letters_temp[i] % 2
            if len(q) % 2 == 1:
                needs = (needs-1) // 2
            else:
                needs = needs // 2
            if needs <= k:
                res.append(True)
            else:
                res.append(False)
        return res

so = Solution()
print(so.canMakePaliQueries("abcda",
[[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]))