def rearrange_array(nums):
    pos_ind = 0
    neg_ind = 1
    result = [0] * len(nums)
    for i in range(len(nums)):
        if nums[i] > 0 and pos_ind < len(nums):
            result[pos_ind] = nums[i]
            pos_ind += 2
        elif nums[i] < 0 and neg_ind < len(nums):
            result[neg_ind] = nums[i]
            neg_ind += 2
    return result


print(rearrange_array([1, 2, 3, -1, -2, -3]))
