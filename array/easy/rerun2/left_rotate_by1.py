def leftRotateByOne(nums):
    if len(nums) < 1:
        return -1
    return nums[1:] + nums[:1]


print(leftRotateByOne([3]))
