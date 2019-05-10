"""
写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

class Solution:
    def fizzBuzz(self, n: int):
    #     for i in range(1, n+1):
    #         if i % 3 == 0:
    #             if i % 5 == 0:
    #                 print('FizzBuzz')
    #             else:
    #                 print('Fizz')
    #         elif i % 5 == 0:
    #             print('Buzz')
    #         else:
    #             print(str(i))
        return ["Fizz" * (i % 3 ==  0) + "Buzz" * (i % 5 == 0) +
            str(i) * (i % 3 != 0 and i % 5 != 0) for i in range(1, n+1)]


so = Solution()
print(so.fizzBuzz(20))