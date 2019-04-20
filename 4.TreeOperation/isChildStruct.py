"""
From  剑指Offer
判断一个树是否是另一个树的子结构

"""
class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

import collections


def isCS(node, rootB):
    if not rootB:
        return True
    if not node or node.val != rootB.val:
        return False
    return isCS(node.left, rootB.left) and isCS(node.right, rootB.right)


def isChildStruct(rootA, rootB):
    # 判断B是否是A的子结构
    # 先在A中找到值和B根节点相同的节点
    if not rootB and not rootA:
        return True
    if not rootB:
        return True
    if not rootA:
        return False

    deq = collections.deque()
    deq.append(rootA)
    while deq:
        node = deq.pop()
        if node.val == rootB.val:
            if isCS(node, rootB):
                return True
        if node.left:
            deq.append(node.left)
        if node.right:
            deq.append(node.right)
    return False



