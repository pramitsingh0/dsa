def partition(nums, low, high):
    pivot_ind = (low + high) // 2
    pivot = nums[pivot_ind]
    nums[high], nums[pivot_ind] = nums[pivot_ind], nums[high]
    i = low
    j = high - 1
    while True:
        while i < high and nums[i] <= pivot:
            i += 1
        while j >= 0 and nums[j] > pivot:
            j -= 1
        if i > j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[i], nums[high] = nums[high], nums[i]
    return i


def quickSort(nums, low, high):
    if low < high:
        partition_ind = partition(nums, low, high)
        quickSort(nums, low, partition_ind - 1)
        quickSort(nums, partition_ind + 1, high)


nums = [10, 7, 8, 9, 1, 5]
print(quickSort(nums, 0, 5))

print(nums)
