def find_num(arr):
    num = 0 
    for ele in arr:
        num = num ^ ele
    return num

print(find_num([4, 1, 2, 1, 2]))