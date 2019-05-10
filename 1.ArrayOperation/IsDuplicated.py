import time
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """



so = Solution()
time_start = time.time()
print(so.containsDuplicate([1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 5, 5, 6]))
time_end = time.time()
print('op2 cost', time_end-time_start)


