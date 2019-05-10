
import sys

if __name__ == '__main__':
    try:
        while True:
            lengthOfRandomNums = int(sys.stdin.readline().strip())
            nums = []
            for i in range(lengthOfRandomNums):
                nums.append(int(sys.stdin.readline()))
            # 暴力法
            # nums = sorted(nums)
            # same = 0
            # for i in range(lengthOfRandomNums-1):
            #     while nums[i] == nums[i+1] and i < lengthOfRandomNums -1 - same:  # 多个重复的情况
            #         for j in range(i, lengthOfRandomNums-1):
            #             nums[j] = nums[j+1]
            #         same += 1
            # nums = nums[:lengthOfRandomNums - same]
            # print(nums)

            # 哈希表法
            mapping = [0] * 1000
            for num in nums:
                mapping[num] = 1
            for i in range(1000):
                if mapping[i] == 1:
                    print(i)

    except:
        pass