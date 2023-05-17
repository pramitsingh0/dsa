def reverse_array(a, high, low):
    high, low = len(a) - 1, 0
    if high <= low: return
    temp = a[low]
    a[low] = a[high]
    a[high] = temp
