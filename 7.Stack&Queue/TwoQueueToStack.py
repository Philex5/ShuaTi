from collections import deque

class StackByTwoQueue(object):
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, value):
        if len(self.queue2) != 0:
            self.queue2.append(value)
        else:
            self.queue1.append(value)

    def pop(self):
        if len(self.queue1) != 0:
            while len(self.queue1) != 1:
                self.queue2.append(self.queue1.popleft())
            self.queue1.pop()
        elif len(self.queue2) != 0:
            while len(self.queue2) != 1:
                self.queue1.append(self.queue2.popleft())
            self.queue2.pop()
        else:
            raise ('Empoty Queue')


de = StackByTwoQueue()
de.push('a')
de.push('b')
de.push('c')
print(de.queue1)
print(de.queue2)
de.pop()
de.pop()
print(de.queue1)
print(de.queue2)
de.push('d')
print(de.queue1)
print(de.queue2)
de.pop()
print(de.queue1)
print(de.queue2)




