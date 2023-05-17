def delete_from_sorted(arr, n, ele):
    ele_index = bin_search(arr, n, ele)
    for i in range(ele_index, n - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    print(arr)

def bin_search(arr, n, ele):
    high, low = n - 1, 0
    while high > low:
        mid = high + low // 2

        if arr[mid] == ele:
            return mid
        elif arr[mid] < ele:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    ele = 10

    delete_from_sorted(arr, n, ele)
