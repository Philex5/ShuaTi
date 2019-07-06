# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 下午9:05
# @Author  : Philex
# @File    : complexListNode.py
# @Software: PyCharm

"""
剑指offer 面试题35: 复杂链表的复制
"""


class ComplexListNode:
    def __init__(self, val=None, next=None, sibling=None):
        self.val = val
        self.next = next
        self.sibling = sibling


# 第一步,在每个节点后添加复制节点,并且复制节点的sibling指向与原节点相同
def cloneNode(pHead):
    pNode = pHead
    while pNode:
        pClone = ComplexListNode()
        pClone.val = pNode.val
        pClone.next = pNode.next
        pClone.sibling = pNode.sibling

        pNode.next = pClone
        pNode = pClone.next


# 调整每个复制节点的sibling指向,应为原节点sibling指向的下一个位置
def connectSiblingNodes(pHead):
    pNode = pHead
    while pNode:
        pCloned = pNode.next
        if pNode.sibling:
            pCloned.sibling = pNode.sibling.next
        pNode = pCloned.next


def reconnectNodes(pHead):
    pNode = pHead
    pCloneHead = None
    pCloneNode = None

    if pNode:
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next
    while pNode:
        pCloneNode.next = pNode.next
        pCloneNode = pCloneNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next
    return pCloneHead


def solution(pHead):
    cloneNode(pHead)
    connectSiblingNodes(pHead)
    return reconnectNodes(pHead)
