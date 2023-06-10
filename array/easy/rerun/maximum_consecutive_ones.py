def maximum_consecutive_ones(arr):
    max_ones = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            if max_ones < count:
                max_ones = count
            count = 0
            continue
        count += 1
    max_count = max(count, max_ones)
    return max_count
print(maximum_consecutive_ones([1, 0, 1, 1, 0, 1]))