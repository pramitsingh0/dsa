def findFloor(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            return mid
        else:
            high = mid
    return -1

print(findFloor([1,2,8,10,11,12,19], 5))