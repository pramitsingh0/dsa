def searchMatrix(matrix, target):
    t = 0
    b = len(matrix) - 1
    l = 0
    r = len(matrix[0]) - 1
    containing_row = 0
    while t <= b:
        m = (t + b) // 2
        if matrix[m][0] <= target and matrix[m][r] >= target:
            containing_row = m
            break
        if matrix[m][0] > target:
            b = m - 1
        elif matrix[m][r] < target:
            t = m + 1

    while l <= r:
        m = (l + r) // 2
        if matrix[containing_row][m] == target:
            return True
        
        if target > matrix[containing_row][m]:
            l = m + 1
        else:
            r = m - 1
    return False






matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix, 30))