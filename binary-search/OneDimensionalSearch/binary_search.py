def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high)//2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid
        else:
            return mid
    return -1

print(binarySearch([2,3,7,10,13,14,17], 14))