def multiply(n, m):
    prod = 1
    for i in range(n):
        prod *= m
    return prod


def findRoot(n, m):
    low = 1
    high = m
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        prod = multiply(n, mid)
        if prod <= m:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans


print(findRoot(5, 243))
