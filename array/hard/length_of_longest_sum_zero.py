def lengthOfLargest(nums):
    n = len(nums)
    sums = 0
    nums_hash = {}
    largestSub = 0
    currentLargest = 0
    for i in range(n):
        sums += nums[i]
        if sums == 0:
            largestSub = i + 1
        else:
            if sums in nums_hash:
                currentLargest = i - nums_hash[sums]
                largestSub = max(currentLargest, largestSub)
            else:
                nums_hash[sums] = i
    return largestSub

print(lengthOfLargest([6, -2, 2, -8, 1, 7, 4, -10]))
