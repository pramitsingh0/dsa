def findUnion(arr1, arr2):
    i = 0
    j = 0
    union_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if len(union_array) == 0 or union_array[-1] != arr1[i]:
                union_array.append(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            if len(union_array) == 0 or union_array[-1] != arr2[j]:
                union_array.append(arr2[j])
            j += 1
        else:
            if (
                len(union_array) == 0
                or union_array[-1] != arr1[i]
                or union_array[-1] != arr2[j]
            ):
                union_array.append(arr1[i])
            j += 1
            i += 1

    while i < len(arr1):
        if len(union_array) == 0 or union_array[-1] != arr1[i]:
            union_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        if len(union_array) == 0 or union_array[-1] != arr2[j]:
            union_array.append(arr2[j])
        j += 1
    return union_array


print(findUnion([1, 2, 3, 4, 5], [2, 3, 4, 4, 5]))
