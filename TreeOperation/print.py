"""
之字形打印节点值
"""
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printNode(root):
    if not root:
        return
    toBePrint = 1
    nextLevel = 0
    odd = 1
    deq = deque()    # 偶数层的栈
    deq1 = deque()   # 奇数层的栈
    deq.append(root)
    while deq or deq1:
        if not odd:
            node = deq1.popleft()
            print(node.val, end=' ')
            if node.right:
                deq.append(node.right)
                nextLevel += 1
            if node.left:
                deq.append(node.left)
                nextLevel += 1
        else:
            node = deq.pop()
            print(node.val, end=' ')
            if node.right:
                deq1.append(node.right)
                nextLevel += 1
            if node.left:
                deq1.append(node.left)
                nextLevel += 1
        toBePrint -= 1
        if toBePrint == 0:
            print()
            toBePrint = nextLevel
            nextLevel = 0
            odd = 1 if odd == 0 else 0

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8
printNode(node1)