from collections import deque

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack():
    def __init__(self):
        self.topNode = Node(None)

    def top(self):
        if self.topNode:
            return self.topNode.val
        return None

    def push(self, value):
        node = Node(value)
        node.next = self.topNode
        self.topNode = node

    def pop(self):
        if not self.topNode:
            return None
        node = self.topNode
        self.topNode = self.topNode.next
        return node.val



def isPopOrder(inputOrder, printOrder):
    if not inputOrder or not printOrder:
        return False
    stack = Stack()
    l = len(inputOrder)
    i = 0
    j = 0
    while j < l:
        while stack.topNode.val != printOrder[j] and i < l:
            stack.push(inputOrder[i])
            i += 1
        if stack.topNode.val == printOrder[j]:
           print(stack.pop())
           j += 1
        else:
            return False
    return True


print(isPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))



