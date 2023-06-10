def spiral_matrix(matrix):
    left = 0
    right = len(matrix[0])
    top = 0
    bottom = len(matrix)
    aux_array = []
    while left < right and top < bottom:
        for i in range(left, right):
            aux_array.append(matrix[top][i])
        top += 1
        for i in range(top, bottom):
            aux_array.append(matrix[i][right - 1])
        right -= 1
        if left >= right or top >= bottom:
            break
        for i in range(right - 1, left - 1, -1):
            aux_array.append(matrix[bottom - 1][i])
        bottom -= 1
        for i in range(bottom - 1, top - 1, -1):
            aux_array.append(matrix[i][left])
        left += 1

    return aux_array
