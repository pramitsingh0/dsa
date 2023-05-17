def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        smallest_ind = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_ind]:
                smallest_ind = j
        arr = swap(arr, i, smallest_ind)
    return arr


print(selection_sort([12, 46, 24, 52, 20, 9]))

# Best case and worst case both are O(n^2) because even if the list is sorted, we have go through the entire list
