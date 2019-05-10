class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        先排序，然后遍历两个列表找并集
        """
        if nums1 == [] or nums2 == []:
            return []
        list1 = sorted(nums1)
        list2 = sorted(nums2)
        intersection = []
        i = 0
        j = 0
        while 1:
            while list1[i] < list2[j]:
                i += 1
                if i >= len(list1):
                    return intersection
            while list1[i] > list2[j]:
                j += 1
                if j >= len(list2):
                    return intersection
            if list1[i] == list2[j]:
                intersection.append(list1[i])
                i += 1
                j += 1
                if i >= len(list1) or j >= len(list2):
                    return intersection


    def intersect2(self, nums1, nums2):
        """
        先用字典储存nums1中的值以及它出现的次数
        再遍历nums2,若其中的值存在于字典的键，则把该键加入结果列表，该键对应的值-1
        """
        maps = {}
        results = []
        for num1 in nums1:
            if num1 in maps.keys():
                maps[num1] += 1
            else:
                maps[num1] = 1
        print(maps)
        for num2 in nums2:
            if num2 in maps.keys():
                if maps[num2] > 0:
                    maps[num2] -= 1
                    print(num2)
                    results.append(num2)
        print(results)

        return results


so = Solution()
so.intersect2([4, 9, 5], [9, 4, 9, 8, 4])
