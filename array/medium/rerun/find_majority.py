def findMajority(nums):
    count = 0
    majorEle = 0
    for ele in nums:
        if count == 0:
            majorEle = ele
        if ele != majorEle:
            count -= 1
        else:
            count += 1
    return majorEle


print(findMajority([2, 2, 1, 1, 1, 2, 2]))
