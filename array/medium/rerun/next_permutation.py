def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    bp_index = -1
    while i >= 0:
        if nums[i] < nums[i + 1]:
            bp_index = i
        i -= 1
    if bp_index == -1:
        nums.reverse()
        return nums
    # Swap element
    for i in range(n - 1, bp_index, -1):
        if nums[i] > nums[bp_index]:
            nums[i], nums[bp_index] = nums[bp_index], nums[i]
            break
    return nums[: bp_index + 1] + sorted(nums[bp_index + 1 :])


print(nextPermutation([2, 1, 5, 4, 3, 0, 0]))
