def next_permutation(arr):
    n = len(arr)
    bp_index = -1
    i = n - 2
    while i >= 0:
        if arr[i] < arr[i + 1]:
            bp_index = i
            break
        i -= 1
    if bp_index == -1:
        arr.reverse()
        print("reversed")
        return arr
    smaller_than_bp = bp_index + 1
    for i in range(bp_index + 1, n):
        if arr[i] < arr[smaller_than_bp] and arr[i] > arr[bp_index]:
            smaller_than_bp = i
    arr[bp_index], arr[smaller_than_bp] = arr[smaller_than_bp], arr[bp_index]
    return arr[: bp_index + 1] + merge_sort(arr[bp_index + 1 :])


def merge(arr1, arr2):
    i = 0
    j = 0
    aux_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            aux_arr.append(arr1[i])
            i += 1
        else:
            aux_arr.append(arr2[j])
            j += 1
    aux_arr.extend(arr1[i:])
    aux_arr.extend(arr2[j:])
    return aux_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    return merge(left_half, right_half)


print(next_permutation([1, 3, 2]))
