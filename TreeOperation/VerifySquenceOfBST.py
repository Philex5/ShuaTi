"""
剑指Offer 面试题33: 二叉搜索树的后序遍历序列
给出一个序列,判断是否能作为二叉搜索树的后序遍历序列
"""

def verifySquenceOfBST(sequence):
    if not sequence or len(sequence) == 0:
        return False
    print(f'processing {sequence}', end=' ')
    # 后序遍历,根节点在序列的最后
    root = sequence[-1]
    l = len(sequence)
    i = 0
    # 找到左右子树的分离点
    while sequence[i] < root:
        i += 1
    print(f'separate {root}')
    # 分离得到的右子树中是否存在比根节点小的数? 存在则不可能为后序遍历序列
    for j in range(i, l - 1):
        if sequence[j] < root:
            return False
    left = True
    if i > 0:
        left = verifySquenceOfBST(sequence[:i])
    right = True
    if i < l - 1:
        right = verifySquenceOfBST(sequence[i:-1])
    return left and right

seq = [5, 7, 6, 9, 11, 10, 8]
print(verifySquenceOfBST(seq))
