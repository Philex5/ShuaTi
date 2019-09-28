"""
剑指offer 5 替换空格

把空格替换成"%20"

"""

### 思路一：双指针法，一个指针指向原字符串尾，一个指向计算之后的

def s5func(strs, rep):
    if len(strs) <= 0 or rep == None:
        return
    # 统计空格数
    blankNum = 0
    for str in strs:
        if str == ' ':
            blankNum += 1
    lenStr = len(strs)
    newLenStr = (len(strs) + 2 * blankNum)
    newStrs = [' '] * newLenStr
    p1 = lenStr - 1
    p2 = newLenStr - 1
    while p1 >= 0 and p1 <= p2:
        if strs[p1] == ' ':
            newStrs[p2-len(rep)+1: p2+1] = rep
            p2 -= len(rep)
            p1 -= 1
        else:
            newStrs[p2] = strs[p1]
            p2 -= 1
            p1 -= 1
    return ''.join(newStrs)

print(s5func('I got a lot of offer', '%20'))

