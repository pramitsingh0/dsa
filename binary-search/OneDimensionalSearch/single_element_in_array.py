def singleNonDuplicate(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)
        if (m - 1 < 0 or nums[m] == nums[m - 1]) and (m >= len(nums) or nums[m] == nums[m + 1]):
            return nums[m]
        
        arrLeft = m - 1 if nums[m] == nums[m -1 ] else m
        if arrLeft % 2:
            r = m - 1
        else:
            l = m + 1
    return -1