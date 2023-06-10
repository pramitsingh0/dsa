def findInterserction(arr1, arr2):
    i = 0
    j = 0
    m = len(arr1)
    n = len(arr2)
    intersection_arr = []
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            if len(intersection_arr) == 0 or intersection_arr[-1] != arr2[j]:
                intersection_arr.append(arr1[i])
            i += 1
            j += 1
    return intersection_arr


print(findInterserction([1, 3, 4, 5, 7], [2, 3, 5, 6]))
