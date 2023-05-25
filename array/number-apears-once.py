# Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
def single_num(nums) -> int:
    xorr = 0
    for i in nums:
        xorr = xorr ^ i
    return xorr


print(single_num([4, 1, 2, 1, 2]))
