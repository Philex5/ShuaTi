"""
剑指offer 6 从后往前打印链表

先进后出，很容易想到用栈来解决
"""
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def s6solution(root):
    if not root:
        print(' ')
        return
    node = root
    nodes = []
    while node:
        nodes.append(node)
        node = node.next
    while len(nodes) > 0:
        node = nodes.pop()
        print(node.val)
    return

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4

s6solution(node1)






