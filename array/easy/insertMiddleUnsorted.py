def insert_middle(arr, size, ele, pos):
    if pos < 0 or pos > size:
        return -1
    for i in range(size - 1, pos, -1):
        if (i == size - 1):
            arr.append(arr[i])
        arr[i] = arr[i - 1]
    arr[pos] = ele
    return arr

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5, 6, 7]
    size = 7
    ele = 8
    pos = 2
    print(insert_middle(arr1, size, ele, pos))
