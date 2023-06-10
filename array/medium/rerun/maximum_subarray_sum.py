def findMaximum(nums):
    sum = 0
    max_sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        max_sum = max(max_sum, sum)
        if sum < 0:
            sum = 0
    return max_sum


print(findMaximum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
