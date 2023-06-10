def findMaximum(nums):
    count = 0
    maximum_count = 0
    for ele in nums:
        if ele == 0:
            count = 0
        else:
            count += 1
        maximum_count = max(count, maximum_count)

    return maximum_count


nums = list(map(int, input("").strip().split()))

print(findMaximum(nums))
