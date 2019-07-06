# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 下午9:27
# @Author  : Philex
# @File    : simplifyPath.py
# @Software: PyCharm

"""
以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。

示例 1：
输入："/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。
示例 2：

输入："/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根是你可以到达的最高级。
示例 3：

输入："/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。
示例 4：

输入："/a/./b/../../c/"
输出："/c"
示例 5：

输入："/a/../../b/../c//.//"
输出："/c"
示例 6：

输入："/a//b////c/d//././/.."
输出："/a/b/c"
"""

from collections import deque
class Solution:
    def simplifyPath(self, path):
        """
        思路,以'/'为分隔符,分出各个目录名,放入栈中,后入先出来处理'..'字符,跳过当前目录
        最后把剩下的目录名,倒着组成路径(因为是按后入先出的操作,所以处理完的顺序是反的)
        """

        ways = path.split('/')
        path = []
        for way in ways:
            if way == '..':
                if path:
                    path.pop()
            elif way and way != '.':
                path.append(way)

        return "/" + "/".join(path)

    # def simplifyPath(self, path):
    #     """
    #     简洁版(人家的代码)
    #     对呀,直接从处理完的里面pop不就好了,干嘛对分割后的字符pop设置,当做处理之后的保存.
    #     """
    #     stack = []
    #     path = path.split("/")
    #
    #     for item in path:
    #         print(stack)
    #         if item == "..":
    #             if stack: stack.pop()
    #         elif item and item != ".":
    #             stack.append(item)
    #     return "/" + "/".join(stack)


so = Solution()
print(so.simplifyPath("/a/../../b/../c//.//"))



