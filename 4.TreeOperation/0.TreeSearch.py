import collections
"""
    The BreadthFirstSearch and DepthFirstSearch of Tree
"""

# BFS广度优先搜索，使用先进先出的栈
# 不断弹出弹入树节点，不需要递归运算
def BreadthFirstSearch(root):
    deque = collections.deque()
    values = []
    if root is None:
        return values
    deque.append(root)
    while deque is not None:
        node = deque.popleft()
        values.append(node.value)
        if node.left is not None:
            deque.append(node.left)
        if node.right is not None:
            deque.append(node.right)
    return values


# DFS深度优先搜索, 需要使用栈，先出后进
# 有右子节点先压入右子节点
def DepthFirstSearch(root):
    stack = collections.deque()
    values = []
    stack.append(root)
    while stack is not None:
        node = stack.pop()
        values.append(node.value)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return values








