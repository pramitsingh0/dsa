def find_intersection(arr1, arr2):
    i = 0
    j = 0
    aux_array = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            aux_array.append(arr1[i])
            i += 1
            j += 1
    return aux_array
print(find_intersection([1, 2, 3, 3, 4, 5, 6], [3, 3, 5]))