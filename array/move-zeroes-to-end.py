## My Implmentation
def move_zeroes(arr):
    i = 0
    for j in range(len(arr)):
        if arr[j] == 0:
            i = j
            while i < len(arr) - 1:
                if arr[i] != 0:
                    break
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return arr


def move_zeroes_eff(arr):
    k = 0
    while k < len(arr):
        if arr[k] == 0:
            break
        k += 1
    i = k
    j = k + 1
    while i < len(arr) and j < len(arr):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1
    return arr


print(move_zeroes_eff([1, 2, 0, 1, 0, 4, 0]))
