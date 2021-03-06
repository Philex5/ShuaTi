"""
    树的前序遍历、中序遍历和后序遍历
"""
import collections
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeTraversal:
    # 前序遍历类似深度搜索
    # 先右子节点后左子节点，且从右边弹出
    def PreOrderTraversal(self, root):
        if root is None:
            return
        print(root.val)
        self.PreOrderTraversal(root.left)
        self.PreOrderTraversal(root.right)

    def PreOrderTraversal2(self, root):
        if root is None:
            return
        node = root
        deque = collections.deque()
        deque.append(node)
        while deque:
            node = deque.pop()
            print(node.val)
            if node.right:
                deque.append(node.right)
            if node.left:
                deque.append(node.left)


    # 中序遍历
    # 递归方法
    def InOrderTraversal(self, root):
        if root is None:
            return
        self.InOrderTraversal(root.left)
        print(root.val)
        self.InOrderTraversal(root.right)

    # 非遍历解法
    def InOrderTraversal2(self, root):
        if root is None:
            return
        deque = collections.deque()
        node = root

        while deque or node:
            if node is not None:
                deque.append(node)
                node = node.left
            else:
                TNode = deque.pop()
                print(TNode.val)
                node =TNode.right


    # 后序遍历
    def PostOrderTraversal(self, root):
        if root is None:
            return
        self.PostOrderTraversal(root.left)
        self.PostOrderTraversal(root.right)
        print(root.val)

    # 非递归解法
    def PostOrderTraversal1(self, root):
        # 把后续遍历的逆序存到stack2中
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while len(stack1) > 0:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while len(stack2) > 0:
            print(stack2.pop().val)



if __name__ == '__main__':
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

    tt = TreeTraversal()
    # tt.InOrderTraversal1(node1)
    # tt.InOrderTraversal2(node1)
    # tt.PreOrderTraversal1(node1)
    # tt.PreOrderTraversal2(node1)
    # tt.PostOrderTraversal(node1)
    tt.PostOrderTraversal1(node1)









