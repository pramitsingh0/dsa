def find_missing(nums):
    num_freq = {}
    # you can also do dict.fromkeys(nums, 0) to get {1: 0, 2: 0, 3: 0} etc.
    for i in range(len(nums) + 1):
        num_freq[i] = 0
    for ele in nums:
        num_freq[ele] = 1
    for key in num_freq:
        if num_freq[key] == 0:
            return key
    return -1


# a better implementation
def find_missing_eff(nums):
    num_freq = dict.fromkeys(nums, 0)
    print(num_freq)
    for i in range(len(nums)):
        if not i in num_freq:
            return i


# A bit more mathematical solution
def missing_num(nums):
    n = len(nums)
    actual_sum = sum(nums)
    expected_sum = n * (n + 1) / 2
    return int(expected_sum - actual_sum)


print(missing_num([3, 0, 1]))
