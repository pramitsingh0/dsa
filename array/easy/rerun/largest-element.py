def largest(nums):
    largest = None
    for ele in nums:
        if largest == None or ele > largest:
            largest = ele
    return largest
