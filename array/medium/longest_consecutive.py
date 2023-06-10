def longestConsecutive(nums):
    nums_set = set(nums)
    max_seq = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            currentStreak = 1
