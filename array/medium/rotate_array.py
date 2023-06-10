def rotate_array(matrix):
    left = 0
    right = len(matrix) - 1
    while left <= right:
        top, bottom = left, right
        for i in range(right - left):
            # Save the top left element
            topleft = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topleft
        left += 1
        right -= 1


matrix = [
    [2, 29, 20, 26, 16, 28],
    [12, 27, 9, 25, 13, 21],
    [32, 33, 32, 2, 28, 14],
    [13, 14, 32, 27, 22, 26],
    [33, 1, 20, 7, 21, 7],
    [4, 24, 1, 6, 32, 34],
]

rotate_array(matrix)
for ele in matrix:
    print(ele)
