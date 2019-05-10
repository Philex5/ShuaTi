from collections import deque

class QueueByTwoStack():
    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, value):
        self.stack1.append(value)

    def pop(self):
        if len(self.stack2) == 0:
            if len(self.stack1) == 0:
                raise ( 'Stack is None!' )
            else:
                while len(self.stack1) > 0:
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


qb = QueueByTwoStack()
qb.push('a')
qb.push('b')
qb.push('c')
qb.pop()
qb.pop()
print(qb.stack1)
print(qb.stack2)
qb.push('d')
qb.push('e')
print(qb.stack1)
print(qb.stack2)
qb.pop()
qb.pop()
qb.pop()
qb.pop()
