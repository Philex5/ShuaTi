"""
剑指offer 7 重建二叉树

输入二叉树的前序遍历和中序遍历的结果，请重建二叉树

"""

class BinaryTreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = right
        self.right = right


def s7solution(preOrders, inorders):
    if len(preOrders) <= 0 or len(inorders) <= 0:
        return None
    rootValue = preOrders[0]
    root = BinaryTreeNode(rootValue)
    p = inorders.index(rootValue)
    print(rootValue)
    root.left = s7solution(preOrders[1:p+1], inorders[:p])
    root.right = s7solution(preOrders[p+1:], inorders[p+1:])
    return root


node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)

node1.left = node2
node1.right = node3
node2.left = node4
node4.right = node7
node3.left = node5
node3.right = node6
node6.left = node8


class TreeTraversal:
    # 前序遍历类似深度搜索
    # 先右子节点后左子节点，且从右边弹出
    def PreOrderTraversal(self, root):
        if root is None:
            return
        print(root.val)
        self.PreOrderTraversal(root.left)
        self.PreOrderTraversal(root.right)


tt = TreeTraversal()

# print(tt.PreOrderTraversal(node1))
root = s7solution([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
#print(tt.PreOrderTraversal(root))















