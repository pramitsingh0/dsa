def find_element(arr, size, key):
    for i in range(size):
        if arr[i] == key:
            return i
    return -1
def delete_element(arr, size, key):
    ele_index = find_element(arr, size, key)
    if ele_index < 0: return "Element not found"
    for i in range(ele_index, size - 1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    size = 5
    key = 2
    print(delete_element(arr, size, key))
