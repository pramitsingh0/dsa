def longest_consecutive(nums):
    nums_set = set(nums)
    longestStreak = 0
    for num in nums:
        if num - 1 not in nums_set:
            currentStreak = 1
            currentNum = num
            while currentNum + 1 in nums_set:
                currentStreak += 1
                currentNum += 1
            longestStreak = max(currentStreak, longestStreak)

    return longestStreak


print(longest_consecutive([100, 200, 1, 3, 2, 4]))
print(longest_consecutive([3, 8, 5, 7, 6]))
