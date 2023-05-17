def reverse_array(arr, start, end):
    if start >= end:
        return arr
    temp = arr[end]
    arr[end] = arr[start]
    arr[start] = temp
    return reverse_array(arr, start + 1, end - 1)


arr = [1, 2, 3, 4, 5]
print(reverse_array(arr, 0, len(arr) - 1))
