def longest_subarray_sum(nums, k):
    prefix_sum = {}
    sum = 0
    longest = 0
    for i in range(len(nums)):
        sum += nums[i]
        prefix_sum[sum] = i
        if sum == k:
            longest = i + 1
        elif sum > k:
            prev_sum = sum - k
            if prev_sum in prefix_sum:
                diff = i - prefix_sum[prev_sum]
                if diff > longest:
                    longest = diff
    return longest


print(longest_subarray_sum([-1, 1, 1], 1))
