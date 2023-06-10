def maximum_subarray(arr):
    i = 0
    sum_store = {}
    while i < len(arr):
        sum = 0
        j = i
        while j < len(arr):
            sum += arr[j]
            sum_store[sum] = [i, j]
            j += 1
        i += 1
    max_sum = max(sum_store.keys())
    return max_sum


# kadane's algorithm
def maximum_sub_kadane(nums):
    max = None
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        if max == None or sum > max:
            max = sum
        if sum < 0:
            sum = 0
    return max


# print(maximum_sub_kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maximum_sub_kadane([5, 4, -1, 7, 8]))
