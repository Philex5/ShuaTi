import math
"""
求x的平方根，精度为0.01
"""
def my_square(x, precision=0.01):
    """
    二分法查找的思想，找到 一个 y,使得 abs(y^2 - x) < 0.01
    利用中点划分[0, x],在根据， ((x + 0)/2) ^ 2与x的大小关系，改变左右端点
    :param x:
    :param precision:
    :return:
    """
    if x == 0:
        return 0
    left = 0
    right = x
    mid = left + (right - left) / 2
    while (abs(mid ** 2 - x) > precision):
        temp = mid ** 2
        if temp > x:
            right = mid
        elif temp < x:
            left = mid
        mid = left + (right - left) / 2
    return mid, -1 * mid

print(my_square(10))
print(math.sqrt(10))


