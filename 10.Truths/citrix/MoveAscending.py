def calInvertNum(index, identification):
    count = 0
    for i in range(index):
        if identification[i] > identification[index]:
            count += 1
    return count


def getMinimumMoves(identification):
    # Write your code here
    dic = {item: i for i, item in enumerate(sorted(identification))}
    c = 0
    for i in range(len(identification)):
        if i != dic[identification[i]] + c:
            c += 1
    return c

print(getMinimumMoves([1, 2, 3]))


