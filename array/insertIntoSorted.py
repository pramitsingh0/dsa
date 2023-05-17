def insert_into_sorted(arr, size, ele):
    i = size - 1
    arr.append(0)
    while i >= 0 and arr[i] > ele:
        arr[i + 1] = arr[i]
        i -= 1
    arr[i + 1] = ele
    return arr

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    size = len(arr)
    ele = 4
    print(insert_into_sorted(arr, size, ele))
