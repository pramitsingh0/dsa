def findMissingRepeatingNumbers(nums):
    n = len(nums)
    sn = n * (n + 1) / 2
    s2n = n * (n + 1) * (2 * n + 1) / 6
    s = 0
    s2 = 0

    for i in range(n):
        s += nums[i]
        s2 += nums[i] * nums[i]

    val2 = abs(s2 - s2n)
    val1 = abs(s - sn)
    val2 = val2 / val1

    x = (val2 + val1) / 2
    y = x - val1

    return {int(x), int(y)}


print(findMissingRepeatingNumbers([3, 1, 2, 5, 3]))
