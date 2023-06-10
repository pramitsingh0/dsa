def two_sum(nums, target):
    nums_freq = dict()
    for i in range(len(nums)):
        nums_freq[nums[i]] = i
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums_freq:
            return [i, nums_freq[diff]]

    return [-1, -1]
