"""
  有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution(object):
    # 遇左括号入栈，遇右括号与出栈符号对比
    # 要考虑只有左括号的情况
    # 前提，字符串不为空且长度为偶数
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftP = '([{'
        rightP = ')]}'
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []
    # def isValid(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
        # 前提：不为空且长度为偶数
        # if s == []:
        #     return True
        # if len(s) % 2 != 0:
        #     return False
        # de = []
        # leftP = '({['
        # rightP = ')}]'
        # for i in range(len(s)):
        #     if s[i] in leftP:
        #         de.append(s[i])
        #     if s[i] in rightP:
        #         if len(de) == 0:
        #             return False
        #         tmp = de.pop()
        #         print(tmp, s[i])
        #         if s[i] == '(' and tmp != '(':
        #             return False
        #         if s[i] == '}' and tmp != '{':
        #             return False
        #         if s[i] == ']' and tmp != '[':
        #             return False
        # return s == []


so = Solution()
print(so.isValid('()'))



