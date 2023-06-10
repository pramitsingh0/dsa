def fourSum(nums, target):
    result = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = len(nums) - 1
            while k < l:
                sums = nums[i] + nums[j] + nums[k] + nums[l]
                if sums > target:
                    l -= 1
                elif sums < target:
                    k += 1
                else:
                    result.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return result


print(fourSum([4, 3, 3, 4, 4, 2, 1, 2, 1, 1], 9))
