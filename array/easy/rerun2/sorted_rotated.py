def check_sorted_rotated(nums):
    count = 0
    for i in range(len(nums) - 1):
        if nums[i] > nums[(i + 1) % len(nums)]:
            count += 1

    return count <= 1


print(check_sorted_rotated([1, 2, 3, 4, 5]))
print(check_sorted_rotated([4, 1, 5, 2, 3]))
