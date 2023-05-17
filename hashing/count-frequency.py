def count_freq(arr):
    count = {}
    for ele in arr:
        if ele in count:
            count[ele] += 1
        else:
            count[ele] = 1
    return count


print(count_freq([1, 2, 3, 1, 2, 1, 3, 1]))
