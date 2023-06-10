def linear_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    return -1