def searchInsert(nums, target):
    low = 0
    right = len(nums) - 1
    while low <= right:
        mid = (low + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            low = mid + 1
    return low

