def arrangeArray(nums):
    newArray = [0] * len(nums)
    pos_ind = 0
    neg_ind = 1
    for i in range(len(nums)):
        if nums[i] > 0 and pos_ind < len(nums):
            newArray[pos_ind] = nums[i]
            pos_ind += 2
        elif nums[i] < 0 and neg_ind < len(nums):
            newArray[neg_ind] = nums[i]
            neg_ind += 2
    return newArray


print(arrangeArray([1, 2, 3, -1, -2, -3]))
