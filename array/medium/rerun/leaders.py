def findLeaders(nums):
    i = len(nums) - 1
    current_biggest = None
    result = []
    while i >= 0:
        if current_biggest == None or nums[i] > current_biggest:
            current_biggest = nums[i]
            result.append(current_biggest)
        i -= 1
    return result


print(findLeaders([10, 22, 12, 3, 0, 6]))
