def findLongestSub(nums, k):
    prefix_sum = {}
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        prefix_sum[sum] = i
        if sum == k:
            return i + 1
        elif sum > k:
            diff = sum - k
            if diff in prefix_sum:
                return i - prefix_sum[diff]
    return -1


nums = list(map(int, input("Enter Nums: ").strip().split()))
k = int(input())

print(findLongestSub(nums, k))
