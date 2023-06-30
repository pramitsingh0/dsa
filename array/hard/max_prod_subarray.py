def findMaxProd(nums):
    n = len(nums)
    pref = 1
    suff = 1
    max_prod = 1
    for i in range(n):
        pref *= nums[i]
        suff *= nums[n - i - 1]
        if pref == 0:
            pref = 1
        if suff == 0:
            suff = 1

        max_prod = max(max_prod, max(pref, suff))

    return max_prod


print(findMaxProd([1, 2, -3, 0, -4, -5]))
