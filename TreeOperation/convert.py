# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 下午5:12
# @Author  : Philex
# @File    : convert.py
# @Software: PyCharm


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def convert(root):
    pLastNodeInList = None
    convertNode(root, pLastNodeInList)

    # pLastNodeInList 指向双向链表的尾节点
    # 需要返回头结点
    pHeadOfList = pLastNodeInList
    while pHeadOfList and pHeadOfList.left:
        pHeadOfList = pHeadOfList.left

    return pHeadOfList


def convertNode(pNode, pLastNodeInList):
    if not pNode:
        return

    pCurrent = pNode

    if pCurrent.left:
        convertNode(pCurrent.left, pLastNodeInList)

    pCurrent.left = pLastNodeInList

    if pLastNodeInList:
        pLastNodeInList.right = pCurrent

    pLastNodeInList = pCurrent

    if pCurrent.right:
        convertNode(pCurrent.right, pLastNodeInList)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.right = node6
node5.left = node7
node5.right = node8

convertedNode1 = convert(node1)
node = convertedNode1
while node:
    print(node.val)
    node = node.right
