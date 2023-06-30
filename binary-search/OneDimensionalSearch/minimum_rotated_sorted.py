def findMin(nums):
    l = 0
    r = len(nums) - 1
    min = None
    while l <= r:
        m = (l + r) // 2
        if not min or nums[m] < min:
            min = nums[m]
        if nums[m] > nums[r] and nums[l] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    return min

print(findMin([7,8,9,0,1,3,4,5]))