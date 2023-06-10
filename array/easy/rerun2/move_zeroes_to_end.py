def moveZeros(nums):
    k = 0
    while k < len(nums):
        if nums[k] == 0:
            break
        k += 1
    i = k
    j = k + 1
    while i < len(nums) and j < len(nums):
        if nums[j] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
        j += 1
    return nums


print(moveZeros([1, 0, 2, 3, 0, 4, 0, 1]))
