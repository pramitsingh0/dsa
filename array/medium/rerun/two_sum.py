def two_sums(nums, target):
    nums_freq = {}
    for i in range(len(nums)):
        nums_freq[nums[i]] = i
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_freq:
            return [i, nums_freq[diff]]
    return [-1, -1]


print(two_sums([2, 6, 5, 8, 11], 14))
