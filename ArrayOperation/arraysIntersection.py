"""
给出三个均为 严格递增排列 的整数数组 arr1，arr2 和 arr3。

返回一个由 仅 在这三个数组中 同时出现 的整数所构成的有序数组。

 

示例：

输入: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
输出: [1,5]
解释: 只有 1 和 5 同时在这三个数组中出现.

"""


class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        思路一：利用集合的交操作
        因为set无序，所以顺序会变，需要最后排个序
        利用内置数据结构，时间空间都消耗极低，战胜100%
        :param arr1:
        :param arr2:
        :param arr3:
        :return:
        """
        if not arr1 or not arr2 or not arr3:
            return []
        arr1 = set(arr1)
        arr2 = set(arr2)
        arr3 = set(arr3)
        arr1 = arr1.intersection(arr2)
        arr1 = arr1.intersection(arr3)
        return sorted(list(arr1))

    def arraysIntersection1(self, arr1, arr2, arr3):
        """
        思路二：统计各个数字在三个列表中出现的次数，次数为3的为相交的数字
        """
        res = []
        apperance = {}
        for i in arr1:
            if i in apperance.keys():
                continue
            else:
                apperance[i] = 1
        for i in arr2:
            if i in apperance.keys() and apperance[i] == 1:
                apperance[i] += 1
            else:
                apperance[i] = 1
        for i in arr3:
            if i in apperance.keys() and apperance[i] == 2:
                apperance[i] += 1
            else:
                apperance[i] = 1
        for key in apperance.keys():
            if apperance[key] == 3:
                res.append(key)
        return res




so = Solution()
print(so.arraysIntersection1(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))