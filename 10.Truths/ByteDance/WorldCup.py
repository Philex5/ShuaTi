# class Solution(object):
#     def __init__(self, ):


def countFans(sets, i, j, visited):
    if i >= M or j >= M:
        return 0
    if visited[i][j] == 1:
        return 0
    elif sets[i][j] == 0:
        visited[i][j] = 1
        return 0
    else:
        visited[i][j] = 1
        count = 1 + countFans(sets, i, j+1, visited) + countFans(sets, i, j-1, visited) \
                  + countFans(sets, i-1, j, visited) + countFans(sets, i+1, j, visited) \
                  + countFans(sets, i - 1, j-1, visited) + countFans(sets, i + 1, j-1, visited) \
                  + countFans(sets, i - 1, j+1, visited) + countFans(sets, i + 1, j+1, visited)
        print(count)
        return count


if __name__ == '__main__':
    strMN = input()
    MN = strMN.split(',')
    M = int(MN[0])
    N = int(MN[1])
    sets = []
    for i in range(M):
        strNums = input()
        nums = strNums.split(',')
        for j in range(N):
            sets[i][j] = int(nums[j])
        sets.append(list(map(int, input().split(','))))

    # M = 10
    # N = 10
    # sets = []
    # sets.append([0,0,0,0,0,0,0,0,0,0])
    # sets.append([0,0,0,1,1,0,1,0,0,0])
    # sets.append([0,1,0,0,0,0,0,1,0,1])
    # sets.append([1,0,0,0,0,0,0,0,1,1])
    # sets.append([0,0,0,1,1,1,0,0,0,1])
    # sets.append([0,0,0,0,0,0,1,0,1,1])
    # sets.append([0,1,1,0,0,0,0,0,0,0])
    # sets.append([0,0,0,1,0,1,0,0,0,0])
    # sets.append([0,0,1,0,0,1,0,0,0,0])
    # sets.append([0,1,0,0,0,0,0,0,0,0])
    #visited = [[0] * N] * M
    visited = []
    for i in range(M):
        vi = []
        for j in range(N):
            vi.append(0)
        visited.append(vi)
    groupIndex = 0
    maxFanNum = 0
    for i in range(M):
        for j in range(N):
            if sets[i][j] == 1 and visited[i][j] == 0:
                fanNums = countFans(sets, i, j, visited)
                print(fanNums)
                maxFanNum = max(fanNums, maxFanNum)
                groupIndex += 1
            visited[i][j] = 1
    print(groupIndex, maxFanNum)



"""
0,0,0,0,0,0,0,0,0,0
0,0,0,1,1,0,1,0,0,0
0,1,0,0,0,0,0,1,0,1
1,0,0,0,0,0,0,0,1,1
0,0,0,1,1,1,0,0,0,1
0,0,0,0,0,0,1,0,1,1
0,1,1,0,0,0,0,0,0,0
0,0,0,1,0,1,0,0,0,0
0,0,1,0,0,1,0,0,0,0
0,1,0,0,0,0,0,0,0,0"""






