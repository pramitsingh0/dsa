def find_majority(nums):
    count = 0
    element = None
    for i in range(len(nums)):
        if count == 0:
            element = nums[i]
        if nums[i] == element:
            count += 1
        else:
            count -= 1
    return element


print(find_majority([2, 2, 1, 1, 1, 2, 2]))
