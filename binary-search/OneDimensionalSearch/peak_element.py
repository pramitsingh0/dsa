def findPeakElement(nums):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        m = l + ((r - l) // 2)
        if (m == n - 1 or nums[m] > nums[m + 1]) and (m == 0 or nums[m] > nums[m - 1]):
            return m
        
        if nums[m + 1] > nums[m]:
            l = m + 1
        elif nums[m - 1] > nums[m]:
            r = m - 1


nums = [1,2,1,3,5,6,4]
print(findPeakElement(nums))