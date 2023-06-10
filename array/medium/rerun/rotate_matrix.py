def rotateMatrix(matrix):
    left = 0
    right = len(matrix) - 1
    while left < right:
        top = left
        bottom = right
        for i in range(right - left):
            # save topLeft corner of square
            top_left = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = top_left
        left += 1
        right -= 1
    return matrix


print(rotateMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
