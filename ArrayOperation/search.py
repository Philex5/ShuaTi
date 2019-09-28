"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

"""
class Solution():

    def search(self, nums, target):
        """
        思路： 可以连续使用二分查找，二分查找找出旋转点，再在两侧分别进行二分查找，找到目标值
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1 and nums[0] != target:
            return -1
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        t = left
        print(t)
        left = 0
        right = len(nums) - 1
        # 注意是“<=”，这样可以应对长度为1的nums
        while left <= right:
            mid = (left + right) // 2
            realmid = (mid + t) % n
            print('left: {} right: {}'.format(left, right))
            print('mid: {} realmid: {} nums[realmid]: {}'.format(mid, realmid, nums[realmid]))
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1.

    def searchOpt(self, nums, target):
        """
        不用先找出旋转的点，直接在二分查找的基础上修改
        l_mid_][_mid_r，根据mid划分为四个区域，l-mid, mid-r可以直接二分，另外两个要不断缩小范围
        """
        if len(nums) <= 0:
            return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1





so = Solution()
print(so.search([4, 5, 6, 7, 0, 1, 2], 1))
print(so.searchOpt([3,1 ], 1))














