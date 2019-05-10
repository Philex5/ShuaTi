"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.point = -1

    def push(self, x: int) -> None:
        self.nums.append(x)
        self.point += 1

    def pop(self) -> None:
        a = self.nums[self.point]
        self.point -= 1
        self.nums = self.nums[:self.point+1]
        return a

    def top(self) -> int:
        return self.nums[self.point]

    def getMin(self) -> int:
        if len(self.nums) != 0:
            return min(self.nums)
        return 0

# Your MinStack object will be instantiated and called as such:
x = 10
obj = MinStack()
obj.push(x)
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)