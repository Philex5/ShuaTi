def quickSort(nums, low, high):
    if low >= high:
        return
    first, last, key = low, high, nums[low]
    while first < last:
        while nums[last] >= key and last > first:
            last -= 1
        nums[first] = nums[last]
        while nums[first] <= key and last > first:
            first += 1
        nums[last] = nums[first]
    nums[first] = key
    quickSort(nums, first+1, high)
    quickSort(nums, low, first-1)


a = [3, 5, 2, 1, 7, 8, 2, 9]
quickSort(a, 0, len(a)-1)
print(a)
