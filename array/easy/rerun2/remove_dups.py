def removeDups(nums):
    i = 0
    j = 0
    while j < len(nums):
        if nums[j] != nums[i]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
    return nums


print(removeDups([1, 1, 2, 2, 2, 3, 3]))
print(removeDups([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4]))
