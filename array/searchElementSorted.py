def bin_search(arr, size, ele):
    high, low = size - 1, 0
    while True:
        mid = (high + low) // 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            high = mid - 1
        elif arr[mid] < ele:
            low = mid + 1
        if high < low:
            return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    size = 10
    ele = 11
    print(bin_search(arr, size, ele))
